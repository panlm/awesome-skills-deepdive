#!/usr/bin/env python3
"""Spawn sync_translate.py fully detached from the parent shell."""
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "cache" / "logs" / "detached.log"
LOG.parent.mkdir(parents=True, exist_ok=True)

with open(LOG, "ab") as f:
    proc = subprocess.Popen(
        [sys.executable, str(ROOT / "scripts" / "sync_translate.py"), *sys.argv[1:]],
        stdin=subprocess.DEVNULL,
        stdout=f,
        stderr=subprocess.STDOUT,
        start_new_session=True,  # the key: equivalent to setsid
        cwd=str(ROOT),
    )
print(f"spawned pid={proc.pid}, logging to {LOG}")
