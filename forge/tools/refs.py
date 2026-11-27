# card: B13
"""References by key (B13; amended by B15, B16, B20): `check` reads the scanned rule texts for keys that must resolve exactly
once (card ids, `plan <h>` keys, `L-<n>`), line references that must not exist, the card line of every code file, AGENTS.md
as pointers only (B16 class 4) and the backticked paths of the rule files (B20 class 5). `cards` prints the cards no code file
names yet, never red. `legacy <file> --base <ref>` prints the `refs.json` legacy row of an edited spec copy.
Exit: 0 green, 1 red, 2 cannot judge (refs.json, SOURCES.md, plan copy, a file's encoding, no card headings, work list).
Importable: line_ref_tokens(text) (B11's add/repeat/set refuse a line reference by this one pattern), card_headings(root),
cards_not_built(root) (B15's `late`)."""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import words  # noqa: E402  B3's plan resolver: the one resolver of plan keys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULT_ALIASES = ("plan", "spec", "part2", "part2b", "part3", "part3b", "part4", "part4b", "audit", "v1.10")
NUM = r"\d+(?:-\d+)?(?:,\d+)*"
URL = re.compile(r"[A-Za-z][\w+.-]*://[^\s)>\]`]*")  # a scheme URL carries a port, not a line
FILE_REF = re.compile(r"(?<![\w./\\-])[\w./\\-]*?[\w-]\.[A-Za-z]\w*:" + NUM + r"(?!\w)")
CARD_WORD = re.compile(r"(?<![\w./\\:-])(C\d-\d+|[AB]\d+)(?!\w|-\d|\.\w)")
PLAN_KEY = re.compile(r"(?<![\w.-])plan (\d+[^\W\d_]?(?:\.\d+)?)(?![\w:]|\.\d)")
LIST_ID = re.compile(r"(?<![\w-])L-(\d+)(?![\w-])")
HEADING = re.compile(r"^### (C\d-\d+|[AB]\d+) ")
# the ids may be followed by a remark: ci.yml (`C1-6 (amended by B8). ...`) and older files already end the line that way
CARD_LINE = re.compile(r"card:\s*((?:C\d-\d+|[AB]\d+)(?:\s*,\s*(?:C\d-\d+|[AB]\d+))*)(?:\s*$|\s*[(;.:]|\s+--)")
POINTER = re.compile(r"^- `[^`]+`(: .*)?$")
CODE_DIRS = ("forge/tools/", "forge/hooks/", "forge/mods/", "measure/tools/", "factory/tools/", "factory/hooks/")
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv"}


class Cannot(Exception):
    """A verdict cannot be given: exit 2, never green."""


def line_ref_tokens(text, aliases=DEFAULT_ALIASES):
    """[(line number, token)] of line references: `<alias>:<n>` and `<name>.<ext>:<n>` (with -n and ,n); scheme URLs skipped."""
    alias = re.compile(r"(?<![\w.:/\\-])(?:%s):%s(?!\w)" % ("|".join(re.escape(a) for a in aliases), NUM))
    out = []
    for n, line in enumerate(text.split("\n"), 1):
        line = URL.sub(lambda m: " " * len(m.group(0)), line)
        out += [(n, m.group(0)) for rx in (alias, FILE_REF) for m in rx.finditer(line)]
    return out


def glob_re(pat):
    out, i = "", 0
    while i < len(pat):
        if pat.startswith("**/", i):
            out, i = out + "(?:.*/)?", i + 3
        elif pat[i] == "*":
            out, i = out + "[^/]*", i + 1
        else:
            out, i = out + re.escape(pat[i]), i + 1
    return re.compile(out + r"\Z")


def matches(pat, rel):
    return bool(glob_re(pat).match(rel))


def norm(p):
    return p.replace("\\", "/")


def tracked(root):
    if os.path.exists(os.path.join(root, ".git")):
        r = subprocess.run(["git", "-C", root, "ls-files", "-z"], capture_output=True)
        if r.returncode == 0:
            return sorted(x for x in r.stdout.decode("utf-8", "replace").split("\0") if x
                          and os.path.isfile(os.path.join(root, x)))
    out = []
    for d, dirs, names in os.walk(root):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
        out += [norm(os.path.relpath(os.path.join(d, n), root)) for n in names]
    return sorted(out)


