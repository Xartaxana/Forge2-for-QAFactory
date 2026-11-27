# card: C1-5
# hook: PreToolUse
"""PreToolUse hook (cards C1-5, B9): refuses a write under a root of forge/hooks/protected-roots.json.

foreign_write.py [--root D]   the tool call JSON arrives on the input; D (default: this repository) holds the roots file.
Judged: file_path and notebook_path of Write, Edit, MultiEdit, NotebookEdit; the command of Bash and PowerShell, where only
LITERAL paths in a named write position count (redirects, tee, cp/install/rsync destination, mv, rm, sed -i, git outside
its read list, the PowerShell write cmdlets...). Other tools pass. Exit 2 refuses; every case the hook cannot judge (input,
roots file, its own error, a bad argument) exits 0 with one stderr line "foreign_write not checked: <why>". A refusal
journals one line; a crash and a refusal with no session id journal nothing (stderr only; B17 owns the policy).
Cuts: none of its own (a path or command is judged whole). A shell line continuation (an ODD run of unquoted backslashes, in
PowerShell backticks, before a line end) joins the lines; an even run is literal text and the line end separates; inside
quotes nothing joins. The same character escapes a quote character on an odd run only.
Residuals, named: a symlink, junction, `~`, a variable, a script, an alias or an indirect write errs GREEN; so do a UNC admin
share (//host/C$) and an 8.3 short name (they are not resolved); so does an agent editing the roots file or a live hook (the
acceptance diff is the net); so do git path arguments other than the work tree, git-dir, clone/init/worktree add targets
and --separate-git-dir (e.g. worktree move, archive -o, diff --output, format-patch -o, bundle create, submodule add); so
do Bash ANSI-C quoting (the dollar-quote $'...'), an abbreviated long option (git --sep=) and a value-taking option missing
from the arity lists (git init --ref-format, git clone --template / -u and the rest of clone -h value options; the target
is misread). The hook is protection against an agent's accidental write, not against an adversary.
"""
import json
import os
import posixpath
import re
import sys
from collections import namedtuple

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
    """Unify slashes, drop a leading //?/ or //./ (//?/UNC/ -> //), drop trailing dots and spaces of each component (Win32
    does), MSYS /c/x -> c:/x, collapse .., fold case; a relative path resolves against cwd."""
    p = re.sub(r"^//[?.]/(UNC/)?", lambda m: "//" if m.group(1) else "", p.replace("\\", "/"), flags=re.I)
    p = "/".join(c if c in (".", "..") else c.rstrip(". ") for c in p.split("/"))
    p = re.sub(r"^/([A-Za-z])(?=/|$)", r"\1:", p)
    if cwd and not re.match(r"[A-Za-z]:/|/", p):
        p = norm(cwd) + "/" + p
    return posixpath.normpath(p).lower()


def under(t, root):
    """A root covers itself and what lies under it, by whole components."""
    return t == root or t.startswith(root.rstrip("/") + "/")


def eol(cmd, i):
    """The length of the line end at cmd[i]: 2 for CRLF, 1 for LF, else 0."""
    return 2 if cmd.startswith("\r\n", i) else int(cmd.startswith("\n", i))


def escaped(cmd, i, cont):
    """True when an odd run of cont directly precedes cmd[i] (a cont or a quote), so cmd[i] is literal text. A run holds no
    quote, so it shares cmd[i]'s quote state; the walk is bounded by the run."""
    j = i
    while j > 0 and cmd[j - 1] == cont:
        j -= 1
    return (i - j) % 2 == 1


def skip_heredocs(cmd, i, hd):
    """i is the newline that ends a line with heredocs hd: return the index of the last newline of their bodies."""
    for d, dash in hd:
        while i + 1 < len(cmd):
            j = cmd.find("\n", i + 1)
            j = len(cmd) if j < 0 else j
            line, i = cmd[i + 1:j], j
            if line.rstrip("\r").lstrip("\t" if dash else "") == d:
                break
    return i


def in_quote(cmd, i, q, buf, cont):
    """One character inside quote q: (buf, q) after it. Quotes are removed from the word; an odd run escapes a closing
    double quote (t-1985 N7: ps: backtick, never backslash)."""
    c = cmd[i]
    if c != q:
        return buf + c, q
    if q == '"' and escaped(cmd, i, cont):
        return buf[:-1] + c, q
    return buf, None


def op_at(cmd, i):
    """The operator that starts at cmd[i] (a character of ;|&()<>): the longest of the two- and three-character forms."""
    for two in (">>", ">|", ">&", "&>>", "&>", "&&", "||", "<<<", "<<-", "<<"):
        if cmd.startswith(two, i):
            return two
    return cmd[i]


