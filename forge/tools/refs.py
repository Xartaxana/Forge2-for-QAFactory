# card: B13
"""References by key (B13; amended by B15, B16, B20): `check` reads the scanned rule texts for keys that must resolve exactly
once (card ids, `plan <h>` keys, `L-<n>`), line references that must not exist, the card line of every code file, AGENTS.md
as pointers only (B16 class 4) and the backticked paths of the rule files (B20 class 5). `cards` prints the cards no code file
names yet, never red. `legacy <file> --base <ref>` prints the `refs.json` legacy row of an edited spec copy.
The base of `check` is read as every base job reads it: --base, else FORGE_BASE (ci.py), through ratchets.base_of.
Exit: 0 green, 1 red, 2 cannot judge (refs.json, SOURCES.md, plan copy, a file's encoding, no card headings, work list, a
dead scanner).
Importable: line_ref_tokens(text) (B11's add/repeat/set refuse a line reference by this one pattern), card_headings,
card_states(root) -> (not built, not judged) and cards_not_built(root) (B15's `late`)."""
import argparse
import fnmatch
import hashlib
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ratchets  # noqa: E402  B20's one allow-list judge, one refusal, one file reader, one base reader
import words  # noqa: E402  B3's plan resolver: the one resolver of plan keys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
Cannot = ratchets.Refuse  # a verdict cannot be given: exit 2, never green
NUM = r"\d+(?:-\d+)?(?:,\d+)*"
URL = re.compile(r"[A-Za-z][\w+.-]*://[^\s)>\]`]*")  # a scheme URL carries a port, not a line
FILE_REF = re.compile(r"(?<![\w./\\-])[\w./\\-]*?[\w-]\.[A-Za-z]\w*:" + NUM + r"(?!\w)")
PLAN_KEY = re.compile(r"(?<![\w.-])plan (\d+[^\W\d_]?(?:\.\d+)?)(?![\w:]|\.\d)")
LIST_ID = re.compile(r"(?<![\w-])L-(\d+)(?![\w-])")
OWNS = re.compile(r"^- owns\b[^:]*:(.*)")  # `- owns:` and `- owns (inside accepted cards):` (t-2104 F5)
POINTER = re.compile(r"^- `[^`]+`(: .*)?$")
CODE_DIRS = ("forge/tools/", "forge/hooks/", "forge/mods/", "measure/tools/", "factory/tools/", "factory/hooks/")
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv"}
SPEC_FILE = re.compile(r"forge/specs/[^/]+\.md")


class Forms:
    """The card id form, read from the `card_id` row of refs.json (`A<n> | B<n> | C<d>-<n>`): one source for the heading, the
    word and the card line (t-2104 F6: the form had been hard-coded three times, the row never read)."""

    def __init__(self, row):
        alts = [a.strip() for a in str(row or "").split("|")]
        if not all(re.fullmatch(r"(?:[A-Za-z]|<n>|<d>|-)+", a) and "<" in a for a in alts):
            raise Cannot("forge/refs.json card_id: not alternatives of `X<n>` / `X<d>-<n>`: %r" % (row,))
        one = "|".join(a.replace("<n>", r"\d+").replace("<d>", r"\d") for a in alts)
        self.heading = re.compile(r"^### (%s) " % one)
        self.word = re.compile(r"(?<![\w./\\:-])(%s)(?!\w|-\d|\.\w)" % one)
        # the ids may be followed by a remark: ci.yml (`C1-6 (amended by B8). ...`) and older files already end the line that way
        self.line = re.compile(r"card:\s*((?:%s)(?:\s*,\s*(?:%s))*)(?:\s*$|\s*[(;.:]|\s+--)" % (one, one))


def glob_match(glob, rel):
    """A glob against a path that may not exist yet (an owns path, a cited name): fnmatch, under any folder."""
    g = glob[3:] if glob.startswith("**/") else glob
    return fnmatch.fnmatchcase(rel, g) or fnmatch.fnmatchcase(rel, "*/" + g)


def spec_aliases(root):
    """Aliases of the spec files that exist, read from forge/specs/ (t-2104 F3): `plan`, `spec`, `part4b-2` for each file
    `...-plan.md`, `...-spec.md`, `...-spec-part4b-2.md`."""
    out = set()
    folder = os.path.join(root, "forge", "specs")
    for name in os.listdir(folder) if os.path.isdir(folder) else ():
        m = re.search(r"-(plan|spec)\.md$", name) or re.search(r"-spec-(part[\w-]+)\.md$", name)
        if m:
            out.add(m.group(1))
    return out


