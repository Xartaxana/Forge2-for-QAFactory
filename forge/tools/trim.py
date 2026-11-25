# card: C1-4
"""Trim run output before it enters a context: keep the last N lines, plus dropped lines a --keep pattern matches.

trim.py [--root D] [--last N] [--keep REGEX]... [file]     file defaults to stdin; N defaults to 30

At or under N lines the text is printed whole. Over N: a first line [trimmed K of M lines] (K = lines not printed),
the kept lines in their order, then the last N lines. Bytes read as UTF-8 with replacement; if any were replaced the
marker is printed even when K is 0. Exit: 0, 2 for N below 1 or a pattern that does not compile.
"""
import argparse
import collections
import contextlib
import re
import sys


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root")  # accepted for the common door of the tools; trim reads no repository data
    p.add_argument("--last", type=int, default=30)
    p.add_argument("--keep", action="append", default=[])
    p.add_argument("file", nargs="?")
    a = p.parse_args(argv)
    if a.last < 1:
        print("--last must be at least 1, got %d" % a.last)
        return 2
    pats = []
    for k in a.keep:
        try:
            pats.append(re.compile(k))
        except re.error as exc:
            print("--keep pattern %r does not compile: %s" % (k, exc))
            return 2
    # streamed line by line: memory is bounded by N plus the kept lines, however large the log (review t-1944, F9)
    tail, kept, m, replaced = collections.deque(maxlen=a.last), [], 0, False
    with (open(a.file, "rb") if a.file else contextlib.nullcontext(sys.stdin.buffer)) as src:
        for chunk in src:
            try:
                ln = chunk.decode("utf-8")
            except UnicodeDecodeError:
                ln, replaced = chunk.decode("utf-8", "replace"), True
            ln = ln[:-1] if ln.endswith("\n") else ln
            m += 1
            if len(tail) == a.last:
                old = tail[0]  # about to leave the tail; a CR is dropped for the match only, the line prints as it was
                if any(q.search(old[:-1] if old.endswith("\r") else old) for q in pats):
                    kept.append(old)
            tail.append(ln)
    out = kept + list(tail)
    if m > a.last or replaced:
        out.insert(0, "[trimmed %d of %d lines%s]" % (m - len(kept) - len(tail) if m > a.last else 0, m,
                                                     "; non-UTF-8 bytes replaced" if replaced else ""))
    sys.stdout.buffer.write(("\n".join(out) + "\n").encode("utf-8") if out else b"")
    return 0


if __name__ == "__main__":
    sys.exit(main())