def tokens(cmd, ps=False):
    """Words ("w", text) and operators ("op", text): ; && || | & ( ) > >> >| >& < and a newline (as ;). Quotes are removed,
    a backslash outside them stays (Windows paths), a heredoc body is skipped, an fd prefix of a redirect is dropped. An
    unquoted backslash (ps: backtick) directly before LF or CRLF joins the lines unless it is itself escaped (t-1984 N1:
    `\\`+LF is a literal backslash, then a new command); at the end of the command it is dropped. The same character
    escapes a quote (inside double quotes: only `"`) on an odd run only (t-1985 N7)."""
    out, buf, have, q, i, hd, want = [], "", False, None, 0, [], False
    cont = "`" if ps else "\\"

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
            buf, q = in_quote(cmd, i, q, buf, cont)
        elif c in "'\"" and not escaped(cmd, i, cont):  # an escaped quote outside quotes is a literal (Bash it\'s)
            q, have = c, True
        elif c == cont and eol(cmd, i + 1) and escaped(cmd, i, cont):
            buf, have = buf + c, True
        elif c == cont and eol(cmd, i + 1):
            i += eol(cmd, i + 1)
        elif c in " \t\r":
            flush()
        elif c == "\n":
            flush()
            out.append(("op", ";"))
            i, hd = skip_heredocs(cmd, i, hd), []
        elif c in ";|&()<>":
            if c == ">" and have and buf.isdigit():
                buf, have = "", False
            flush()
            op = op_at(cmd, i)
            i += len(op) - 1
            out.append(("op", ">" if op in ("&>", "&>>", ">|") else op))
            want = op in ("<<", "<<-")
        else:
            buf, have = buf + c, True
        i += 1
    flush()
    return out


def events(cmd, ps=False):
    """("(",), (")",) and ("seg", words, redirect targets) in command order."""
    ev, words, reds, red = [], [], [], None

    def end():
        nonlocal words, reds
        if words or reds:
            ev.append(("seg", words, reds))
        words, reds = [], []

    for kind, t in tokens(cmd, ps):
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
    """cp/install/rsync/mv -t or --target-directory, each in the = and space forms (t-1986 D1, R4)."""
    return long_opt(args, "-t") or long_opt(args, "--target-directory")


def long_opt(args, name):
    """The value of a long option given as `name=V` or `name V`, or None."""
    for i, a in enumerate(args):
        if a == name and i + 1 < len(args):
            return args[i + 1]
        if a.startswith(name + "="):
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


def git_chain(args, cwd, env):
    """The leading options of a git command: (tree after the -C chain, {--git-dir, --work-tree: raw value}, index of the
    subcommand)."""
    tree, i = norm(cwd) if cwd else cwd, 0
    raw = {"--git-dir": env.get("GIT_DIR"), "--work-tree": env.get("GIT_WORK_TREE")}
    while i < len(args) and args[i].startswith("-"):
        name, _, val = args[i].partition("=")
        if args[i] in ("-C", "-c", "--git-dir", "--work-tree") and i + 1 < len(args):
            name, val, i = args[i], args[i + 1], i + 1
        if name == "-C" and usable(val):
            tree = norm(val, tree)
        elif name in raw:
            raw[name] = val
        i += 1
    return tree, raw, i


def clone_targets(rest, tree, named, wt):
    """What `git clone` writes: its destination, a --separate-git-dir and a given work tree."""
    p = positional(rest, ("-b", "--branch", "--depth", "-o", "--origin", "--reference", "-c", "--config", "-j",
                          "--separate-git-dir"))
    dest = p[1:2] or [re.sub(r"(\.git)?/*$", "", x).rsplit("/", 1)[-1].rsplit(":", 1)[-1] for x in p[:1]]
    return sorted({norm(x, tree) for x in dest} | {norm(x, tree) for x in named if usable(x)} | ({wt} if wt else set()))


def more_named(sub, rest):
    """The path an init <dir> or a worktree add <path> names (t-1985 N8, N9)."""
    if sub == "init":
        return positional(rest, ("-b", "--initial-branch", "--template", "--separate-git-dir", "--object-format"))[:1]
    if sub == "worktree" and rest[:1] == ["add"]:
        return positional(rest[1:], ("-b", "-B", "--reason"))[:1]
    return []


def git_reads(sub, rest):
    """True for a git subcommand that writes no tree."""
    return sub in GIT_READ or (sub == "config" and any(a.startswith("--get") for a in rest)) or (
        sub == "worktree" and rest[:1] == ["list"]) or (sub == "remote" and "-v" in rest)


