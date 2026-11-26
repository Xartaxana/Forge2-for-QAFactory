# card: C1-2
"""The one module of every ratchet (F246): finding lines, exit precedence, base and raise lines, one resolver door, and the
one driver of the four list tools (universality, crap, lint, clone): scope, readers, list rules, --update, exit codes.

Exit: 0 green, 1 red, 2 cannot judge (Refuse), 3 part not judged here (red on Actions, TESTING rule 7). Precedence 2 > 1 > 3 > 0.
Finding line: `new: <identity> <detail>`, the identity one token (whitespace written %20); a stale row prints `stale: <id>`.
A list tool is a module with SPEC (a Spec), basis(), scan(root, args, data) -> Scan, and optional add_options / check_args.
"""
import argparse
import ast
import glob
import io
import json
import os
import re
import subprocess
import sys
import tokenize
import warnings

TOOL_VERSION = "1"
ROOTS = ("factory", "forge/tools", "forge/hooks", "measure/tools")  # the C1-3 roots (crap, lint, clone)
RECORD = ("word", "decision")  # the kinds a raise or a --record may resolve to
FUNCS = (ast.FunctionDef, ast.AsyncFunctionDef)
DEFS = FUNCS + (ast.ClassDef,)
BAD = (SyntaxError, ValueError, RecursionError, MemoryError, OSError)  # ValueError holds UnicodeError and a NUL byte
INSTALL = "python -m pip install -r forge/ci-requirements.txt"
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# B20 (d): the old `budget-raise:` keyword is not read. The line may sit anywhere in a message; a quote (`>`) or an indent
# (a fence inside a quote, t-1991 F5) before it is skipped, so such a line counts.
RAISE_RE = re.compile(r"^[ \t>]*ratchet-raise: (\S+) (\S+) -- (\S+)[ \t\r]*$", re.M)


class Refuse(Exception):
    """The ratchet cannot be judged: exit 2 with the message."""


def python_minor():
    return "%d.%d" % sys.version_info[:2]


def encode(text):
    """N23: an identity is one token, whitespace written %20 (F1: encoded where the identity is built, never late)."""
    return re.sub(r"\s", "%20", text)


def label(key):
    """The printed identity of a row key: a tuple key (file, token) is joined by `::`."""
    return encode("::".join(key) if isinstance(key, tuple) else key)


def finding(identity, detail):
    return "new: %s %s" % (encode(identity), detail)


def verdict(codes):
    for code in (2, 1, 3):
        if code in codes:
            return code
    return 0


def parser(desc):
    ap = argparse.ArgumentParser(description=desc)
    ap.add_argument("--root", default=ROOT)
    ap.add_argument("--base")
    return ap


def guarded(fn, *args):
    for stream in (sys.stdout, sys.stderr):  # outside text (a commit message, a file name) never crashes a print
        fix = getattr(stream, "reconfigure", None)
        if fix:
            fix(errors="backslashreplace")
    try:
        return fn(*args)
    except Refuse as exc:
        print("cannot judge: %s" % exc)
        return 2


def read_json(path, what):
    try:
        with open(path, "rb") as fh:
            raw = fh.read()
    except OSError:
        raise Refuse("%s: absent or unreadable" % what)
    try:
        return json.loads(raw.decode("utf-8"))
    except ValueError as exc:  # UnicodeDecodeError is one too
        raise Refuse("%s: not valid UTF-8 JSON (%s)" % (what, exc))


def git(root, *args):
    return subprocess.run(["git", "-C", root] + list(args), capture_output=True)


def text_of(result):
    return result.stdout.decode("utf-8", "replace")  # a non-UTF-8 message is read with replacement


def base_of(root, arg):
    """--base, else FORGE_BASE (ci.py's resolved base, F245), else None. A value that is no commit is exit 2."""
    value = arg or os.environ.get("FORGE_BASE") or ""
    if not value or set(value) == {"0"}:
        return None
    result = git(root, "rev-parse", "--verify", "-q", value + "^{commit}")
    if result.returncode:
        raise Refuse("base %s: not a commit here" % value)
    return text_of(result).strip()


