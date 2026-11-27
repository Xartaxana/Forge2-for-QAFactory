# card: C1-5, B5
"""Adapt Codex PreToolUse events to the Forge hook inputs."""
from pathlib import Path
import sys

import budget
import foreign_write
from hio import io as HIO

ROOT = str(Path(__file__).resolve().parents[2])
PATCH_HEADERS = ("*** Add File: ", "*** Update File: ", "*** Delete File: ", "*** Move to: ")


def calls(payload):
    """Use the tool's working directory and expose every path in a native patch."""
    name = payload.get("tool_name")
    tool_input = payload.get("tool_input")
    if not isinstance(tool_input, dict):
        return [payload]
    command = tool_input.get("command")
    cwd = tool_input.get("workdir")
    if isinstance(cwd, str) and cwd:
        payload = dict(payload, cwd=cwd)
    if name in ("Bash", "exec_command", "shell_command"):
        shell = str(tool_input.get("shell") or "").replace("\\", "/").rsplit("/", 1)[-1].lower()
        powershell = shell in ("pwsh", "powershell", "pwsh.exe", "powershell.exe")
        return [dict(payload, tool_name="PowerShell" if powershell or (not shell and sys.platform == "win32")
                     else "Bash")]
    if name != "apply_patch" or not isinstance(command, str):
        return [payload]
    return [
        dict(payload, tool_name="Write" if header == PATCH_HEADERS[0] else "Edit",
             tool_input={"file_path": line[len(header):]})
        for line in command.splitlines()
        for header in PATCH_HEADERS
        if line.startswith(header)
    ] or [payload]


def body(payload, note):
    if payload is None:
        return budget.body(payload, note, ROOT)
    events = calls(dict(payload, forge_host="codex"))
    for event in events:
        if event.get("tool_name") in foreign_write.FILE_TOOLS + foreign_write.SHELLS:
            if foreign_write.body(event, note, ROOT):
                return 2
    event = events[0]
    if len(events) > 1:
        paths = [e["tool_input"]["file_path"] for e in events]
        event = dict(event, tool_input={"file_paths": paths})
    return budget.body(event, note, ROOT)


if __name__ == "__main__":
    sys.exit(HIO.guard(body, "pass", "json"))
