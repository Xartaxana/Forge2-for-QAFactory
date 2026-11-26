# card: B22
"""Rule-cut gate: a range whose rule text loses a sentence or a carry id needs a commit line naming the cut (F19).

rule_cuts.py [--root D] [--base R]   exit 0 green, 1 an uncovered cut or gone id or an unrecorded config change, 2 cannot judge
The rule set: the globs of forge/rule-cuts.json `files` (per path segment), HEAD's globs on both committed trees. A text line
of the base set that the head set holds fewer times is removed; its sentence pieces are fragments. A fragment is kept when one
head sentence, or a window of two adjacent sentences of one block, holds `keep` of its IDF-weighted token share (tokens cut to
`prefix` characters) and every number of it; else it is a cut. An id on a `carry:` or `rows:` line of the base set and on no
such line of the head set is gone. Lines read from the messages of base..HEAD (a leading `>`, space or tab is skipped):
  rule-cut: <id | "gist"> -- <W-n>               a live owner word, none listed in `not_confirming` (base or HEAD)
  rule-reworded: "<old gist>" -- "<new gist>"    the new gist in a head sentence absent at the base
  rule-to-code: <id | "gist"> -- <path>          a tool or hook file that differs between the trees
A gist holds `gist_min` words and covers every cut holding it (normal form, casefolded), or equals one whole cut and covers
the cuts it equals; an id is one of the base set's carry ids and covers its gone id and every cut whose removed line holds
it. `paired:`, `reworded (by line):`, `to code (by line):` and `unused:` are evidence for the critic and the Lead, never a
verdict. A config key changed against the base needs `ratchet-raise: rule-cuts.json <key> -- <W-n>`.
"""
import collections
import fnmatch
import json
import math
import re
import subprocess
import sys

import ratchets

REL = "forge/rule-cuts.json"
CODE = ("forge/tools/", "forge/hooks/", "factory/tools/", "factory/hooks/")
FENCE_RE = re.compile(r"\s*(```|~~~)")
HEADING_RE = re.compile(r" {0,3}#{1,6}(\s|$)")
IDS_RE = re.compile(r"(?:carry|rows):(.*)")
ITEM_RE = re.compile(r"\s*([-*+]|\d+[.)])\s|\s*\|")
SPAN_RE = re.compile(r"\(case:|(?:(?<=\()|(?<=; )|(?<=, ))tools?:")
ORDINAL_RE = re.compile(r"\d+[.)]")
SENT_RE = re.compile(r"(?<=[.;!?])\s+")
LINE_RE = re.compile(r'^[ \t>]*rule-(cut|reworded|to-code): ("[^"\n]*"|[^\s"]+) -- ("[^"\n]*"|\S+)[ \t\r]*$', re.M)
EPS = 1e-9  # E28: a share AT keep is kept, though a sum of equal float weights can land a hair below it
CHECKS = {"schema": lambda v: v == "rule-cuts/1",
          "files": lambda v: isinstance(v, list) and bool(v) and all(isinstance(f, str) and f for f in v),
          "keep": lambda v: type(v) in (int, float) and 0 < v <= 1,
          "prefix": lambda v: type(v) is int and v > 0,
          "gist_min": lambda v: type(v) is int and v > 0,
          "not_confirming": lambda v: isinstance(v, list) and all(isinstance(f, str) for f in v)}
Parsed = collections.namedtuple("Parsed", "lines blocks ids sents")
Frag = collections.namedtuple("Frag", "place text ids toks nums")
Unit = collections.namedtuple("Unit", "place text toks nums")
Line = collections.namedtuple("Line", "kind target to text err")


# ---- text: normal form, words, sentences, the parse of one rule file

def span_end(text, i, tool):
    """Past the balancing `)` of a case span opened at i; at a tool clause's own `;` or its parenthesis' `)` (or the end)."""
    depth = 0
    for k in range(i, len(text)):
        depth += (text[k] == "(") - (text[k] == ")")
        if tool and (depth < 0 or text[k] == ";" and not depth):
            return k
        if not tool and not depth:
            return k + 1
    return len(text)