def base_doc(root, base, rel, out):
    """The JSON of rel at the base; None (with its line) when there is no base or the base holds no such file (born)."""
    if base is None:
        out("raises not judged: no base")
        return None
    shown = git(root, "show", "%s:%s" % (base, rel))
    if shown.returncode:
        out("born: %s holds no %s, raises not judged" % (base[:12], rel))
        return None
    try:
        return json.loads(text_of(shown))
    except ValueError as exc:
        raise Refuse("%s:%s: not valid JSON (%s)" % (base[:12], rel, exc))


def resolve(rid, kinds=("word",)):
    """B3's door (F252): None when the record resolves to one of kinds, else the red line. Until B3 there is no registry,
    so every id is red; B3's builder replaces this body with the words.py call."""
    return "cannot resolve %s: no registry" % rid


def judge_raises(root, base, rel, keys, out):
    """keys: {key: (what, kinds)}. Each needs `ratchet-raise: <file> <key> -- <id>` in --base..HEAD, the id resolving to a kind."""
    if not keys:
        return 0
    log = text_of(git(root, "log", "--format=%B", "%s..HEAD" % base))
    lines, code = RAISE_RE.findall(log), 0
    for key, (what, kinds) in keys.items():
        ids = [i for f, k, i in lines if k == key and (rel == f or rel.endswith("/" + f))]
        errs = [resolve(i, kinds) for i in ids]  # F1: None is a record that resolves
        if None in errs:
            continue
        msg = errs[0] if ids else "%s needs `ratchet-raise: %s %s -- <W-n | D-n>`" % (what, os.path.basename(rel), key)
        out(finding("%s::%s" % (rel, key), msg))
        code = 1
    return code


def files_of(root, patterns):
    """The ONE file-set reader: files under root matching the globs, '/'-separated, sorted, never __pycache__ (t-1991 Q6)."""
    found = set()
    for pat in patterns:
        for rel in glob.glob(pat, root_dir=root, recursive=True, include_hidden=True):
            rel = rel.replace("\\", "/")
            if os.path.isfile(os.path.join(root, rel)) and "__pycache__" not in rel.split("/"):
                found.add(rel)
    return sorted(found)


def raw_of(root, rel):
    with open(os.path.join(root, rel), "rb") as fh:
        return fh.read()


def utf8_of(root, rel):
    """The strict UTF-8 text reader: bytes that are not UTF-8 raise UnicodeDecodeError, a ValueError, so in BAD (universality
    reads through parse_all with it: a broken file is a red finding, exit 1, t-1998 F2)."""
    return raw_of(root, rel).decode("utf-8")


def text_file(root, rel):
    """utf8_of for an aggregate (size): a file that is not UTF-8 is exit 2 naming it, since a sum over files has no per-file
    finding to print (t-1998 Q3). Python source is read by read_source, the other kind."""
    try:
        return utf8_of(root, rel)
    except UnicodeDecodeError:
        raise Refuse("%s: not UTF-8" % rel)


def read_source(root, rel):
    """The ONE Python source reader (crap, lint, clone): bytes decoded by the PEP 263 coding line or BOM; a file that cannot be
    decoded raises, and the caller reports it as broken, never clean."""
    raw = raw_of(root, rel)
    return raw.decode(tokenize.detect_encoding(io.BytesIO(raw).readline)[0])


def describe(exc):
    if isinstance(exc, OSError):  # str() of an OSError holds an absolute path
        return "%s: %s" % (type(exc).__name__, (exc.strerror or "cannot be read")[:200])
    lines = str(exc).splitlines()
    return "%s: %s" % (type(exc).__name__, lines[0][:200]) if lines else type(exc).__name__


def tree_of(build):
    """parse_all's per-file function for a tool that reads the tree (crap, clone): build(rel, the parsed source)."""
    return lambda rel, source: build(rel, ast.parse(source, filename=rel))


def parse_all(root, files, each, read=read_source):
    """([each(rel, read(root, rel)) per file], [(rel, why)], files read): a file that cannot be read, or that each() raises
    on, is broken, never clean; a file whose bytes could not be read at all (an OSError) is not counted as read (N2, the
    Lead's ruling (1)). The one per-file loop of the four list tools, so that rule is written once (t-1997 X6, t-1998 F2:
    universality passes read=utf8_of)."""
    done, broken, unread = [], [], 0
    for rel in files:
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                done.append(each(rel, read(root, rel)))
        except BAD as exc:
            broken.append((rel, describe(exc)))
            unread += isinstance(exc, OSError)
    return done, broken, len(files) - unread


