# food-picture-01 entry: emit the bundled ramen photograph.
#
# The picture lives in this repository as entry.png (JPEG bytes). Running
# this program copies those exact bytes to MAKEFUN_OUTPUT_DIR/entry.png
# (or /output when the variable is unset). Pure standard library, no
# network access, no randomness, no clock reads, so two runs always
# produce identical output.

import os
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"


def run() -> int:
    folder = Path(__file__).resolve().parent
    picture = folder / IMAGE_NAME
    if not picture.is_file():
        print(f"missing {IMAGE_NAME} next to main.py", file=sys.stderr)
        return 1
    destination_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination_dir.mkdir(parents=True, exist_ok=True)
    data = picture.read_bytes()
    target = destination_dir / IMAGE_NAME
    target.write_bytes(data)
    # Guard the gate: the emitted file must be byte-identical to the bundle.
    if target.stat().st_size != len(data):
        print("output size mismatch after write", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