def strip_spans(text):
    """F7: a `(case: ...)` span is cut whole. A `tool:`/`tools:` clause opening a parenthesis or after its `; ` or `, ` is cut
    only to that clause's end: `(counted by code, tool: none yet; <rule>)` keeps its rule, and a built tool's mark dropped is
    no cut (t-2079 F1: K12's 9939cb0 went red on `(eight steps; tool: B10, not built)`)."""
    m = SPAN_RE.search(text)
    while m:
        i, tool = m.start(), text[m.start()] != "("
        if tool and text[:i].count("(") <= text[:i].count(")"):  # `, tool:` outside a parenthesis is rule text
            m = SPAN_RE.search(text, m.end())
            continue
        text = text[:i] + " " + text[span_end(text, i, tool):]
        m = SPAN_RE.search(text, i)
    return text


def norm(text):
    return " ".join(strip_spans(text).replace("*", "").replace("`", "").split())


def words(text):
    return re.findall(r"\w+", text.casefold())


def toks(text, prefix):
    return {w[:prefix] for w in words(text)}


def nums(text):
    """F8 (b): the digit runs of a text, uncut (a prefix would make 3600 and 36000 equal)."""
    return set(re.findall(r"\d+", text))


def sentences(text):
    return [s for s in SENT_RE.split(text) if s]


def kind_of(raw, fence):
    if FENCE_RE.match(raw):
        return "fence"
    if HEADING_RE.match(raw) and not fence:
        return "heading"
    if IDS_RE.match(raw):
        return "ids"
    if not re.search(r"\w", raw):
        return "blank"  # a blank line, a table separator, a rule: no token
    return "item" if ITEM_RE.match(raw) else "text"


def parse(rel, text, into):
    """Add one rule file's text lines, blocks (a paragraph, a list item with its continuation, a table row) and carry ids to
    into; a place is `<file>::<heading>`, `(top)` above the first heading."""
    place, fence, block = "%s::(top)" % rel, False, []
    for raw in text.split("\n") + [""]:
        kind = kind_of(raw, fence)
        fence ^= kind == "fence"
        if kind != "text" and block:
            into.blocks.append((block[0], " ".join(block[1:])))
            block = []
        if kind == "heading":
            place = "%s::%s" % (rel, raw.strip().lstrip("#").strip() or "(top)")
        elif kind == "ids":
            for rid in filter(None, re.split(r"[\s,]+", IDS_RE.match(raw).group(1))):
                into.ids.setdefault(rid, place)
        elif kind in ("item", "text"):
            block = (block or [place]) + [norm(raw)]
            into.lines.append((place, raw, norm(raw)))


def read(files):
    p = Parsed([], [], {}, set())
    for rel in sorted(files):
        parse(rel, files[rel], p)
    p.sents.update(s.casefold() for _, text in p.blocks for s in sentences(text))
    return p


# ---- cuts: removed lines, fragments, the weighted share

def removed(base, head):
    """Base text lines the head set holds fewer times (casefolded normal form, the whole set: a move removes nothing)."""
    left = collections.Counter(n.casefold() for _, _, n in head.lines)
    out = []
    for place, raw, n in base.lines:
        left[n.casefold()] -= 1
        if left[n.casefold()] < 0:
            out.append((place, raw, n))
    return out


def fragments(base, head, prefix):
    out = []
    for place, raw, n in removed(base, head):
        ids = set(re.split(r"[^\w:-]+", raw))  # 2.3: an id as a whole token of the raw line, `(case: ...)` included
        sents, mark = sentences(n), ITEM_RE.match(raw)
        # t-2079 B3, t-2082 R1: an ordinal is structure only as the item marker of its own line (`12. text`); a bare
        # number that a wrap left alone on a line (`3600.`) is rule text
        if mark and mark.group(1) and len(sents) > 1 and ORDINAL_RE.fullmatch(sents[0]):  # the marker, then its text
            sents = sents[1:]
        out += [Frag(place, s, ids, toks(s, prefix), nums(s)) for s in sents if words(s)]
    return out


