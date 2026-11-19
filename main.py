"""Entry for make.fun news-image-20261118.

Copies the pre-rendered poster (image.png, shipped in this repository)
to /output/entry.png. Standard library only, no network, deterministic:
the output bytes are always identical to image.png.
"""

import hashlib
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "image.png")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    with open(src, "rb") as f:
        src_hash = hashlib.sha256(f.read()).hexdigest()
    with open(dst, "rb") as f:
        dst_hash = hashlib.sha256(f.read()).hexdigest()
    assert src_hash == dst_hash, "output differs from image.png"
    assert os.path.getsize(src) == os.path.getsize(dst), "output size differs"
    print("sha256: " + dst_hash)
    print("Wrote " + dst + " (" + str(os.path.getsize(dst)) + " bytes)")


if __name__ == "__main__":
    main()