def git_writes(args, cwd, env=None):
    """The trees a git command writes, or [] for a read command. The ONE target-tree resolver, in git's order (t-1984 N2,
    measured): the -C chain first, each -C against the tree the previous one gave; then --git-dir/--work-tree (= or space
    form; an option beats its GIT_DIR=/GIT_WORK_TREE= prefix assignment) resolve against the tree the chain gave. BOTH places
    git writes are judged: the work tree (else the chain's tree) and the git-dir (else the chain's tree, where git finds it;
    measured: `git -C A --work-tree=B commit` moves A's HEAD). Clone writes its destination and a given work tree; the
    paths of init <dir>, worktree add <path> and --separate-git-dir (clone, init) are judged too (t-1985 N8, N9)."""
    tree, raw, i = git_chain(args, cwd, env or {})
    gd, wt = [norm(raw[k], tree) if usable(raw[k]) else None for k in ("--git-dir", "--work-tree")]
    if i >= len(args):
        return []
    sub, rest = args[i], args[i + 1:]
    named = [long_opt(rest, "--separate-git-dir")] if sub in ("clone", "init") else []  # t-1985 N9: named write targets
    if sub == "clone":  # it ignores GIT_DIR but writes a work tree (t-1985 N8, measured)
        return clone_targets(rest, tree, named, wt)
    named += more_named(sub, rest)
    return [] if git_reads(sub, rest) else sorted({wt or tree, gd or tree} | {norm(x, tree) for x in named if usable(x)})


def value_options(head):
    """The options of a write command that take a value (their value is no path)."""
    if head in ("cp", "install", "mv", "rsync", "mkdir"):
        return ("-m", "-o", "-g", "-S", "-t")
    return ("-s", "-r", "--size", "--reference") if head == "truncate" else ()


def inplace_paths(args):
    """sed/perl in place: the files after the script (the first positional, unless -e/-f gave it)."""
    script = any(a in ("-e", "-f", "--expression", "--file") for a in args)
    return positional(args, ("-e", "-f", "--expression", "--file"))[0 if script else 1:]


def writes(head, args, ps):
    """The literal path words the command head writes (relative ones are resolved by the caller)."""
    if ps and head in PS_FIRST + PS_COPY + PS_MOVE:
        return ps_paths(head, args)
    p = positional(args, value_options(head))
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
        return inplace_paths(args)
    if head == "dd":
        return [a[3:] for a in args if a.startswith("of=")]
    return []


Cmd = namedtuple("Cmd", "head args cwd ps env")  # ONE parsed command: head word, its arguments, base dir, shell, VAR= prefixes


def parse(words, cwd, ps):
    """A segment's words -> Cmd, or None when only VAR= assignments are left."""
    env = {}
    while words and re.match(r"[A-Za-z_]\w*=", words[0]):
        k, _, env[k] = words[0].partition("=")
        words = words[1:]
    if not words:
        return None
    head = re.sub(r"\.exe$", "", posixpath.basename(words[0].replace("\\", "/")).lower())
    return Cmd(head, words[1:], cwd, ps, env)


def rule_git(c):
    """A git command: the tree the target-tree resolver gives (None: not a git command)."""
    return git_writes(c.args, c.cwd, c.env) if c.head == "git" else None


def rule_writes(c):
    """Any other command: its literal write-position paths."""
    return [norm(w, c.cwd) for w in writes(c.head, c.args, c.ps) if usable(w)]


# Ordered rule functions over ONE parsed command: the first that returns a list (not None) judges it. B11 adds its rules
# in front of these.
RULES = (rule_git, rule_writes)


def judge_cmd(c):
    for rule in RULES:
        got = rule(c)
        if got is not None:
            return got
    return []


def new_cwd(c):
    """The base after a `cd`: an unusable or `-` argument leaves it."""
    a = positional(c.args)
    return norm(a[-1], c.cwd) if a and usable(a[-1]) and a[-1] != "-" else c.cwd


def targets(cmd, cwd, ps):
    """Every normalised write target of a shell command; `cd` moves the base, a parenthesis scopes it."""
    out, stack = [], []
    for ev in events(cmd, ps):
        if ev[0] == "(":
            stack.append(cwd)
        elif ev[0] == ")":
            cwd = stack.pop() if stack else cwd
        else:
            c = parse(ev[1], cwd, ps)
            out += [norm(r, cwd) for r in ev[2] if usable(r)]
            if c and c.head in ("cd", "set-location", "sl", "pushd"):
                cwd = new_cwd(c)
            elif c:
                out += judge_cmd(c)
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


def run(v, n, argv):
    return HIO.run_root("foreign_write", __doc__, os.path.dirname(os.path.dirname(HERE)), argv, lambda root: body(v, n, root))


if __name__ == "__main__":
    sys.exit(HIO.guard(lambda v, n: run(v, n, sys.argv[1:]), "pass", "json"))