def units_of(head, prefix):
    """The head sentences: each sentence of a block and each window of two adjacent ones (a split sentence still pairs)."""
    out = []
    for place, text in head.blocks:
        ss = sentences(text)
        out += [Unit(place, s, toks(s, prefix), nums(s)) for s in ss + [" ".join(ss[i:i + 2]) for i in range(len(ss) - 1)]]
    return out


def scorer(units):
    """F2 (b): the inverted index token -> units, and the weight ln(1 + S / df) (df 0: ln(1 + S))."""
    index = collections.defaultdict(list)
    for i, u in enumerate(units):
        for t in u.toks:
            index[t].append(i)
    s = len(units)
    return index, lambda t: math.log(1 + s / len(index[t])) if index.get(t) else math.log(1 + s)


def best(frag, units, index, w):
    """(share, every number kept, unit) of the fragment's best head unit; a tie goes to the unit keeping the numbers."""
    total = sum(map(w, frag.toks))
    found = {i for t in frag.toks for i in index.get(t, ())}
    scored = [(sum(map(w, frag.toks & units[i].toks)) / total, frag.nums <= units[i].nums, i) for i in found]
    return max(scored, default=(0.0, False, None))


def shown(text):
    return text if len(text) <= 200 else text[:200] + "..."


def cuts_of(base, head, cfg, out):
    units = units_of(head, cfg["prefix"])
    index, w = scorer(units)
    cut = []
    for f in fragments(base, head, cfg["prefix"]):
        share, whole, i = best(f, units, index, w)
        if share + EPS < cfg["keep"] or not whole:
            cut.append(f)
        elif share < 1 - EPS:
            out('paired: %s "%s" ~ %s (%.2f)' % (ratchets.encode(f.place), shown(f.text), ratchets.encode(units[i].place), share))
    return cut


# ---- the lines of the range and their covers

def gist(quoted):
    return norm(quoted[1:-1]).casefold()


def whole(text):
    """t-2079 B3: the whole form of a fragment or a gist -- normal form, casefolded, a trailing `.;!?` dropped; a `"` is
    dropped too (a quoted gist cannot hold one, t-2082 N1)."""
    return re.sub(r"[\s.;!?]+$", "", norm(text.replace('"', "")).casefold())


def short(quoted, cfg):
    return len(words(quoted)) < cfg["gist_min"]


def refusal(kind, target, to, cfg, ctx):
    """Why a line is not read (it covers nothing), or None. ctx: (head, base, paths changed in the range, the whole forms of
    the cuts). A short target gist is read when it equals a whole cut (t-2079 B3: a 1-2 word fragment had no door); a short
    gist covers only the fragments it equals (E25)."""
    head, base, changed, wholes = ctx
    quoted = [q for q in (target, to if kind == "reworded" else "") if q.startswith('"')]
    if kind == "reworded" and len(quoted) < 2:
        return "rule-reworded takes two quoted gists"
    if not target.startswith('"') and target not in base.ids:  # t-2079 B1: any word or `-` covered every cut
        return "%s is no carry id" % target
    # quoted[0] is the target when any is quoted: an unquoted reworded target is refused above
    if any(short(q, cfg) and (k or whole(q[1:-1]) not in wholes) for k, q in enumerate(quoted)):
        return "gist under %d words" % cfg["gist_min"]
    if kind == "reworded" and not any(gist(to) in s for s in head.sents - base.sents):
        return "new gist names no new text"
    if kind == "to-code" and not (to.startswith(CODE) and to in changed):
        return "%s is no tool or hook file changed in the range" % to
    return None


def confirm(wid, cfg, resolve):
    """F11 (b): a listed id never confirms a cut; else the registry decides (a live `word`)."""
    if wid in cfg["not_confirming"]:
        return "cannot confirm: %s is listed in %s not_confirming; cite the owner's word on this cut" % (wid, REL)
    return resolve(wid)


