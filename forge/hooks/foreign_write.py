# card: C1-5
"""PreToolUse hook (cards C1-5, B9): refuses a write under a root of forge/hooks/protected-roots.json.

foreign_write.py [--root D]   the tool call JSON arrives on the input; D (default: this repository) holds the roots file.
Judged: file_path and notebook_path of Write, Edit, MultiEdit, NotebookEdit; the command of Bash and PowerShell, where only
LITERAL paths in a named write position count (redirects, tee, cp/install/rsync destination, mv, rm, sed -i, git outside
its read list, the PowerShell write cmdlets...). Other tools pass. Exit 2 refuses; every case the hook cannot judge (input,
roots file, its own error) exits 0 with one stderr line "foreign_write not checked: <why>".
Residuals, named: a symlink, junction, `~`, a variable, a script, an alias or an indirect write errs GREEN; so does an agent
editing the roots file or a live hook (the acceptance diff is the net).
"""
import argparse
import json
import os
import posixpath
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from hio import io as HIO  # noqa: E402

DOOR = ("a protected root is written by the person only; the list changes by a reviewed commit of "
        "forge/hooks/protected-roots.json")
FILE_TOOLS, SHELLS = ("Write", "Edit", "MultiEdit", "NotebookEdit"), ("Bash", "PowerShell")
GIT_READ = ("status", "log", "show", "diff", "rev-parse", "ls-files", "ls-tree", "cat-file", "grep", "rev-list",
            "merge-base", "blame", "describe", "for-each-ref", "shortlog")
EVERY = ("rm", "rmdir", "mkdir", "touch", "unlink", "ln", "tee", "truncate")
PS_FIRST = ("set-content", "sc", "add-content", "ac", "out-file", "clear-content", "clc", "new-item", "ni", "remove-item",
            "ri", "rm", "del", "erase", "rd", "rmdir", "rename-item", "rni", "ren", "md", "mkdir")
PS_COPY, PS_MOVE = ("copy-item", "cpi", "cp", "copy"), ("move-item", "mi", "mv", "move")
PS_PATH = ("path", "literalpath", "filepath", "destination", "pspath", "lp")
PS_VALUE = ("value", "encoding", "itemtype", "type", "stream", "filter", "include", "exclude", "width", "newname",
            "name", "delimiter", "inputobject")


def norm(p, cwd=""):
    """Unify slashes, MSYS /c/x -> c:/x, collapse .., fold case; a relative path resolves against cwd."""
    p = re.sub(r"^/([A-Za-z])(?=/|$)", r"\1:", p.replace("\\", "/"))
    if cwd and not re.match(r"[A-Za-z]:/|/", p):
        p = norm(cwd) + "/" + p
    return posixpath.normpath(p).lower()


def under(t, root):
    """A root covers itself and what lies under it, by whole components."""
    return t == root or t.startswith(root.rstrip("/") + "/")


def tokens(cmd):
    """Words ("w", text) and operators ("op", text): ; && || | & ( ) > >> >| >& < and a newline (as ;). Quotes are removed,
    a backslash outside them stays (Windows paths), a heredoc body is skipped, an fd prefix of a redirect is dropped."""
    out, buf, have, q, i, hd, want = [], "", False, None, 0, [], False

    def flush():
        nonlocal buf, have, want
        if have:
            out.append(("w", buf))
            if want:
                hd.append((buf, out[-2][1] == "<<-"))
            want = False
        buf, have = "", False

    while i < len(cmd):
        c = cmd[i]
        if q:
            if c == "\\" and q == '"' and cmd[i + 1:i + 2] == '"':
                buf, i = buf + '"', i + 1
            elif c == q:
                q = None
            else:
                buf += c
        elif c in "'\"":
            q, have = c, True
        elif c in " \t\r":
            flush()
        elif c == "\n":
            flush()
            out.append(("op", ";"))
            for d, dash in hd:
                while i + 1 < len(cmd):
                    j = cmd.find("\n", i + 1)
                    j = len(cmd) if j < 0 else j
                    line, i = cmd[i + 1:j], j
                    if line.rstrip("\r").lstrip("\t" if dash else "") == d:
                        break
            hd = []
        elif c in ";|&()<>":
            if c == ">" and have and buf.isdigit():
                buf, have = "", False
            flush()
            op = c
            for two in (">>", ">|", ">&", "&>>", "&>", "&&", "||", "<<<", "<<-", "<<"):
                if cmd.startswith(two, i):
                    op = two
                    break
            i += len(op) - 1
            out.append(("op", ">" if op in ("&>", "&>>", ">|") else op))
            want = op in ("<<", "<<-")
        else:
            buf, have = buf + c, True
        i += 1
    flush()
    return out