def is_python(root, rel):
    """A `*.py`, or an extensionless file whose first line is a python shebang (a git hook). Anything else is out."""
    name = rel.rsplit("/", 1)[-1]
    if "." in name:
        return name.endswith(".py")
    try:
        with open(os.path.join(root, rel), "rb") as fh:
            first = fh.readline(512)
    except OSError:
        return True  # unreadable: it is reported as a file that cannot be parsed, never skipped
    return first.startswith(b"#!") and b"python" in first


def is_test(rel):
    parts = rel.split("/")
    return "tests" in parts or (parts[-1].startswith("test_") and parts[-1].endswith(".py"))


def globs(roots):
    return ["%s/**" % r for r in roots]


def scope(root, roots, tests=False):
    """The Python files of the roots (an absent root is empty), `/`-separated, sorted. F256: test files are in for lint only."""
    return [r for r in files_of(root, globs(roots)) if is_python(root, r) and (tests or not is_test(r))]


def load_list(path, what, ident, field="allow", must_exist=False):
    """(data, rows) of a list file keyed by ident(row), which raises on a row without its id/file. No file is an empty list
    (unless must_exist): data {"basis": None, field: []}, which check_basis passes and update never writes (t-1992 N2: node
    B's baselines start absent). Not JSON, no basis, a malformed or duplicate row is exit 2; a reasonless row is judge_list's."""
    if not os.path.isfile(path) and not must_exist:
        return {"basis": None, field: []}, []
    data = read_json(path, what)
    rows = data.get(field) if isinstance(data, dict) else None
    if not isinstance(rows, list):
        raise Refuse("%s: must be one JSON object with a list %s" % (what, field))
    if not isinstance(data.get("basis"), dict):
        raise Refuse("%s: basis missing" % what)
    seen = set()
    for row in rows:
        key = row_key(ident, row, "%s: a %s row" % (what, field))
        if key in seen:
            raise Refuse("%s: duplicate %s row %s" % (what, field, key))
        seen.add(key)
    return data, rows


def row_key(ident, row, what):
    try:
        return ident(row)
    except (KeyError, TypeError, AttributeError, ValueError):
        raise Refuse("%s needs its id or file" % what)


def check_basis(old, now, door):
    """None when the basis matches or the file is not born yet (old None: no drift); the file's Python minor when only that
    differs (exit 3); a Refuse for any other drift."""
    if old is None:
        return None
    for key in now:
        if key not in old:
            raise Refuse("basis %s missing; %s" % (key, door))
        if key != "python" and old[key] != now[key]:
            raise Refuse("basis %s %s -> %s; %s" % (key, old[key], now[key], door))
    return None if old.get("python") == now.get("python") else old["python"]


def basis_changed(old, new):
    """N13's `basis` key: any basis key but python differs between the base and HEAD (constants, roots, tool; an added root
    too; a base with no basis object differs). A label cannot be ordered, so every change errs red as size's unit and paths
    do (t-1994 F1: a changed match constant passed unseen)."""
    strip = lambda b: {k: v for k, v in b.items() if k != "python"} if isinstance(b, dict) else b
    return strip(old) != strip(new)


def judge_list(sites, rows, key, files_read, scope_files, out=print):
    """sites: [(identity, detail)], rows keyed by key(row). Returns (sites no row allows, stale keys, keys of rows without a
    reason). A dead scanner (no site while rows exist; no file read while the scope holds files) is judged before stale."""
    if rows and not sites:
        raise Refuse("scanner found nothing (%d rows)" % len(rows))
    if scope_files and not files_read:
        raise Refuse("scanner read none of the %d files in scope" % scope_files)
    keys = {key(r) for r in rows}
    stale = sorted(keys - {identity for identity, _ in sites})
    bare = [key(r) for r in rows if not str(r.get("reason", "")).strip()]
    for k in stale:
        out("stale: %s" % label(k))
    for k in bare:
        out(finding(label(k), "row has no reason"))
    return [s for s in sites if s[0] not in keys], stale, bare