def read_bytes(root, rel):
    with open(os.path.join(root, rel), "rb") as fh:
        return fh.read()


def decode(rel, raw):
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        raise Cannot("%s: not UTF-8, an unread file is never clean" % rel)


def load_cfg(root):
    path = os.path.join(root, "forge", "refs.json")
    try:
        with open(path, encoding="utf-8") as fh:
            cfg = json.load(fh)
    except (OSError, ValueError) as e:
        raise Cannot("forge/refs.json absent or malformed: %s" % e)
    if not isinstance(cfg, dict):
        raise Cannot("forge/refs.json malformed: not an object")
    for k, default in (("scan", []), ("code_kinds", []), ("line_ref_aliases", list(DEFAULT_ALIASES)), ("line_ok", []),
                       ("allow", []), ("legacy", []), ("local_roots", []), ("path_scan", []), ("path_suffixes", [])):
        cfg.setdefault(k, default)
    return cfg


def card_headings(root, rels=None):
    """{card id: [spec files holding its `### <id> ` heading]} across forge/specs/*.md."""
    out = {}
    for rel in rels if rels is not None else tracked(root):
        if re.fullmatch(r"forge/specs/[^/]+\.md", rel):
            for line in decode(rel, read_bytes(root, rel)).split("\n"):
                m = HEADING.match(line)
                if m:
                    out.setdefault(m.group(1), []).append(rel)
    return out