def all_aliases(root, cfg):
    return sorted(spec_aliases(root) | set(cfg["line_ref_aliases"]), key=lambda a: (-len(a), a))


def line_ref_tokens(text, aliases=None):
    """[(line number, token)] of line references: `<alias>:<n>` and `<name>.<ext>:<n>` (with -n and ,n); scheme URLs skipped.
    No aliases given: those of this repository (spec files present plus refs.json line_ref_aliases)."""
    aliases = aliases if aliases is not None else all_aliases(ROOT, load_cfg(ROOT))
    alias = re.compile(r"(?<![\w.:/\\-])(?:%s):%s(?!\w)" % ("|".join(re.escape(a) for a in aliases), NUM))
    out = []
    for n, line in enumerate(text.split("\n"), 1):
        line = URL.sub(lambda m: " " * len(m.group(0)), line)
        out += [(n, m.group(0)) for rx in (alias, FILE_REF) for m in rx.finditer(line)]
    return out


def norm(p):
    return p.replace("\\", "/")


def tracked(root):
    """B20 wants TRACKED files (git ls-files), which ratchets.files_of (a disk glob) is not; the walk is the no-git fallback."""
    if os.path.exists(os.path.join(root, ".git")):
        r = ratchets.git(root, "ls-files", "-z")
        if r.returncode == 0:
            return sorted(x for x in ratchets.text_of(r).split("\0") if x and os.path.isfile(os.path.join(root, x)))
    out = []
    for d, dirs, names in os.walk(root):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
        out += [norm(os.path.relpath(os.path.join(d, n), root)) for n in names]
    return sorted(out)


def matching(root, rels, patterns):
    """The tracked files among the files_of(patterns) disk glob."""
    return sorted(set(ratchets.files_of(root, patterns)) & set(rels))


def strict(rel, raw):
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        raise Cannot("%s: not UTF-8, an unread file is never clean" % rel)


def allow_key(row):
    return (row["file"], row["token"])


def load_cfg(root):
    cfg = ratchets.read_json(os.path.join(root, "forge", "refs.json"), "forge/refs.json")
    if not isinstance(cfg, dict):
        raise Cannot("forge/refs.json malformed: not an object")
    for k, default in (("scan", []), ("code_kinds", []), ("line_ref_aliases", []), ("line_ok", []),
                       ("allow", []), ("legacy", []), ("local_roots", []), ("path_scan", []), ("path_suffixes", [])):
        cfg.setdefault(k, default)
    if "card_id" not in cfg:
        raise Cannot("forge/refs.json: no card_id row")
    for row in cfg["allow"]:
        ratchets.row_key(allow_key, row, "forge/refs.json allow row")
    return cfg


def card_headings(root, rels, forms):
    """{card id: [spec files holding its `### <id> ` heading]} across forge/specs/*.md."""
    out = {}
    for rel in rels:
        if SPEC_FILE.fullmatch(rel):
            for line in ratchets.text_file(root, rel).split("\n"):
                m = forms.heading.match(line)
                if m:
                    out.setdefault(m.group(1), []).append(rel)
    return out


def header_cols(cells):
    low = [c.lower() for c in cells]
    name = next((i for i, c in enumerate(low) if c in ("file", "path")), None)
    return (name, low.index("sha256")) if name is not None and "sha256" in low else ()


def source_row(src, line, cells, cols):
    m = re.match(r"\S+", cells[cols[0]]) if len(cells) > max(cols) else None
    if not m or not re.fullmatch(r"[0-9a-f]{64}", cells[cols[1]]):
        raise Cannot("%s: table row does not parse: %s" % (src, line.strip()[:80]))
    return m.group(0), cells[cols[1]]


def table_rows(src, text):
    """[(path cell, sha256)] of the tables of one SOURCES.md; a row that does not parse, or no table -> Cannot."""
    cols, rows = None, []
    for line in text.split("\n"):
        if not line.strip().startswith("|"):
            cols = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cols is None:
            cols = header_cols(cells)
        elif cols and not set("".join(cells)) <= set("-: "):
            rows.append(source_row(src, line, cells, cols))
    if not rows:
        raise Cannot("%s: no table of path and sha256 rows" % src)
    return rows


def parse_sources(root, rels):
    """{repo-relative copy: recorded sha256} from every SOURCES.md table."""
    out = {}
    for src in [r for r in rels if r.rsplit("/", 1)[-1] == "SOURCES.md"]:
        for name, sha in table_rows(src, ratchets.text_file(root, src)):
            here = norm(os.path.normpath(os.path.join(os.path.dirname(src), name)))
            out[here if here in rels else norm(name)] = sha
    return out