def cleared(old_rows, new_rows):
    """N13's `clear` key: rows at the base, none at HEAD. An empty list switches off judge_list's first dead-scanner branch
    (N16), so emptying is a raise however it was done (t-1992 N4: by hand it passed unseen)."""
    return bool(old_rows) and not new_rows


def _shrink(path, data, field, key, stale, out=print):
    """update's helper, never a gate (t-1994 F3): drop the stale rows and write the file: True. No stale row: nothing
    written, False (a file not born stays unborn)."""
    keep = [r for r in data[field] if key(r) not in stale]
    if len(keep) == len(data[field]):
        return False
    data[field] = keep
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(data, indent=2) + "\n")
    out("updated: %d stale %s rows removed" % (len(stale), field))
    return True


def update(root, path, data, field, key, stale, record, kinds, scope, out=print):
    """The ONE --update / --record road of every list tool (F246, t-1992 N3): 0 done, 1 refused with nothing written.
    A record must resolve to one of kinds; only a resolved record may empty the list (N16); then _shrink, then a warning
    about uncommitted paths in scope, since the list describes the committed tree (N15). scope takes the globs files_of
    takes (each sent to git as `:(glob)`, t-1994 F2: plain pathspecs read `**` and `*` otherwise); an empty scope warns
    about the whole tree."""
    if record:
        err = resolve(record, kinds)
        if err:
            out(err)
            return 1
    if not record and cleared(data[field], [r for r in data[field] if key(r) not in stale]):
        out("refused: --update would empty %s; door: --record <W-n | D-n> and a `ratchet-raise: %s clear -- <id>` line"
            % (field, os.path.basename(path)))
        return 1
    _shrink(path, data, field, key, stale, out)
    specs = [":(glob)" + s for s in scope]
    dirty = [ln for ln in text_of(git(root, "status", "--porcelain", "--", *specs)).split("\n") if ln.strip()]
    if dirty:
        out("uncommitted changes in scope: %d paths -- the list describes the committed tree" % len(dirty))
    return 0


# ---- the driver of the four list tools (F246 (a): one copy; t-1996 B1)

def ident(row):
    rid = row["id"]
    if not isinstance(rid, str) or not rid.strip():
        raise ValueError("an id is a non-empty string")
    if re.search(r"\s", rid):  # t-1997 X5: a site is encoded, so such a row would print stale and new with one identity
        raise Refuse("row id %s holds whitespace (N23: an identity is one token, whitespace written %%20)" % json.dumps(rid))
    return rid


class Spec:
    """A list tool's constants: rel (its list file), key(row), field (the rows' name), scope (globs for --update's warning),
    labels (the `row added` and `emptied` raise texts), extra(old, data) -> {key: text} (a tool's own raise keys), validate(data)
    (a Refuse for a malformed non-list part), must_exist (a list file that is never born absent), listing (the tool takes
    --list; False: the flag is not registered, so it is a usage error, t-1997 X3)."""

    def __init__(self, rel, key=ident, field="rows", scope=(), labels=("baseline row added", "list emptied"), extra=None,
                 validate=None, must_exist=False, listing=True):
        self.rel, self.key, self.field, self.scope, self.labels = rel, key, field, scope, labels
        self.extra, self.validate, self.must_exist, self.listing = extra, validate, must_exist, listing


class Scan:
    """What a tool measured. sites [(identity, detail)]; broken [(path, why)] (red, no row allows it, --update refused); red
    [(identity, detail)] (red, no row allows it); files in scope and files read -- two counts, N2 (a file read but
    not parsed is read; one that raised OSError is not); lines for --list (None:
    the sites); code 0 or 3 (a part not judged); skip: row keys not judged; notes {row id: text added to its stale line};
    green: lines printed with no verdict."""

    def __init__(self, sites, broken, files, read, lines=None, code=0, skip=(), notes=None, green=(), red=()):
        self.sites, self.broken, self.files, self.read, self.code = sites, broken, files, read, code
        self.lines = lines if lines is not None else ["%s %s" % s for s in sites]
        self.skip, self.notes, self.green, self.red = set(skip), notes or {}, list(green), list(red)


def door(rel):
    """The basis door text, built from the list file's name (the same for every list tool)."""
    return ("door: edit basis in %s; a basis change also needs `ratchet-raise: %s basis -- <W-n | D-n>`"
            "; --update does not touch basis" % (rel, os.path.basename(rel)))


