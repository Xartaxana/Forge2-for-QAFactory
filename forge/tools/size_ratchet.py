# card: C1-2
"""Size ratchet: each row of forge/budgets.json measured against its ceiling; a raised ceiling needs a raise line (B20).

size_ratchet.py [--root D] [--base R]    exit 0 green, 1 a value above its ceiling or an unrecorded raise, 2 cannot judge
Units: bytes, nonblank_lines, rows (of a JSON {"rows": [...]}), limit (read by another tool; only its raise is judged here).
A path with no file is `absent: 0`. `stage_start_load: null` is `not set` (F248): listed and counted, outside the exit.
The figure line `tests: <t> lines, product: <p> lines (ratio <t/p>)` is never a verdict (B20 (f)).
"""
import glob
import os
import sys

import ratchets

REL = "forge/budgets.json"
UNITS = ("bytes", "nonblank_lines", "rows", "limit")
TESTS = ("forge/tests/**/*.py", "factory/tests/**/*.py")
PRODUCT = tuple(d + "/**/*.py" for d in ("forge/tools", "forge/hooks", "factory/tools", "factory/hooks", "measure/tools"))


def check_rows(data):
    rows = data.get("rows") if isinstance(data, dict) else None
    if not isinstance(rows, dict):
        raise ratchets.Refuse('%s: must hold {"rows": {...}}' % REL)
    for key, row in rows.items():
        if key == "stage_start_load" and (row is None or isinstance(row, dict)):
            continue
        ok = isinstance(row, dict) and row.get("unit") in UNITS
        ok = ok and type(row.get("ceiling")) is int and row["ceiling"] >= 0
        paths = row.get("paths") if ok else None
        if not ok or (row["unit"] != "limit" and not (isinstance(paths, list) and paths and all(isinstance(p, str) for p in paths))):
            raise ratchets.Refuse("%s row %s: needs a known unit, a non-negative integer ceiling and paths" % (REL, key))
    return rows


def files_of(root, patterns):
    found = set()
    for pat in patterns:
        for rel in glob.glob(pat, root_dir=root, recursive=True):
            if os.path.isfile(os.path.join(root, rel)):
                found.add(rel.replace("\\", "/"))
    return sorted(found)


def nonblank(root, rel):
    with open(os.path.join(root, rel), "rb") as fh:
        return sum(1 for ln in fh.read().decode("utf-8", "replace").split("\n") if ln.strip())


def count_rows(root, rel):
    data = ratchets.read_json(os.path.join(root, rel), rel)
    if not isinstance(data, dict) or not isinstance(data.get("rows"), list):
        raise ratchets.Refuse('%s: must be JSON {"rows": [...]}' % rel)
    return len(data["rows"])


def measure(root, row):
    """The row's value, or None when no file of its paths exists."""
    files = files_of(root, row["paths"])
    if not files:
        return None
    if row["unit"] == "bytes":
        return sum(os.path.getsize(os.path.join(root, f)) for f in files)
    if row["unit"] == "nonblank_lines":
        return sum(nonblank(root, f) for f in files)
    return sum(count_rows(root, f) for f in files)


def judge_row(root, key, row, out):
    if key == "stage_start_load":
        out("%s: %s" % (key, "not set: first measured run (F9)" if row is None else "set (judged by the stage start card)"))
        return 0
    if row["unit"] == "limit":
        out("%s: limit %d (read by its tool)" % (key, row["ceiling"]))
        return 0
    value = measure(root, row)
    out("%s: %s (ceiling %d)" % (key, "absent: 0" if value is None else "%d %s" % (value, row["unit"]), row["ceiling"]))
    if (value or 0) <= row["ceiling"]:
        return 0
    out(ratchets.finding("%s::%s" % (REL, key), "value %d > ceiling %d" % (value, row["ceiling"])))
    return 1


def raised(old, rows):
    keys = {}
    for key, row in rows.items():
        before = old.get(key)
        if isinstance(row, dict) and isinstance(before, dict) and row["ceiling"] > before["ceiling"]:
            keys[key] = "ceiling %d -> %d" % (before["ceiling"], row["ceiling"])
    return keys


def figure(root):
    t = sum(nonblank(root, f) for f in files_of(root, TESTS))
    p = sum(nonblank(root, f) for f in files_of(root, PRODUCT))
    return "tests: %d lines, product: %d lines (ratio %s)" % (t, p, "%.2f" % (t / p) if p else "n/a")


def run(argv):
    a = ratchets.parser(__doc__.split("\n")[0]).parse_args(argv)
    rows = check_rows(ratchets.read_json(os.path.join(a.root, REL), REL))
    base = ratchets.base_of(a.root, a.base)
    codes = [judge_row(a.root, k, r, print) for k, r in rows.items()]
    old = ratchets.base_doc(a.root, base, REL, print)
    if old is not None:
        codes.append(ratchets.judge_raises(a.root, base, REL, raised(check_rows(old), rows), print))
    print(figure(a.root))
    return ratchets.verdict(codes)


def main(argv):
    return ratchets.guarded(run, argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