def code_files(root, cfg, rels):
    """{tracked code file: its comment leader}; the first code_kinds row that matches wins."""
    out = {}
    for row in cfg["code_kinds"]:
        for rel in matching(root, rels, [row["glob"]]):
            out.setdefault(rel, row["comment"])
    return out


def card_ids_of(text, comment, forms):
    """The ids of the card line within the first 3 lines, or None."""
    for line in text.split("\n")[:3]:
        s = line.strip()
        m = forms.line.match(s[len(comment):].strip()) if s.startswith(comment) else None
        if m:
            return [x.strip() for x in m.group(1).split(",")]
    return None


def card_line_findings(rel, text, comment, heads, forms):
    """[(rel, token, kind, line, message)]; the token is what an allow row names: the id, or `card line` when none is named."""
    if not text.strip():
        return []  # an empty file is exempt
    ids = card_ids_of(text, comment, forms)
    if ids is None:
        loose = re.search(r"%s\s*card:\s*([^\s,;(]+)" % re.escape(comment), "\n".join(text.split("\n")[:3]))
        tok = loose.group(1) if loose else "card line"
        return [(rel, tok, "cardline", 0, "%s: no `%s card: <id>` line in the first 3 lines%s" % (
            rel, comment, " (it names %s)" % tok if loose else ""))]
    return [(rel, i, "cardline", 0, "%s: card line names %s: %s" % (
        rel, i, "no heading" if i not in heads else "headings in " + ", ".join(heads[i])))
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
    def __init__(self, root, cfg, heads, forms):
        self.root, self.cfg, self.heads, self.forms = root, cfg, heads, forms
        self.ids = "unread"
        self.aliases = all_aliases(root, cfg)

    def line_ok(self, token):
        name = norm(token.rsplit(":", 1)[0])
        return any(glob_match(row["glob"], name) for row in self.cfg["line_ok"])

    def list_has(self, n):
        if self.ids == "unread":
            self.ids = list_ids(self.root)
        return self.ids is not None and "L-%s" % n in self.ids


def key_findings(ctx, rel, text):
    """[(kind, token, line number, message)] of keys and line references in one scanned text; kind line|card|plan|list."""
    out = [("line", tok, n, "line reference " + tok) for n, tok in line_ref_tokens(text, ctx.aliases)]
    for n, line in enumerate(text.split("\n"), 1):
        line = URL.sub(" ", line)
        if ctx.forms.heading.match(line):
            continue  # the heading itself is the target, not a citation
        for m in ctx.forms.word.finditer(line):
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
    for n, line in enumerate(ratchets.text_file(ctx.root, "AGENTS.md").split("\n"), 1):
        if not line.strip() or line.startswith("#"):
            continue
        if not POINTER.match(line):
            red.append("AGENTS.md:%d: AGENTS.md holds text, not a pointer" % n)
            continue
        red += ["AGENTS.md:%d: pointer path does not exist: %s" % (n, p)
                for p in re.findall(r"`([^`]+)`", line) if not path_exists(p, rels)]
    return red, []


class PathJudge:
    """B20 class 5: one word of a backticked token that looks like a path names a tracked path (or a basename)."""

    def __init__(self, ctx, rels):
        self.fold = (lambda s: s.lower()) if os.name == "nt" else (lambda s: s)
        self.tracked = {self.fold(r) for r in rels}
        self.bases = {self.fold(r.rsplit("/", 1)[-1]) for r in rels}
        self.roots = [self.fold(norm(r)).rstrip("/") for r in [ctx.root] + list(ctx.cfg["local_roots"])]
        self.suffixes = tuple(ctx.cfg["path_suffixes"])

    def word(self, w):
        """None (fine or not a path), ("note", why) or ("red", why)."""
        f = self.fold(norm(w))
        if re.match(r"[A-Za-z]:/|/|~", f):
            top = next((r for r in self.roots if f.startswith(r + "/")), None)
            if top is None:
                return "note", "not judged: outside the repository: %s" % w
            f = f[len(top) + 1:]
        if "/" in f:
            f = f.rstrip("/")
            ok = f in self.tracked or any(r.startswith(f + "/") for r in self.tracked)
        else:
            ok = f in self.bases
        return None if ok else ("red", "path does not name a tracked file: %s (door: write the path, or an allow row)" % w)

    def path_like(self, w):
        return bool(w) and not re.search(r"[<>*{]", w) and ("/" in w or "\\" in w or w.endswith(self.suffixes))


def path_findings(judge, rel, text):
    """([(rel, word, kind, line, message)] red, [notes])."""
    red, notes = [], []
    for n, line in enumerate(text.split("\n"), 1):
        for tok in re.findall(r"`([^`\n]+)`", line):
            for w in [re.split(r"::|#", x)[0].rstrip(".,;:)") for x in tok.split()]:
                got = judge.word(w) if judge.path_like(w) else None
                if got and got[0] == "note":
                    notes.append("%s:%d: %s" % (rel, n, got[1]))
                elif got:
                    red.append((rel, w, "path", n, "%s:%d: %s" % (rel, n, got[1])))
    return red, notes


def at_base(root, base, rel):
    r = ratchets.git(root, "show", "%s:%s" % (base, rel))
    return r.stdout if r.returncode == 0 else None


def held_tokens(text, ctx):
    return {t for _, t in line_ref_tokens(text, ctx.aliases)} | {m.group(1) for m in ctx.forms.word.finditer(text)}


def base_findings(ctx, base, notes):
    """`check --base`: a legacy row only shrinks (AR-20)."""
    root, red = ctx.root, []
    doc = ratchets.base_doc(root, base, "forge/refs.json", notes.append)
    try:
        old = {r["file"]: set(r["tokens"]) for r in doc.get("legacy", [])} if doc else {}
    except (KeyError, TypeError, AttributeError):
        raise Cannot("forge/refs.json at %s is malformed" % base)
    for row in ctx.cfg["legacy"]:
        f, toks = row["file"], set(row["tokens"])
        if f in old:
            red += ["%s: legacy row gains token %s against %s" % (f, t, base) for t in sorted(toks - old[f])]
        else:
            raw = at_base(root, base, f)
            held = held_tokens(strict(f, raw), ctx) if raw is not None else set()
            red += ["%s: new legacy row lists %s, which the bytes at %s do not hold" % (f, t, base) for t in sorted(toks - held)]
    return red


def sources_status(root, rels):
    status = {}
    for rel, sha in parse_sources(root, rels).items():
        if rel in rels:
            status[rel] = "frozen" if hashlib.sha256(ratchets.raw_of(root, rel)).hexdigest() == sha else "edited"
    return status


def scan_findings(ctx, scan, status, legacy):
    """(found, seen, red): every finding of the scanned texts before any allow row; the old tokens of each edited copy; the
    edited copies that hold tokens and have no legacy row (red, with their door)."""
    found, seen, red = [], {}, []
    for rel in scan:
        hits = key_findings(ctx, rel, ratchets.text_file(ctx.root, rel))
        if status.get(rel) == "edited":
            seen[rel] = {h[1] for h in hits if legacy_kind(h[0])}
            if seen[rel] and rel not in legacy:
                red.append("%s: copy edited and no legacy row; run: python -B forge/tools/refs.py legacy %s --base <ref>" % (rel, rel))
                continue
        found += [(rel, tok, kind, n, msg) for kind, tok, n, msg in hits]
    return found, seen, red


def judged_reds(ctx, found, open_ids, status, legacy):
    """The messages of the findings no allow row, no line_ok target and no legacy token covers."""
    red = []
    for rel, tok, kind, n, msg in found:
        edited = status.get(rel) == "edited"
        if (rel, tok) not in open_ids or (kind == "line" and ctx.line_ok(tok)):
            continue
        if edited and legacy_kind(kind) and tok in legacy.get(rel, ()):
            continue
        pre = "new " if edited and kind == "line" else "unresolved id: " if edited and kind == "card" else ""
        red.append(msg if kind in ("path", "cardline") else "%s:%d: %s%s" % (rel, n, pre, msg))
    return red


def check(root, base=None):
    """base: a commit already resolved by ratchets.base_of (--base, else FORGE_BASE as ci.py passes it), or None."""
    cfg = load_cfg(root)
    forms = Forms(cfg["card_id"])
    rels = tracked(root)
    heads = card_headings(root, rels, forms)
    if not heads:
        raise Cannot("forge/specs/ holds no card heading: never green on no data")
    status = sources_status(root, rels)
    ctx = Ctx(root, cfg, heads, forms)
    legacy = {r["file"]: set(r["tokens"]) for r in cfg["legacy"]}
    scan = [r for r in matching(root, rels, [row["glob"] for row in cfg["scan"]]) if status.get(r) != "frozen"]
    found, seen, red = scan_findings(ctx, scan, status, legacy)
    for rel, comment in code_files(root, cfg, rels).items():
        if status.get(rel) != "frozen":
            found += card_line_findings(rel, ratchets.text_file(root, rel), comment, heads, forms)
    a_red, notes = agents_findings(ctx, rels)
    red += a_red
    judge = PathJudge(ctx, rels)
    for rel in matching(root, rels, cfg["path_scan"]):
        p_red, p_notes = path_findings(judge, rel, ratchets.text_file(root, rel))
        found, notes = found + p_red, notes + p_notes
    # B20: ONE rule for every allow list (ratchets.judge_list): a dead scanner is exit 2 before stale, then stale, then no reason
    msgs = []
    sites = [((r, t), m) for r, t, _k, _n, m in found]
    open_sites, _, _ = ratchets.judge_list(sites, cfg["allow"], allow_key, len(scan), len(scan), msgs.append)
    red += judged_reds(ctx, found, {s[0] for s in open_sites}, status, legacy)
    rows = [{"file": r["file"], "token": t, "reason": r.get("reason", "")} for r in cfg["legacy"] for t in r["tokens"]]
    old = [((r, t), "") for r in seen for t in seen[r]]
    ratchets.judge_list(old, rows, allow_key, len(seen), len(seen), msgs.append)
    red += msgs
    if base:
        red += base_findings(ctx, base, notes)
    else:
        notes.append("legacy rows not judged against a base")
    return red, notes


def strip_local(p, cfg):
    for lr in cfg["local_roots"]:
        top = norm(lr).rstrip("/") + "/"
        if p.startswith(top):
            return p[len(top):]
    return p


def spec_owns(root, rels, cfg):
    """{card id: [owned paths]} from each card's `- owns ...:` line (the `(inside accepted cards)` forms too)."""
    out, forms = {}, Forms(cfg["card_id"])
    for rel in [r for r in rels if SPEC_FILE.fullmatch(r)]:
        cur = None
        for line in ratchets.text_file(root, rel).split("\n"):
            m, own = forms.heading.match(line), OWNS.match(line)
            if m:
                cur = m.group(1)
            elif line.startswith("#"):
                cur = None
            elif cur and own:
                paths = [norm(p.strip("`;.")) for p in re.split(r"[,\s]+", own.group(1)) if "/" in p or "." in p]
                out.setdefault(cur, []).extend(strip_local(p, cfg) for p in paths)
    return out


def card_states(root, cfg=None):
    """B15's `late` input: (not built, not judged). Not built: a card whose owns name a code-kind path or a folder under
    CODE_DIRS and that no code file names. Not judged: every other card with a heading (no code owns: its state is unknown,
    never `built`, never `not built`)."""
    cfg = cfg or load_cfg(root)
    forms, rels = Forms(cfg["card_id"]), tracked(root)
    named = set()
    for rel, comment in code_files(root, cfg, rels).items():
        named |= set(card_ids_of(ratchets.text_file(root, rel), comment, forms) or ())
    kinds = [row["glob"] for row in cfg["code_kinds"]]
    code = lambda p: p.startswith(CODE_DIRS) or any(glob_match(g, p) for g in kinds)
    owners = {c for c, ps in spec_owns(root, rels, cfg).items() if any(code(p) for p in ps)}
    order = lambda c: [int(x) for x in re.findall(r"\d+", c)]
    return sorted(owners - named, key=order), sorted(set(card_headings(root, rels, forms)) - owners, key=order)


def cards_not_built(root, cfg=None):
    return card_states(root, cfg)[0]


def legacy_row(root, rel, base):
    cfg = load_cfg(root)
    raw = at_base(root, base, rel)
    if raw is None:
        raise Cannot("%s absent at %s" % (rel, base))
    forms = Forms(cfg["card_id"])
    ctx = Ctx(root, cfg, card_headings(root, tracked(root), forms), forms)
    return {"file": rel, "tokens": sorted({f[1] for f in key_findings(ctx, rel, strict(rel, raw)) if legacy_kind(f[0])})}


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
            print(json.dumps(legacy_row(root, norm(a.file), ratchets.base_of(root, a.base)), ensure_ascii=False))
            return 0
        red, notes = check(root, ratchets.base_of(root, a.base))
    except Cannot as e:
        print("cannot judge: %s" % e)
        return 2
    for line in notes + red:
        print(line)
    print("refs: %s" % ("red, %d findings" % len(red) if red else "green"))
    return 1 if red else 0


if __name__ == "__main__":
    sys.exit(main())