def lines_of(log, cfg, ctx, resolve, out):
    read_lines = []
    for m in LINE_RE.finditer(log):
        kind, target, to = m.groups()
        text, why = m.group(0).strip(" \t>\r"), refusal(kind, target, to, cfg, ctx)
        if why:
            out("not read: %s -- %s" % (why, text))
        else:
            read_lines.append(Line(kind, target, to, text, confirm(to, cfg, resolve) if kind == "cut" else None))
    return read_lines


def hits(line, frag, rid, cfg):
    if line.kind == "reworded" or line.target.startswith('"'):
        if frag is None:
            return False
        if short(line.target, cfg):
            return whole(line.target[1:-1]) == whole(frag.text)
        return gist(line.target) in frag.text.casefold()
    return line.target == rid if frag is None else line.target in frag.ids


def need(frag, rid, gone, cfg):
    if frag is None:
        return ("left every carry line (base: %s) -- put it on the carry line where its rule now stands, or rule-cut: %s -- "
                "<W-n>" % (ratchets.encode(gone[rid]), rid))
    if short(frag.text, cfg):  # t-2082 N1: under gist_min words the door is the whole fragment, typed as printed here
        door = frag.text.replace('"', "")
        return ('cut "%s" -- needs rule-cut: "%s" -- <W-n>, or rule-reworded: "%s" -- "<new, %d+ words>"'
                % (shown(frag.text), door, door, cfg["gist_min"]))
    return ('cut "%s" -- needs rule-cut: "<%d+ words of it>" -- <W-n>, or rule-reworded: "<old>" -- "<new, %d+ words>"'
            % (shown(frag.text), cfg["gist_min"], cfg["gist_min"]))


def cover(cuts, gone, lines, cfg, out):
    """(code, covered): one cover that resolves suffices; a cover that does not prints its red text."""
    items = [(f.place, f, None) for f in cuts] + [(rid, None, rid) for rid in sorted(gone)]
    used, covered, code = set(), 0, 0
    for place, frag, rid in items:
        mine = [k for k, ln in enumerate(lines) if hits(ln, frag, rid, cfg)]
        used.update(mine)
        errs = [lines[k].err for k in mine]
        if None in errs:
            covered += 1
            continue
        code = 1
        out(ratchets.finding(place, errs[0] if errs else need(frag, rid, gone, cfg)))
    for k, ln in enumerate(lines):
        if k not in used:
            out("unused: " + ln.text)
        elif ln.kind != "cut":
            out("%s (by line): %s -> %s" % ("reworded" if ln.kind == "reworded" else "to code", ln.target, ln.to))
    return code, covered


def judge(base_files, head_files, log, cfg, resolve, changed=frozenset()):
    """The pure core: (code, printed lines). base_files, head_files: {rel: text} of the rule set; log: the messages of the
    range; resolve(id): None for a live owner word, else its red text; changed: the paths that differ between the trees."""
    said = []
    base, head = read(base_files), read(head_files)
    cuts = cuts_of(base, head, cfg, said.append)
    gone = {rid: p for rid, p in base.ids.items() if rid not in head.ids}
    lines = lines_of(log, cfg, (head, base, changed, {whole(f.text) for f in cuts}), resolve, said.append)
    code, covered = cover(cuts, gone, lines, cfg, said.append)
    said.append("cuts: %d fragments, %d ids gone, %d covered" % (len(cuts), len(gone), covered))
    return code, said


# ---- git readers (committed trees only) and the run

def config_of(raw):
    try:
        cfg = json.loads(raw)
    except ValueError as exc:  # UnicodeDecodeError is one too
        raise ratchets.Refuse("%s at HEAD: not valid UTF-8 JSON (%s)" % (REL, exc))
    bad = [k for k, ok in CHECKS.items() if not isinstance(cfg, dict) or not ok(cfg.get(k))]
    if bad:
        raise ratchets.Refuse("%s at HEAD: %s absent or malformed" % (REL, ", ".join(bad)))
    return cfg