def events(cmd):
    """("(",), (")",) and ("seg", words, redirect targets) in command order."""
    ev, words, reds, red = [], [], [], None

    def end():
        nonlocal words, reds
        if words or reds:
            ev.append(("seg", words, reds))
        words, reds = [], []

    for kind, t in tokens(cmd):
        if kind == "op" and t in (">", ">>", ">&"):
            red = t
        elif kind == "op" and t.startswith("<"):
            red = "<"
        elif kind == "op":
            end()
            if t in "()":
                ev.append((t,))
        elif red:
            if red == "<" or (red == ">&" and re.fullmatch(r"\d+|-", t)):
                pass
            else:
                reds.append(t)
            red = None
        else:
            words.append(t)
    end()
    return ev


def positional(args, takes=()):
    out, i = [], 0
    while i < len(args):
        if args[i] == "--":
            return out + args[i + 1:]
        if args[i] in takes:
            i += 1
        elif not args[i].startswith("-"):
            out.append(args[i])
        i += 1
    return out


def dest_opt(args):
    for i, a in enumerate(args):
        if a == "-t" and i + 1 < len(args):
            return args[i + 1]
        if a.startswith("--target-directory="):
            return a.split("=", 1)[1]
    return None


def ps_paths(head, args):
    """PowerShell write cmdlets: -Path/-LiteralPath/-FilePath/-Destination values, else the first positional (Copy-Item:
    the destination; Move-Item: both). A comma list is several paths."""
    named, pos, dest, i = [], [], None, 0
    while i < len(args):
        a = args[i]
        nm, _, val = a[1:].partition(":") if a.startswith("-") and len(a) > 1 else ("", "", "")
        if nm.lower() in PS_PATH + PS_VALUE:
            val = val or (args[i + 1] if i + 1 < len(args) else "")
            i += 0 if a[1:].count(":") else 1
            if nm.lower() == "destination":
                dest = val
            elif nm.lower() in PS_PATH:
                named.append(val)
        elif not a.startswith("-"):
            pos.append(a)
        i += 1
    if head in PS_COPY:
        return [dest] if dest else (pos[1:2] if not named else pos[:1])
    if head in PS_MOVE:
        return [x for x in named + ([dest] if dest else []) + pos][:2]
    return [p for x in (named or pos[:1]) for p in x.split(",")]


def git_writes(args, cwd):
    """The tree a git command writes, or [] for a read command. Last -C wins; clone writes its destination."""
    tree, i = norm(cwd) if cwd else cwd, 0
    while i < len(args) and args[i].startswith("-"):
        if args[i] == "-C" and i + 1 < len(args):
            tree = norm(args[i + 1], cwd)
        i += 2 if args[i] in ("-C", "-c") else 1
    if i >= len(args):
        return []
    sub, rest = args[i], args[i + 1:]
    if sub == "clone":
        p = positional(rest, ("-b", "--branch", "--depth", "-o", "--origin", "--reference", "-c", "--config", "-j"))
        return [norm(p[1], tree)] if len(p) > 1 else (
            [norm(re.sub(r"(\.git)?/*$", "", p[0]).rsplit("/", 1)[-1].rsplit(":", 1)[-1], tree)] if p else [])
    read = sub in GIT_READ or (sub == "config" and any(a.startswith("--get") for a in rest)) or (
        sub == "worktree" and rest[:1] == ["list"]) or (sub == "remote" and "-v" in rest)
    return [] if read else [tree]


