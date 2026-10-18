#!/usr/bin/env python3
"""Copy only hash-verified publication artifacts, excluding local proof and cache files."""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath


MAX_BYTES = 1024 * 1024 * 1024


def prepare(source, destination):
    if source.is_symlink() or not source.is_dir() or destination.is_symlink():
        raise ValueError("Source and destination must not be symlinks")
    inventory_path = source / "_boris/proof/artifacts.json"
    inventory_bytes = inventory_path.read_bytes()
    inventory = json.loads(inventory_bytes)
    if (
        inventory.get("format") != "boris-publication-artifacts"
        or inventory.get("schema_version") != 1
        or inventory.get("target") != "public"
    ):
        raise ValueError("Unsupported publication inventory")
    if destination.exists() and (not destination.is_dir() or any(destination.iterdir())):
        raise ValueError("Destination must be a new or empty directory")
    records = inventory["artifacts"]
    seen = set()
    total = 0
    for record in records:
        name = record["path"]
        parts = name.split("/")
        relative = PurePosixPath(name)
        if (
            not name
            or relative.is_absolute()
            or "\\" in name
            or any(part in ("", ".", "..") for part in parts)
            or name.startswith(("_boris/proof/", ".boris-cache/"))
            or name in ("_boris/proof", ".boris-cache")
            or name in seen
            or record["status"] != "committed"
        ):
            raise ValueError(f"Unsafe or uncommitted artifact: {name}")
        seen.add(name)
        current = source
        for part in parts:
            current = current / part
            if current.is_symlink():
                raise ValueError(f"Symlink in artifact path: {name}")
        if not current.is_file() or current.stat().st_nlink != 1:
            raise ValueError(f"Artifact must be an unlinked regular file: {name}")
        content = current.read_bytes()
        if len(content) != record["bytes"] or hashlib.sha256(content).hexdigest() != record["sha256"]:
            raise ValueError(f"Artifact digest or size mismatch: {name}")
        total += len(content)
        if total > MAX_BYTES:
            raise ValueError("Pages artifact exceeds the 1 GiB limit")
        target = destination.joinpath(*parts)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    if "index.html" not in seen:
        raise ValueError("Publication must contain index.html")
    return {
        "files": len(seen),
        "bytes": total,
        "inventory_sha256": hashlib.sha256(inventory_bytes).hexdigest(),
        "proof_paths_excluded": True,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("dist"))
    parser.add_argument("--destination", type=Path, default=Path("public-site"))
    parser.add_argument("--summary", type=Path, default=Path(".pages-evidence/artifact.json"))
    args = parser.parse_args()
    summary = prepare(args.source, args.destination)
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    args.summary.write_text(json.dumps(summary, indent=2) + "\n")
    print(f"Verified {summary['files']} files ({summary['bytes']} bytes) for Pages")