def raised(old, cfg):
    """2.5: every key whose value differs between the base and HEAD, a key gone or added too (not ordered: errs red)."""
    if not isinstance(old, dict):
        raise ratchets.Refuse("%s at the base: not one JSON object" % REL)
    return {k: ("key changed", ("word",)) for k in sorted(set(old) | set(cfg)) if old.get(k) != cfg.get(k)}


def in_set(rel, pats):
    parts = rel.split("/")
    return any(len(p.split("/")) == len(parts) and all(map(fnmatch.fnmatchcase, parts, p.split("/"))) for p in pats)


def batch(root, specs):
    """The bytes of each `<rev>:<path>` by ONE `git cat-file --batch` (a process per blob cost about 60 ms on Windows)."""
    r = subprocess.run(["git", "-C", root, "cat-file", "--batch"], input="".join(s + "\n" for s in specs).encode("utf-8"),
                       capture_output=True)
    if r.returncode:
        raise ratchets.Refuse("git cat-file failed")
    data, pos, out = r.stdout, 0, []
    for _ in specs:
        end = data.find(b"\n", pos)
        head = data[pos:end].split(b" ")
        size = int(head[2]) if len(head) == 3 and head[2].isdigit() else -1  # `<spec> missing` holds no size
        out.append(data[end + 1:end + 1 + size] if size >= 0 else b"")
        pos = end + 2 + size  # past the content and its newline; a missing spec (-1) is one header line
    return out


def trees(root, revs, pats):
    """[{rel: text}] of the rule set at each rev; a blob that is not UTF-8 is exit 2 naming it (I4)."""
    specs = []
    for rev in revs:
        listed = ratchets.git(root, "ls-tree", "-r", "-z", "--name-only", rev)
        if listed.returncode:
            raise ratchets.Refuse("%s: tree unreadable" % rev)
        specs += [(rev, r) for r in listed.stdout.decode("utf-8", "replace").split("\0") if r and in_set(r, pats)]
    out = [{} for _ in revs]
    for (rev, rel), raw in zip(specs, batch(root, ["%s:%s" % s for s in specs])):
        try:
            out[revs.index(rev)][rel] = raw.decode("utf-8")
        except UnicodeDecodeError:
            raise ratchets.Refuse("%s:%s: not UTF-8" % (rev[:12], rel))
    return out


def changed(root, base, head="HEAD"):
    listed = ratchets.git(root, "diff", "--name-only", "-z", base, head, "--", *[c.rstrip("/") for c in CODE])
    return set(ratchets.text_of(listed).split("\0")) - {""}


def run(argv):
    a = ratchets.parser(__doc__.split("\n")[0]).parse_args(argv)
    shown_cfg = ratchets.git(a.root, "show", "HEAD:" + REL)
    if shown_cfg.returncode:
        raise ratchets.Refuse("%s: absent at HEAD" % REL)
    cfg = config_of(shown_cfg.stdout)
    base = ratchets.base_of(a.root, a.base)
    if base is None:
        print("cuts not judged: no base")
        return 0
    old = ratchets.base_doc(a.root, base, REL, print)
    keys = raised(old, cfg) if old is not None else {}
    was = old.get("not_confirming") if isinstance(old, dict) else None
    listed = set(cfg["not_confirming"]) | set(was if CHECKS["not_confirming"](was) else ())  # B2: the push may empty it
    log = ratchets.text_of(ratchets.git(a.root, "log", "--format=%B", "%s..HEAD" % base))
    # t-2079 B2, t-2082 B2-bis: a listed id never confirms a config change either, whatever else the lines cite
    codes = [ratchets.judge_raises(a.root, base, REL, keys, print, lambda wid: (
        "cannot confirm: %s is listed in not_confirming" % wid if wid in listed else None))]
    moved = changed(a.root, base) if "rule-to-code:" in log else frozenset()  # one process fewer on most runs
    code, said = judge(*trees(a.root, [base, "HEAD"], cfg["files"]), log, dict(cfg, not_confirming=sorted(listed)),
                       lambda rid: ratchets.resolve(a.root, rid, ("word",)), moved)
    print("\n".join(said))
    return ratchets.verdict(codes + [code])


def main(argv):
    return ratchets.guarded(run, argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