def writes(head, args, ps):
    """The literal path words the command head writes (relative ones are resolved by the caller)."""
    if ps and head in PS_FIRST + PS_COPY + PS_MOVE:
        return ps_paths(head, args)
    p = positional(args, ("-m", "-o", "-g", "-S", "-t") if head in ("cp", "install", "mv", "rsync", "mkdir") else (
        ("-s", "-r", "--size", "--reference") if head == "truncate" else ()))
    if head in EVERY:
        return p
    if head in ("chmod", "chown", "chgrp"):
        return p[1:]
    if head in ("cp", "install", "rsync"):
        t = dest_opt(args)
        return [t] if t else (p if head == "install" and "-d" in args else p[-1:])
    if head == "mv":
        return p + ([dest_opt(args)] if dest_opt(args) else [])
    if head in ("sed", "perl") and any(re.match(r"-[A-Za-z]*i", a) or a == "--in-place" for a in args):
        script = any(a in ("-e", "-f", "--expression", "--file") for a in args)
        return positional(args, ("-e", "-f", "--expression", "--file"))[0 if script else 1:]
    if head == "dd":
        return [a[3:] for a in args if a.startswith("of=")]
    return []


def targets(cmd, cwd, ps):
    """Every normalised write target of a shell command; `cd` moves the base, a parenthesis scopes it."""
    out, stack = [], []
    for ev in events(cmd):
        if ev[0] == "(":
            stack.append(cwd)
        elif ev[0] == ")":
            cwd = stack.pop() if stack else cwd
        else:
            _, words, reds = ev
            while words and re.match(r"[A-Za-z_]\w*=", words[0]):
                words = words[1:]
            out += [norm(r, cwd) for r in reds if usable(r)]
            if not words:
                continue
            head = re.sub(r"\.exe$", "", posixpath.basename(words[0].replace("\\", "/")).lower())
            if head in ("cd", "set-location", "sl", "pushd"):
                a = positional(words[1:])
                if a and usable(a[-1]) and a[-1] != "-":
                    cwd = norm(a[-1], cwd)
            elif head == "git":
                out += git_writes(words[1:], cwd)
            else:
                out += [norm(w, cwd) for w in writes(head, words[1:], ps) if usable(w)]
    return out


def usable(p):
    """A variable or `~` is not resolved: errs green (named residual)."""
    return bool(p) and "$" not in p and not p.startswith("~")


def judge(payload, roots):
    """Return ("pass",), ("skip", why) or ("refuse", target, root)."""
    if not isinstance(payload, dict) or not isinstance(payload.get("tool_name"), str):
        return ("skip", "no tool_name in the input")
    tool, ti, cwd = payload["tool_name"], payload.get("tool_input"), payload.get("cwd")
    cwd = cwd if isinstance(cwd, str) else ""
    if tool not in FILE_TOOLS + SHELLS:
        return ("pass",)
    if not isinstance(ti, dict):
        return ("skip", "no tool_input")
    if tool in SHELLS:
        cmd = ti.get("command")
        ts = targets(cmd, cwd, tool == "PowerShell") if isinstance(cmd, str) and cmd.strip() else None
    else:
        ts = [norm(ti[k], cwd) for k in ("file_path", "notebook_path") if isinstance(ti.get(k), str) and ti[k]] or None
    if ts is None:
        return ("skip", "no path or command in tool_input")
    for t in ts:
        for r in roots:
            if under(t, r):
                return ("refuse", t, r)
    return ("pass",)


def load_roots(root):
    """Return (normalised roots, why): why is set for an absent, unreadable, empty or non-absolute list."""
    p = os.path.join(root, "forge", "hooks", "protected-roots.json")
    try:
        with open(p, encoding="utf-8") as fh:
            roots = json.load(fh).get("roots")
    except (OSError, ValueError, AttributeError) as exc:
        return [], "roots file %s: %s" % (p, exc)
    if not isinstance(roots, list) or not roots or not all(
            isinstance(r, str) and re.match(r"[A-Za-z]:[/\\]|/", r) for r in roots):
        return [], "roots file %s: needs a non-empty list of absolute roots" % p
    return [norm(r) for r in roots], None


def body(payload, note, root):
    roots, why = load_roots(root)
    if payload is None or why:
        print("foreign_write not checked: %s" % (why or note), file=sys.stderr)
        return 0
    v = judge(payload, roots)
    if v[0] == "skip":
        print("foreign_write not checked: %s" % v[1], file=sys.stderr)
    if v[0] != "refuse":
        return 0
    print("foreign_write: refused %s under protected root %s: %s" % (v[1], v[2], DOOR), file=sys.stderr)
    HIO.journal(root, "refuse", "foreign_write", payload.get("session_id"), "foreign_write: " + DOOR)
    return 2


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(HERE)))
    a = ap.parse_args()
    sys.exit(HIO.guard(lambda v, n: body(v, n, a.root), "pass", "json"))
