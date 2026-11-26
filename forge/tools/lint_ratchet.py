# card: C1-3
"""Lint ratchet: pyflakes over the C1-3 roots (and forge/tests, F256 (b)), against forge/baselines/lint.json.

lint_ratchet.py [--root D] [--base R] [--update [--record ID]] [--basis] [--list]
Identity of a finding: `<path>::<MessageClass>:<args joined by ,>`, no line (a moved finding keeps it); the line argument of
RedefinedWhileUnused, ImportShadowedByLoopVar and UndefinedLocal is written `<line>`; repeats are one finding, ` x<n>`.
pyflakes is imported first (not importable: exit 2, even on an empty scope). A syntax or unexpected error is red, never allowed
by a row. Scope, source reading, the driver and every list rule are ratchets.py's.
"""
import importlib
import sys
import warnings

import ratchets

EXTRA = ("forge/tests",)  # F256 (b): one lint rule for test files in every tree
SPEC = ratchets.Spec("forge/baselines/lint.json", scope=ratchets.globs(ratchets.ROOTS + EXTRA))
LINE_CLASSES = ("RedefinedWhileUnused", "ImportShadowedByLoopVar", "UndefinedLocal")  # message_args[1] is a line


class Collector:
    """pyflakes' reporter: keeps what it is told, prints nothing."""

    def __init__(self):
        self.flakes, self.errors = [], []

    def unexpectedError(self, filename, msg):
        self.errors.append(str(msg))

    def syntaxError(self, filename, msg, lineno, offset, text):
        self.errors.append("SyntaxError: %s (line %s)" % (msg, lineno))

    def flake(self, message):
        self.flakes.append(message)


def check_args(a):
    try:
        importlib.import_module("pyflakes.api")
    except ImportError:
        raise ratchets.Refuse("pyflakes not importable (%s)" % ratchets.INSTALL)


def basis():
    version = importlib.import_module("pyflakes").__version__
    return {"tool": "pyflakes %s" % version, "python": ratchets.python_minor(), "constants": {"line_classes": list(LINE_CLASSES)},
            "roots": list(ratchets.ROOTS + EXTRA)}


def ident_of(rel, m):
    args = [str(x) for x in m.message_args]
    if type(m).__name__ in LINE_CLASSES and len(args) > 1:
        args[1] = "<line>"
    return ratchets.encode("%s::%s:%s" % (rel, type(m).__name__, ",".join(args)))  # F1: one token


def sites_of(rel, flakes):
    seen = {}
    for m in flakes:
        seen.setdefault(ident_of(rel, m), []).append(m)
    return [(i, "%s (line %d)%s" % (ms[0].message % ms[0].message_args, ms[0].lineno, " x%d" % len(ms) if len(ms) > 1 else ""))
            for i, ms in seen.items()]


def lint_file(api, root, rel):
    col = Collector()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        api.check(ratchets.read_source(root, rel), rel, col)
    return sites_of(rel, col.flakes), col.errors


def scan(root, a, data):
    api = importlib.import_module("pyflakes.api")
    files = ratchets.scope(root, ratchets.ROOTS + EXTRA, tests=True)
    sites, broken, read = [], [], len(files)
    for rel in files:
        try:
            found, errors = lint_file(api, root, rel)
        except ratchets.BAD as exc:
            found, errors = [], [ratchets.describe(exc)]
            read -= isinstance(exc, OSError)
        sites += found
        broken += [(rel, errors[0])] if errors else []
    return ratchets.Scan(sites, broken, len(files), read)


def main(argv):
    return ratchets.entry(sys.modules[__name__], argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