def parse_sources(root, rels):
    """{repo-relative copy: recorded sha256} from every SOURCES.md table; a table that does not parse -> Cannot."""
    out = {}
    for src in [r for r in rels if r.rsplit("/", 1)[-1] == "SOURCES.md"]:
        cols, rows = None, 0
        for line in decode(src, read_bytes(root, src)).split("\n"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.strip().startswith("|") else None
            if cells is None:
                cols = None
            elif cols is None:
                low = [c.lower() for c in cells]
                name = next((i for i, c in enumerate(low) if c in ("file", "path")), None)
                cols = (name, low.index("sha256")) if name is not None and "sha256" in low else ()
            elif cols and not set("".join(cells)) <= set("-: "):
                m = re.match(r"\S+", cells[cols[0]]) if len(cells) > max(cols) else None
                if not m or not re.fullmatch(r"[0-9a-f]{64}", cells[cols[1]]):
                    raise Cannot("%s: table row does not parse: %s" % (src, line.strip()[:80]))
                here = norm(os.path.normpath(os.path.join(os.path.dirname(src), m.group(0))))
                out[here if here in rels else norm(m.group(0))] = cells[cols[1]]
                rows += 1
        if not rows:
            raise Cannot("%s: no table of path and sha256 rows" % src)
    return out


def code_comment(cfg, rel):
    for row in cfg["code_kinds"]:
        if matches(row["glob"], rel):
            return row["comment"]
    return None


def card_ids_of(text, comment):
    """The ids of the card line within the first 3 lines, or None."""
    for line in text.split("\n")[:3]:
        s = line.strip()
        m = CARD_LINE.match(s[len(comment):].strip()) if s.startswith(comment) else None
        if m:
            return [x.strip() for x in m.group(1).split(",")]
    return None


def card_line_findings(rel, text, comment, heads):
    if not text.strip():
        return []  # an empty file is exempt
    ids = card_ids_of(text, comment)
    if ids is None:
        return ["%s: no `%s card: <id>` line in the first 3 lines" % (rel, comment)]
    return ["%s: card line names %s: %s" % (rel, i, "no heading" if i not in heads else "headings in " + ", ".join(heads[i]))
            for i in ids if len(heads.get(i, [])) != 1]


def list_ids(root):
    """L-<n> ids the work list holds, or None when B11 is not built or the list is absent; unreadable -> Cannot."""
    tool = os.path.join(root, "forge", "tools", "worklist.py")
    if not os.path.isfile(tool) or not os.path.isfile(os.path.join(root, "forge", "worklist.yaml")):
        return None
    r = subprocess.run([sys.executable, "-B", tool, "ids"], capture_output=True, cwd=root)
    if r.returncode != 0:
        raise Cannot("forge/worklist.yaml unreadable: worklist.py ids exit %d" % r.returncode)
    return set(re.findall(r"L-\d+", r.stdout.decode("utf-8", "replace")))


class Ctx:
    def __init__(self, root, cfg, heads):
        self.root, self.cfg, self.heads = root, cfg, heads
        self.used = set()  # indexes of allow rows that suppressed something
        self.ids = "unread"
        self.aliases = cfg["line_ref_aliases"]

    def allowed(self, rel, token):
        for i, row in enumerate(self.cfg["allow"]):
            if row.get("file") == rel and row.get("token") == token:
                self.used.add(i)
                return True
        return False

    def line_ok(self, token):
        name = norm(token.rsplit(":", 1)[0])
        return any(matches("**/" + row["glob"], name) for row in self.cfg["line_ok"])

    def list_has(self, n):
        if self.ids == "unread":
            self.ids = list_ids(self.root)
        return self.ids is not None and "L-%s" % n in self.ids


def key_findings(ctx, rel, text):
    """[(kind, token, line number, message)] of keys and line references in one scanned text; kind line|card|plan|list."""
    out = [("line", tok, n, "line reference " + tok) for n, tok in line_ref_tokens(text, ctx.aliases)]
    for n, line in enumerate(text.split("\n"), 1):
        line = URL.sub(" ", line)
        if HEADING.match(line):
            continue  # the heading itself is the target, not a citation
        for m in CARD_WORD.finditer(line):
            k = m.group(1)
            got = ctx.heads.get(k, [])
            if len(got) != 1:
                out.append(("card", k, n, "card id %s %s" % (k, "has no heading" if not got else "has headings in " + ", ".join(got))))
        for m in PLAN_KEY.finditer(line):
            ok = words.plan_key_ok(ctx.root, m.group(1))
            if ok is None:
                raise Cannot("plan copy absent: cannot judge `plan %s` in %s" % (m.group(1), rel))
            if not ok:
                out.append(("plan", m.group(0), n, "plan key `%s` does not resolve exactly once" % m.group(0)))
        for m in LIST_ID.finditer(line):
            if not ctx.list_has(m.group(1)):
                out.append(("list", m.group(0), n, "cannot resolve %s: %s" % (
                    m.group(0), "no work list" if ctx.ids is None else "not in the list")))
    return out


def legacy_kind(kind):
    return kind in ("line", "card")


def path_exists(p, rels):
    p = norm(p).rstrip("/")
    return p in rels or any(r.startswith(p + "/") for r in rels)


def agents_findings(ctx, rels):
    """B16 class 4: AGENTS.md is a heading and pointer lines only; every backticked path exists."""
    if "CLAUDE.md" not in rels:
        return [], ["AGENTS.md not judged: no CLAUDE.md (C1-1)"]
    if "AGENTS.md" not in rels:
        return ["AGENTS.md: absent (C1-1 landed, B16 class 4)"], []
    red = []
    for n, line in enumerate(decode("AGENTS.md", read_bytes(ctx.root, "AGENTS.md")).split("\n"), 1):
        if not line.strip() or line.startswith("#"):
            continue
        if not POINTER.match(line):
            red.append("AGENTS.md:%d: AGENTS.md holds text, not a pointer" % n)
            continue
        red += ["AGENTS.md:%d: pointer path does not exist: %s" % (n, p)
                for p in re.findall(r"`([^`]+)`", line) if not path_exists(p, rels)]
    return red, []


def path_findings(ctx, rel, text, rels):
    """B20 class 5: each word of a backticked token that looks like a path names a tracked path (or a basename)."""
    fold = (lambda s: s.lower()) if os.name == "nt" else (lambda s: s)
    tracked_set = {fold(r) for r in rels}
    bases = {fold(r.rsplit("/", 1)[-1]) for r in rels}
    roots = [fold(norm(ctx.root)).rstrip("/")] + [fold(norm(r)).rstrip("/") for r in ctx.cfg["local_roots"]]
    suffixes = tuple(ctx.cfg["path_suffixes"])
    red, notes = [], []
    for n, line in enumerate(text.split("\n"), 1):
        for tok in re.findall(r"`([^`\n]+)`", line):
            for w in tok.split():
                w = re.split(r"::|#", w)[0].rstrip(".,;:)")
                if not w or re.search(r"[<>*{]", w) or not ("/" in w or "\\" in w or w.endswith(suffixes)):
                    continue
                f = fold(norm(w))
                if re.match(r"[A-Za-z]:/|/|~", f):
                    top = next((r for r in roots if f.startswith(r + "/")), None)
                    if top is None:
                        notes.append("%s:%d: not judged: outside the repository: %s" % (rel, n, w))
                        continue
                    f = f[len(top) + 1:]
                if "/" in f:
                    f = f.rstrip("/")
                    ok = f in tracked_set or any(r.startswith(f + "/") for r in tracked_set)
                else:
                    ok = f in bases
                if not ok and not ctx.allowed(rel, w):
                    red.append("%s:%d: path does not name a tracked file: %s (door: write the path, or an allow row)" % (rel, n, w))
    return red, notes


def git_show(root, ref, rel):
    r = subprocess.run(["git", "-C", root, "show", "%s:%s" % (ref, rel)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def check_ref(root, ref):
    r = subprocess.run(["git", "-C", root, "rev-parse", "--verify", "--quiet", ref + "^{commit}"], capture_output=True)
    if r.returncode != 0:
        raise Cannot("base %s is not a commit" % ref)


def held_tokens(text, ctx):
    return {t for _, t in line_ref_tokens(text, ctx.aliases)} | {m.group(1) for m in CARD_WORD.finditer(text)}


def base_findings(ctx, base):
    """`check --base`: a legacy row only shrinks (AR-20)."""
    root, red = ctx.root, []
    check_ref(root, base)
    raw = git_show(root, base, "forge/refs.json")
    try:
        old = {r["file"]: set(r["tokens"]) for r in json.loads(raw.decode("utf-8")).get("legacy", [])} if raw else {}
    except (ValueError, KeyError, UnicodeDecodeError, AttributeError):
        raise Cannot("forge/refs.json at %s is malformed" % base)
    for row in ctx.cfg["legacy"]:
        f, toks = row["file"], set(row["tokens"])
        if f in old:
            red += ["%s: legacy row gains token %s against %s" % (f, t, base) for t in sorted(toks - old[f])]
        else:
            raw = git_show(root, base, f)
            held = held_tokens(decode(f, raw), ctx) if raw is not None else set()
            red += ["%s: new legacy row lists %s, which the bytes at %s do not hold" % (f, t, base) for t in sorted(toks - held)]
    return red


def check(root, base=None):
    cfg = load_cfg(root)
    rels = tracked(root)
    heads = card_headings(root, rels)
    if not heads:
        raise Cannot("forge/specs/ holds no card heading: never green on no data")
    status = {}
    for rel, sha in parse_sources(root, rels).items():
        if rel in rels:
            status[rel] = "frozen" if hashlib.sha256(read_bytes(root, rel)).hexdigest() == sha else "edited"
    ctx = Ctx(root, cfg, heads)
    legacy = {r["file"]: set(r["tokens"]) for r in cfg["legacy"]}
    red, notes, seen = [], [], {}
    for rel in [r for r in rels if any(matches(row["glob"], r) for row in cfg["scan"]) and status.get(r) != "frozen"]:
        edited = status.get(rel) == "edited"
        found = key_findings(ctx, rel, decode(rel, read_bytes(root, rel)))
        if edited:
            seen[rel] = {f[1] for f in found if legacy_kind(f[0])}
            if seen[rel] and rel not in legacy:
                red.append("%s: copy edited and no legacy row; run: python -B forge/tools/refs.py legacy %s --base <ref>" % (rel, rel))
                continue
        for kind, tok, n, msg in found:
            if ctx.allowed(rel, tok) or (kind == "line" and ctx.line_ok(tok)):
                continue
            if edited and legacy_kind(kind) and tok in legacy.get(rel, ()):
                continue
            pre = "new " if edited and kind == "line" else "unresolved id: " if edited and kind == "card" else ""
            red.append("%s:%d: %s%s" % (rel, n, pre, msg))
    for rel in rels:
        comment = code_comment(cfg, rel)
        if comment and status.get(rel) != "frozen":
            red += card_line_findings(rel, decode(rel, read_bytes(root, rel)), comment, heads)
    a_red, a_notes = agents_findings(ctx, rels)
    red, notes = red + a_red, notes + a_notes
    for rel in [r for r in rels if any(matches(g, r) for g in cfg["path_scan"])]:
        p_red, p_notes = path_findings(ctx, rel, decode(rel, read_bytes(root, rel)), rels)
        red, notes = red + p_red, notes + p_notes
    for i, row in enumerate(cfg["allow"]):
        if not str(row.get("reason", "")).strip():
            red.append("refs.json allow row %d (%s %s): no reason" % (i, row.get("file"), row.get("token")))
        if i not in ctx.used:
            red.append("refs.json allow row %d (%s %s) is stale: it suppresses nothing" % (i, row.get("file"), row.get("token")))
    for rel, toks in legacy.items():
        if status.get(rel) != "edited":
            red.append("refs.json legacy row %s is stale: the file is not an edited copy" % rel)
        else:
            red += ["refs.json legacy row %s: token %s is stale, drop it" % (rel, t) for t in sorted(toks - seen.get(rel, set()))]
    if base:
        red += base_findings(ctx, base)
    else:
        notes.append("legacy rows not judged against a base")
    return red, notes


def spec_owns(root, rels):
    """{card id: [owned paths]} from each card's `- owns:` line."""
    out = {}
    for rel in [r for r in rels if re.fullmatch(r"forge/specs/[^/]+\.md", r)]:
        cur = None
        for line in decode(rel, read_bytes(root, rel)).split("\n"):
            m = HEADING.match(line)
            if m:
                cur = m.group(1)
            elif line.startswith("#"):
                cur = None
            elif cur and line.startswith("- owns:"):
                paths = [norm(p.strip("`;.")) for p in re.split(r"[,\s]+", line[7:]) if "/" in p or "." in p]
                out.setdefault(cur, []).extend(re.sub(r"^[A-Za-z]:/QAFactory/forge2-repo/", "", p) for p in paths)
    return out


def cards_not_built(root, cfg=None):
    """B15's `late`: card ids whose owns name a code-kind path or a tools/hooks folder and that no code file names."""
    cfg = cfg or load_cfg(root)
    rels = tracked(root)
    named = set()
    for rel in rels:
        comment = code_comment(cfg, rel)
        if comment:
            named |= set(card_ids_of(decode(rel, read_bytes(root, rel)), comment) or ())
    code = lambda p: code_comment(cfg, p) or p.startswith(CODE_DIRS)
    return sorted((c for c, ps in spec_owns(root, rels).items() if c not in named and any(code(p) for p in ps)),
                  key=lambda c: [int(x) for x in re.findall(r"\d+", c)])


def legacy_row(root, rel, base):
    cfg = load_cfg(root)
    check_ref(root, base)
    raw = git_show(root, base, rel)
    if raw is None:
        raise Cannot("%s absent at %s" % (rel, base))
    ctx = Ctx(root, cfg, card_headings(root, tracked(root)))
    return {"file": rel, "tokens": sorted({f[1] for f in key_findings(ctx, rel, decode(rel, raw)) if legacy_kind(f[0])})}


def main(argv=None):
    ap = argparse.ArgumentParser(prog="refs.py")
    ap.add_argument("--root", default=ROOT)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check").add_argument("--base")
    sub.add_parser("cards")
    lg = sub.add_parser("legacy")
    lg.add_argument("file")
    lg.add_argument("--base", required=True)
    a = ap.parse_args(argv)
    root = os.path.abspath(a.root)
    try:
        if a.cmd == "cards":
            ids = cards_not_built(root)
            print("not built: " + (", ".join(ids) if ids else "none"))
            return 0
        if a.cmd == "legacy":
            print(json.dumps(legacy_row(root, norm(a.file), a.base), ensure_ascii=False))
            return 0
        red, notes = check(root, a.base)
    except Cannot as e:
        print("cannot judge: %s" % e)
        return 2
    for line in notes + red:
        print(line)
    print("refs: %s" % ("red, %d findings" % len(red) if red else "green"))
    return 1 if red else 0


if __name__ == "__main__":
    sys.exit(main())
