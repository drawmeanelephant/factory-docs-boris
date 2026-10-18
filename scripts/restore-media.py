#!/usr/bin/env python3
"""Reconstruct the large original video from its small, hash-verified LFS chunks."""

import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import tempfile


def media_path(root, name):
    parts = name.split("/")
    if PurePosixPath(name).is_absolute() or "\\" in name or any(
        part in ("", ".", "..") for part in parts
    ):
        raise ValueError("Unsafe media path")
    result = root
    for part in parts:
        result = result / part
        if result.is_symlink():
            raise ValueError("Media paths must not contain symlinks")
    return result


def restore_media(root):
    manifest = json.loads((root / ".media-chunks/manifest.json").read_text())
    for media in manifest:
        target = media_path(root, media["path"])
        if target.exists():
            if target.stat().st_size != media["bytes"] or (
                hashlib.sha256(target.read_bytes()).hexdigest() != media["sha256"]
            ):
                raise ValueError("Existing media differs from the original; refusing to overwrite it")
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            digest = hashlib.sha256()
            total = 0
            with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as output:
                temporary = Path(output.name)
                for chunk in media["chunks"]:
                    content = media_path(root, chunk["path"]).read_bytes()
                    if len(content) != chunk["bytes"] or (
                        hashlib.sha256(content).hexdigest() != chunk["sha256"]
                    ):
                        raise ValueError("Media chunk size or digest mismatch")
                    output.write(content)
                    digest.update(content)
                    total += len(content)
            if total != media["bytes"] or digest.hexdigest() != media["sha256"]:
                raise ValueError("Reconstructed media size or digest mismatch")
            os.replace(temporary, target)
            temporary = None
        finally:
            if temporary is not None:
                temporary.unlink()


if __name__ == "__main__":
    restore_media(Path(__file__).resolve().parents[1])
    print("Original media verified and ready")
