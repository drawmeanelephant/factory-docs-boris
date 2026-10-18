#!/usr/bin/env python3
"""Bind the site profile to the location supplied by GitHub Pages."""

import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit


def pages_profile(profile, base_url):
    location = urlsplit(base_url)
    if (
        location.scheme != "https"
        or not location.netloc
        or location.username
        or location.password
        or location.query
        or location.fragment
    ):
        raise ValueError("Pages URL must be an HTTPS origin and optional site path")
    base_path = location.path.rstrip("/")
    if any(part in (".", "..") for part in base_path.split("/")):
        raise ValueError("Pages path cannot contain relative components")
    origin = f"{location.scheme}://{location.netloc}"
    normalized = origin + base_path
    profile["site"]["url"] = normalized
    profile["publication"] = {
        "target": "github-pages",
        "base_url": normalized,
        "origin": origin,
        "base_path": base_path,
    }
    for target in profile["targets"]:
        if target.get("head", {}).get("enabled"):
            target["head"]["base_url"] = normalized
    return profile


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--profile", type=Path, default=Path("boris.json"))
    parser.add_argument("--out", type=Path, default=Path(".boris-pages-profile.json"))
    args = parser.parse_args()
    args.out.write_text(
        json.dumps(pages_profile(json.loads(args.profile.read_text()), args.base_url), indent=2) + "\n"
    )