def raised(old, data, spec):
    """N13's raise keys against the base: a row added, the list emptied (`clear`), a basis change (`basis`), a tool's own
    (spec.extra): each `word | decision`. A base that is no well-formed list file is a Refuse."""
    f, key = spec.field, spec.key
    try:
        seen = {key(r) for r in old[f]}
    except (KeyError, TypeError, AttributeError, ValueError):
        raise Refuse("%s at the base: must be one JSON object with well-formed %s rows" % (spec.rel, f))
    keys = {label(key(r)): spec.labels[0] for r in data[f] if key(r) not in seen}
    if cleared(old[f], data[f]):
        keys["clear"] = spec.labels[1]
    if basis_changed(old.get("basis"), data["basis"]):
        keys["basis"] = "basis changed"
    keys.update(spec.extra(old, data) if spec.extra else {})
    return {k: (what, RECORD) for k, what in keys.items()}


def stale_out(notes):
    def out(line):
        print(line + notes.get(line[len("stale: "):], "") if line.startswith("stale: ") else line)
    return out


def conclude(mod, a, held, scan):
    spec, (path, data, base) = mod.SPEC, held
    if a.list and scan.lines:
        print("\n".join(sorted(scan.lines)))
    for where, why in scan.broken:
        print(finding(where, "cannot parse: " + why))
    for identity, detail in scan.red:
        print(finding(identity, detail))
    live = [r for r in data[spec.field] if spec.key(r) not in scan.skip]
    new, stale, bare = judge_list(scan.sites, live, spec.key, scan.read, scan.files, stale_out(scan.notes))
    for identity, detail in new:
        print(finding(label(identity), detail))
    for line in scan.green:
        print(line)
    red = 1 if (new or bare or scan.broken or scan.red) else 0
    if a.update:
        if scan.broken:
            print("refused: --update while a file cannot be parsed (fix it first)")
            return 1
        code = update(a.root, path, data, spec.field, spec.key, set(stale), a.record, RECORD, spec.scope, print)
        return verdict([code, red, scan.code])
    old = base_doc(a.root, base, spec.rel, print)
    code = judge_raises(a.root, base, spec.rel, raised(old, data, spec), print) if old is not None else 0
    return verdict([1 if (red or stale) else 0, code, scan.code])


def judge(mod, a):
    spec = mod.SPEC
    path = os.path.join(a.root, spec.rel)
    data, _ = load_list(path, spec.rel, spec.key, spec.field, spec.must_exist)
    if spec.validate:
        spec.validate(data)
    base = base_of(a.root, a.base)
    drift = check_basis(data["basis"], mod.basis(), door(spec.rel))  # a non-python drift raises: the list file is refused
    # The Lead's rulings (2) and Q2, t-1997 X1, t-1998 F1: after every refused input (a list, base or non-python basis, 2,
    # beats 1), before the python-minor drift and the scan (1 beats 3; a dead scanner must not hide that no record resolves
    # yet, L11).
    if a.update and a.record:
        err = resolve(a.record, RECORD)
        if err:
            print(err)
            return 1
    if drift:
        print("not judged here: python %s, basis %s" % (python_minor(), drift))
        return 3
    return conclude(mod, a, (path, data, base), mod.scan(a.root, a, data))


def drive(mod, argv):
    ap = parser(mod.__doc__.split("\n")[0])
    for flag in ("--update", "--basis") + (("--list",) if mod.SPEC.listing else ()):
        ap.add_argument(flag, action="store_true")
    ap.set_defaults(list=False)
    ap.add_argument("--record")
    getattr(mod, "add_options", lambda p: None)(ap)
    a = ap.parse_args(argv)
    getattr(mod, "check_args", lambda x: None)(a)
    if a.basis:
        print(json.dumps(mod.basis()))
        return 0
    return judge(mod, a)


def entry(mod, argv):
    """A list tool's main: Refuse is exit 2 (guarded); any other exception is exit 2 too, never a traceback exit 1."""
    try:
        return guarded(drive, mod, argv)
    except Exception as exc:
        print("cannot judge: %s" % describe(exc))  # t-1997 X4: describe keeps an OSError's absolute path out
        return 2
