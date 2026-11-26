# card: C1-5
"""Loads _io.py by path under another name: `_io` is a CPython built-in, so `import _io` can never reach the file."""
import importlib.util
import os
import sys

_spec = importlib.util.spec_from_file_location("forge_hooks_io", os.path.join(os.path.dirname(os.path.abspath(__file__)), "_io.py"))
io = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = io
_spec.loader.exec_module(io)
