#!/usr/bin/env python3
"""make.fun news-image-20261122 entry.

The repository holds the finished front-page image in entry.png, drawn for
this competition in the build session. This program simply copies it to the
output location, so it runs with no network and writes exactly the same
bytes on every run.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        sys.exit(f"entry image missing beside main.py: {SOURCE}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    print(f"wrote {target} ({target.stat().st_size} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
