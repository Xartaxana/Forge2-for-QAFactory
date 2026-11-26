"""Fixture harness for forge/tests/test_seeded.py: never a real harness (C0-4 edge). argv: mode, model."""
import json
import sys

mode, model = sys.argv[1], sys.argv[2]
if mode == "fail":
    sys.exit(1)
text = {"empty": "", "canary": "seen CANARY-T1x", "judge": "T1.D1: caught\nI1: unsure"}.get(mode, "blocker: off by one")
used = {"othermodel": "claude-haiku"}.get(mode, model)
print(json.dumps({"result": text, "modelUsage": {used: {"inputTokens": 5, "costUSD": 1.5}}}))
