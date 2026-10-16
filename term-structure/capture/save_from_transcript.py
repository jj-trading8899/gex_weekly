#!/usr/bin/env python3
"""For Claude-run captures: find the JSON that capture.js returned in this session's
transcript and save it to data/raw/<ET date>.json. Prints the saved path.

Usage: python3 capture/save_from_transcript.py [transcript.jsonl]
"""
import datetime as dt, glob, json, os, sys
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_REPO_DATA = os.path.join(ROOT, "..", "data", "term-structure")
DATA = os.path.normpath(_REPO_DATA) if os.path.isdir(_REPO_DATA) else os.path.join(ROOT, "data")
paths = sys.argv[1:] or sorted(glob.glob(os.path.expanduser("~/.claude/projects/**/*.jsonl"), recursive=True),
                               key=os.path.getmtime)[-3:]
found = None

def walk(o):
    global found
    if isinstance(o, str):
        t = o.lstrip()
        if t.startswith('"{\\"capturedAt') or t.startswith('{"capturedAt'):
            found = t
    elif isinstance(o, dict):
        for v in o.values(): walk(v)
    elif isinstance(o, list):
        for v in o: walk(v)

for p in paths:
    for line in open(p, errors="ignore"):
        try: walk(json.loads(line))
        except Exception: pass
if not found:
    sys.exit("No capture result found in transcript")
val, _ = json.JSONDecoder().raw_decode(found)
data = json.loads(val) if isinstance(val, str) else val
bad = [t for t, v in data["tickers"].items() if "error" in v]
if bad:
    sys.exit(f"Capture has errors for {bad}: " + "; ".join(data['tickers'][t]['error'] for t in bad))
et = dt.datetime.fromisoformat(data["capturedAt"].replace("Z", "+00:00")).astimezone(ZoneInfo("America/New_York"))
out = os.path.join(DATA, "raw", et.date().isoformat() + ".json")
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump(data, open(out, "w"))
print(out)
