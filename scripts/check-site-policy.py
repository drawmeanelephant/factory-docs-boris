#!/usr/bin/env python3
"""Gate the published artifact on unofficial notices, noindex, and excluded pages."""

import argparse
from html.parser import HTMLParser
import json
from pathlib import Path


EXCLUDED = {"pricing.html", "support.html", "jp/pricing.html", "jp/support.html"}


class PagePolicy(HTMLParser):
    def __init__(self):
        super().__init__()
        self.robots = set()
        self.notices = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta" and attrs.get("name", "").lower() == "robots":
            self.robots.update(value.strip().lower() for value in attrs.get("content", "").split(","))
        self.notices.update(attrs.get("class", "").split())


def check_site(html_dir):
    inventory = json.loads((html_dir / "_boris/proof/artifacts.json").read_text())
    paths = {record["path"] for record in inventory["artifacts"]}
    if paths & EXCLUDED or any((html_dir / name).exists() for name in EXCLUDED):
        raise ValueError("Pricing or support HTML is still present")
    index = json.loads((html_dir / "_boris/search/search-index.json").read_text())
    if any(document["path"] in EXCLUDED for document in index["documents"]):
        raise ValueError("Pricing or support is still in search")
    pages = 0
    for record in inventory["artifacts"]:
        if not record["path"].endswith(".html"):
            continue
        text = (html_dir / record["path"]).read_text()
        policy = PagePolicy()
        policy.feed(text)
        if not {"noindex", "nofollow", "noarchive"} <= policy.robots:
            raise ValueError(f"Missing crawler policy: {record['path']}")
        if "not affiliated with" not in text.lower():
            raise ValueError(f"Missing non-affiliation notice: {record['path']}")
        if record["kind"] == "html-page" and not {
            "factory-unofficial-notice", "factory-article-disclaimer"
        } <= policy.notices:
            raise ValueError(f"Missing static disclaimers: {record['path']}")
        pages += 1
    print(f"Unofficial-site policy passed for {pages} HTML files; pricing/support excluded")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html-dir", type=Path, default=Path("dist"))
    check_site(parser.parse_args().html_dir)
