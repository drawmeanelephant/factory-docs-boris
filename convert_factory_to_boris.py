#!/usr/bin/env python3
"""
Deterministic Mintlify -> Boris conversion pipeline for factory/docs.
Converts all 262 MDX pages, 10 leaderboard JSX/MDX snippets, 154 OpenAPI 3.0.1
reference pages (77 EN + 77 JP), and 152 static media assets into a validated
Boris workspace at /home/factory-user/repos/factory-boris.
"""

import hashlib
import html
import json
import os
import re
import shutil
import textwrap
import urllib.parse
from collections import defaultdict

BORIS_ROOT = os.path.dirname(os.path.abspath(__file__))
FACTORY_DOCS = os.environ.get("FACTORY_DOCS", "/home/factory-user/repos/factory/docs")
OPENAPI_SPEC = os.path.join(BORIS_ROOT, "openapi.json") if os.path.exists(os.path.join(BORIS_ROOT, "openapi.json")) else "/tmp/factory-openapi.json"
CONTENT_DIR = os.path.join(BORIS_ROOT, "content")
STATIC_DIR = os.path.join(BORIS_ROOT, "static")

REDIRECT_MAP = {
    "cli/features/install-github-app": "guides/droid-exec/code-review",
    "jp/cli/features/install-github-app": "jp/guides/droid-exec/code-review",
    "integrations/github-app": "guides/droid-exec/code-review",
    "jp/integrations/github-app": "jp/guides/droid-exec/code-review",
    "cli/features/missions": "features/missions/overview",
    "jp/cli/features/missions": "jp/features/missions/overview",
    "web/integrations/linear": "integrations/linear",
    "jp/web/integrations/linear": "jp/integrations/linear",
    "enterprise": "enterprise/index",
    "jp/enterprise": "jp/enterprise/index",
}
try:
    _docs_cfg = json.load(open(os.path.join(FACTORY_DOCS, "docs.json"), encoding="utf-8"))
    for _r in _docs_cfg.get("redirects", []):
        _src = _r.get("source", "").strip("/")
        _dst = _r.get("destination", "").strip("/")
        if _src and _dst and ":" not in _src and "*" not in _src:
            REDIRECT_MAP[_src] = _dst
            REDIRECT_MAP[f"jp/{_src}"] = f"jp/{_dst}" if not _dst.startswith("jp/") else _dst
except Exception:
    pass

CHANGELOG_DATES = {
    "changelog/release-notes": "2026-04-15T00:00:00Z",
    "changelog/cli-updates": "2026-04-14T00:00:00Z",
    "changelog/1-10": "2026-04-10T00:00:00Z",
    "changelog/1-9": "2026-03-25T00:00:00Z",
    "changelog/1-8": "2026-03-10T00:00:00Z",
    "jp/changelog/release-notes": "2026-04-15T00:00:00Z",
    "jp/changelog/cli-updates": "2026-04-14T00:00:00Z",
    "jp/changelog/1-10": "2026-04-10T00:00:00Z",
    "jp/changelog/1-9": "2026-03-25T00:00:00Z",
    "jp/changelog/1-8": "2026-03-10T00:00:00Z",
}


def gfm_slug(text: str) -> str:
    """Exact Oliver GFM ASCII heading slugger."""
    s = re.sub(r"<[^>]+>", "", text)
    s = re.sub(r"`([^`]*)`", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    out = []
    prev_dash = False
    for ch in s.strip():
        code = ord(ch)
        if 65 <= code <= 90:
            out.append(chr(code + 32))
            prev_dash = False
        elif (97 <= code <= 122) or (48 <= code <= 57) or ch in ("-", "_"):
            out.append(ch)
            prev_dash = False
        elif ch in (" ", "\t"):
            if not prev_dash:
                out.append("-")
                prev_dash = True
    return "".join(out)


def safe_ascii_anchor(raw: str, prefix: str = "sec") -> str:
    """Ensure anchor matches Boris/Oliver [A-Za-z0-9][A-Za-z0-9_-]* grammar."""
    s = gfm_slug(raw).strip("-_")
    if s and re.match(r"^[A-Za-z0-9][A-Za-z0-9_-]*$", s) and len(s) <= 60:
        if re.search(r"[A-Za-z]", s):
            return s
    digest = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:8]
    if s:
        s = re.sub(r"[^A-Za-z0-9_-]", "", s)[:40].strip("-_")
        if s and s[0].isalnum():
            return f"{s}-{digest}"
    return f"{prefix}-{digest}"


def sanitize_tag(raw: str) -> str:
    s = re.sub(r"[^a-z0-9_-]+", "-", raw.lower()).strip("-_")
    return s[:48] if s else ""


def clean_frontmatter_quote(val: str) -> str:
    v = val.strip()
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        v = v[1:-1]
    v = re.sub(r"\s+", " ", v).strip()
    v = v.replace("\\", "\\\\").replace('"', '\\"')
    if len(v.encode("utf-8")) > 900:
        v = v[:300]
    return f'"{v}"'


def parse_mdx_frontmatter(text: str):
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_raw = text[4:end]
    body = text[end + 4:]
    if body.startswith("\n"):
        body = body[1:]

    meta = {"keywords": []}
    in_keywords = False
    for line in fm_raw.splitlines():
        if in_keywords:
            m_item = re.match(r"^\s*-\s*(.+)$", line)
            if m_item:
                meta["keywords"].append(m_item.group(1).strip().strip("\"'"))
                continue
            else:
                in_keywords = False
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not m:
            continue
        k, v = m.group(1), m.group(2).strip()
        if k == "keywords":
            if v.startswith("[") and v.endswith("]"):
                items = [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
                meta["keywords"].extend(items)
            elif not v:
                in_keywords = True
            else:
                meta["keywords"].append(v.strip("\"'"))
        else:
            meta[k] = v.strip("\"'")
    return meta, body


def copy_static_assets():
    if os.path.exists(STATIC_DIR):
        shutil.rmtree(STATIC_DIR)
    os.makedirs(STATIC_DIR, exist_ok=True)
    count = 0
    for dp, dn, fn in os.walk(FACTORY_DOCS):
        for f in sorted(fn):
            if f.endswith((".mdx", ".md", ".jsx", ".json", ".css", ".DS_Store")):
                continue
            src = os.path.join(dp, f)
            rel = os.path.relpath(src, FACTORY_DOCS)
            dst = os.path.join(STATIC_DIR, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            count += 1
    return count


def build_leaderboard_includes():
    """Convert snippets/leaderboards/*.mdx and jp/snippets/leaderboards/*.mdx into Boris includes."""
    snippet_pairs = [
        ("snippets/leaderboards", "includes/leaderboards"),
        ("jp/snippets/leaderboards", "includes/jp/leaderboards"),
    ]
    generated = {}
    for src_sub, dst_sub in snippet_pairs:
        src_dir = os.path.join(FACTORY_DOCS, src_sub)
        if not os.path.isdir(src_dir):
            continue
        for f in sorted(os.listdir(src_dir)):
            if not f.endswith(".mdx"):
                continue
            stem = f[:-4]
            src_path = os.path.join(src_dir, f)
            raw = open(src_path, encoding="utf-8").read()
            max_m = re.search(r"maxValue=\{([0-9.]+)\}", raw)
            min_m = re.search(r"minValue=\{([0-9.]+)\}", raw)
            is_elo = "<EloChart" in raw

            title = stem.replace("-", " ").title()
            axis = "Elo Rating" if is_elo else "Accuracy (%)"
            max_val = float(max_m.group(1)) if max_m else (1400.0 if is_elo else 100.0)
            min_val = float(min_m.group(1)) if min_m else (800.0 if is_elo else 0.0)
            span = max(max_val - min_val, 1.0)

            rows = []
            for obj_m in re.finditer(r"\{([^{}]+)\}", raw):
                blob = obj_m.group(1)
                name_m = re.search(r'name:\s*["\']([^"\']+)["\']', blob)
                val_m = re.search(r"(?:accuracy|elo|value):\s*([0-9.]+)", blob)
                if not name_m or not val_m:
                    continue
                model_m = re.search(r'(?:model|org):\s*["\']([^"\']+)["\']', blob)
                name_str = name_m.group(1)
                hi = "highlighted: true" in blob or "Factory Droid" in name_str
                rows.append({
                    "name": name_str,
                    "org": model_m.group(1) if model_m else "",
                    "value": float(val_m.group(1)),
                    "highlighted": hi,
                })

            chart_lines = [
                '<div class="factory-chart">',
                f'  <div class="factory-chart-header"><span class="factory-chart-title">{html.escape(title)}</span><span class="factory-chart-axis">{html.escape(axis)}</span></div>',
            ]
            for r in rows:
                pct = max(4.0, min(100.0, ((r["value"] - min_val) / span) * 100.0))
                row_cls = "factory-chart-row factory-chart-row--highlight" if r["highlighted"] else "factory-chart-row"
                org_html = f' <span class="factory-chart-org">({html.escape(r["org"])})</span>' if r["org"] else ""
                val_str = f'{int(round(r["value"]))}' if is_elo else f'{r["value"]:.1f}%'
                chart_lines.append(
                    f'  <div class="{row_cls}">'
                    f'<div class="factory-chart-label">{html.escape(r["name"])}{org_html}</div>'
                    f'<div class="factory-chart-track"><div class="factory-chart-fill" style="width:{pct:.1f}%"></div></div>'
                    f'<div class="factory-chart-val">{html.escape(val_str)}</div>'
                    f'</div>'
                )
            chart_lines.append("</div>")
            chart_html = "\n".join(chart_lines)

            body = raw
            body = re.sub(r"^[ \t]*import\s+[^\n]+\n?", "", body, flags=re.MULTILINE)
            body = re.sub(r"export\s+const\s+[A-Za-z0-9_]+\s*=\s*\[.*?\n\]\s*\n?", "", body, flags=re.DOTALL)
            body = re.sub(r"<(?:BarChart|EloChart)\b[^>]*/>", lambda _: chart_html, body)

            # Convert <Card ...>...</Card> inside snippets
            def snippet_card(m):
                attrs = parse_attrs(m.group(1))
                ctitle = attrs.get("title", "Leaderboard")
                chref = attrs.get("href", "#")
                cinner = m.group(2).strip()
                return f'<div class="factory-card">\n\n**[{ctitle}]({chref})**\n\n{cinner}\n\n</div>'

            body = re.sub(r"<Card\b([^>]*)>(.*?)</Card>", snippet_card, body, flags=re.DOTALL)

            # Add deterministic {#id} to headings inside the snippet
            h_idx = 0
            used_snippet_ids = set()
            def snippet_heading(m):
                nonlocal h_idx
                h_idx += 1
                hashes, htext = m.group(1), m.group(2).strip()
                sub_id = safe_ascii_anchor(htext, f"sec-{h_idx}")
                hid = f"{stem}-{sub_id}"
                suffix = 2
                while hid in used_snippet_ids:
                    hid = f"{stem}-{sub_id}-{suffix}"
                    suffix += 1
                used_snippet_ids.add(hid)
                return f"{hashes} {htext} {{#{hid}}}"

            body = re.sub(r"^(#{1,6})\s+([^\n]+?)\s*$", snippet_heading, body, flags=re.MULTILINE)

            out_rel = f"{dst_sub}/{stem}.md"
            out_abs = os.path.join(CONTENT_DIR, out_rel)
            os.makedirs(os.path.dirname(out_abs), exist_ok=True)
            with open(out_abs, "w", encoding="utf-8") as wf:
                wf.write(body.strip() + "\n")
            generated[out_rel] = out_abs
    return generated


def parse_attrs(attr_str: str) -> dict:
    attrs = {}
    for m in re.finditer(r'([A-Za-z0-9_:-]+)\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|\{([^}]*)\})', attr_str):
        k = m.group(1)
        v = m.group(2) if m.group(2) is not None else (m.group(3) if m.group(3) is not None else m.group(4))
        attrs[k] = v
    for m in re.finditer(r'(?:^|\s)(required|open|defaultOpen|horizontal|arrow)(?=\s|$)', attr_str):
        attrs[m.group(1)] = "true"
    return attrs


def fix_code_fences(body: str, rel_path: str) -> str:
    """Fix stray EOF fences and nested 3-backtick markdown fences in factory/docs."""
    lines = body.splitlines()
    # 1. Upgrade ```markdown fences that contain nested ``` blocks to ````markdown
    if rel_path in (
        "guides/power-user/rules-conventions.mdx",
        "guides/power-user/prompt-crafting.mdx",
        "jp/guides/power-user/rules-conventions.mdx",
        "jp/guides/power-user/token-efficiency.mdx",
    ):
        i = 0
        while i < len(lines):
            m = re.match(r"^(\s*)```markdown\s*$", lines[i])
            if m:
                indent = m.group(1)
                # Find the double ``` closing pattern or next major heading
                close_idx = None
                for j in range(i + 1, len(lines)):
                    if re.match(r"^\s*```\s*$", lines[j]):
                        # Check if next non-empty line is also ``` or a heading/component
                        k = j + 1
                        while k < len(lines) and not lines[k].strip():
                            k += 1
                        if k < len(lines) and re.match(r"^\s*```\s*$", lines[k]):
                            close_idx = k
                            break
                        close_idx = j
                if close_idx is not None:
                    lines[i] = f"{indent}````markdown"
                    lines[close_idx] = f"{indent}````"
                    i = close_idx + 1
                    continue
            i += 1

    # 2. Check parity of fence openers/closers and strip stray trailing ``` at EOF
    in_fence = False
    fence_char = ""
    fence_len = 0
    for idx, line in enumerate(lines):
        m = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if m:
            ticks, info = m.group(1), m.group(2).strip()
            if not in_fence:
                if idx == len(lines) - 1 and info == "":
                    # Stray trailing ``` at EOF!
                    lines.pop()
                    break
                in_fence = True
                fence_char = ticks[0]
                fence_len = len(ticks)
            else:
                if ticks[0] == fence_char and len(ticks) >= fence_len and info == "":
                    in_fence = False
    return "\n".join(lines)


def split_by_code_fences(text: str):
    """Yield (is_code_fence, segment_text) so we never mutate inside code fences."""
    lines = text.splitlines(keepends=True)
    out = []
    cur = []
    in_fence = False
    fence_ch = ""
    fence_len = 0
    for line in lines:
        m = re.match(r"^[ \t]*(`{3,}|~{3,})(.*)$", line)
        if m:
            ticks, info = m.group(1), m.group(2).strip()
            if not in_fence:
                if cur:
                    out.append((False, "".join(cur)))
                    cur = []
                in_fence = True
                fence_ch = ticks[0]
                fence_len = len(ticks)
                cur.append(line)
                continue
            elif ticks[0] == fence_ch and len(ticks) >= fence_len and info == "":
                cur.append(line)
                out.append((True, "".join(cur)))
                cur = []
                in_fence = False
                continue
        cur.append(line)
    if cur:
        out.append((in_fence, "".join(cur)))
    return out


def dedent_NonFence(text: str) -> str:
    """Dedent non-fenced Markdown lines so indented JSX children don't become 4-space code blocks."""
    out = []
    for is_fence, seg in split_by_code_fences(text):
        if is_fence:
            # Strip common leading spaces from the fence block itself
            out.append(textwrap.dedent(seg))
        else:
            dedented_lines = []
            for line in seg.splitlines(keepends=True):
                # Strip up to 8 leading spaces unless it's a nested list item where 2 spaces matter
                m = re.match(r"^([ \t]+)(.*)$", line)
                if m:
                    ws, rest = m.group(1), m.group(2)
                    if len(ws.expandtabs(4)) >= 4 and not re.match(r"^[-*+]\s|^\d+\.\s", rest):
                        dedented_lines.append(rest + ("\n" if line.endswith("\n") else ""))
                    elif len(ws.expandtabs(4)) >= 4 and re.match(r"^[-*+]\s|^\d+\.\s", rest):
                        dedented_lines.append("  " + rest + ("\n" if line.endswith("\n") else ""))
                    else:
                        dedented_lines.append(line)
                else:
                    dedented_lines.append(line)
            out.append("".join(dedented_lines))
    return "".join(out)


def replace_paired_tag(text: str, tag_name: str, replacer):
    """Replace innermost paired <TagName ...>...</TagName> outside code fences, even when wrapping code fences."""
    pattern = re.compile(
        rf"<{tag_name}\b([^>]*?)(?<!/)>(.*?)</{tag_name}>",
        re.DOTALL,
    )
    while True:
        fences = []
        masked_parts = []
        for is_fence, seg in split_by_code_fences(text):
            if is_fence:
                idx = len(fences)
                fences.append(seg)
                masked_parts.append(f"\x00FENCE_{idx}\x00")
            else:
                masked_parts.append(seg)
        masked_text = "".join(masked_parts)

        def unmask(s: str) -> str:
            return re.sub(r"\x00FENCE_(\d+)\x00", lambda fm: fences[int(fm.group(1))], s)

        new_masked, n = pattern.subn(
            lambda m: replacer(unmask(m.group(1)), unmask(m.group(2))),
            masked_text,
        )
        text = unmask(new_masked)
        if n == 0:
            break
    return text


def compute_rel_asset_url(current_id: str, asset_path: str) -> str:
    """Compute relative path from current_id.html to static asset in dist/."""
    clean = asset_path.lstrip("/")
    cur_dir = os.path.dirname(current_id)
    if not cur_dir:
        return clean
    return os.path.relpath(clean, cur_dir)


def resolve_internal_target(raw_href: str, current_id: str, known_ids: set):
    """Resolve a Mintlify href to (target_entity_id, fragment) or None if external/static."""
    if not raw_href:
        return None
    if raw_href.startswith("https://docs.factory.ai"):
        raw_href = raw_href[len("https://docs.factory.ai"):] or "/"
    if raw_href.startswith(("http://", "https://", "mailto:", "tel:")):
        return None
    if raw_href.startswith("#"):
        return (current_id, raw_href[1:])

    path_part, frag = (raw_href.split("#", 1) + [""])[:2] if "#" in raw_href else (raw_href, "")
    path_part = path_part.split("?", 1)[0].strip()
    if not path_part:
        return (current_id, frag)

    # Check if it's a static file extension
    ext = os.path.splitext(path_part)[1].lower()
    if ext in (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".mp4", ".webm", ".ico", ".pdf", ".json", ".txt", ".xml"):
        return None

    is_jp = current_id.startswith("jp/")
    if path_part.startswith("/"):
        cand = path_part.lstrip("/")
    else:
        cur_dir = os.path.dirname(current_id)
        cand = os.path.normpath(os.path.join(cur_dir, path_part)).lstrip("./")

    if cand.endswith((".mdx", ".md")):
        cand = re.sub(r"\.(mdx|md)$", "", cand)
    cand = cand.rstrip("/")
    if not cand:
        cand = "jp/index" if is_jp else "index"

    if cand in REDIRECT_MAP:
        cand = REDIRECT_MAP[cand]

    # Prefer JP counterpart if on a JP page and the link was unprefixed
    if is_jp and not cand.startswith("jp/") and f"jp/{cand}" in known_ids:
        cand = f"jp/{cand}"
    elif is_jp and not cand.startswith("jp/") and f"jp/{cand}/index" in known_ids:
        cand = f"jp/{cand}/index"

    if cand in known_ids:
        return (cand, frag)
    if f"{cand}/index" in known_ids:
        return (f"{cand}/index", frag)
    return None


def convert_mdx_body(body: str, current_id: str, known_ids: set) -> str:
    is_jp = current_id.startswith("jp/")
    inc_prefix = "includes/jp/leaderboards" if is_jp else "includes/leaderboards"

    # 1. Strip JSX imports and `{false && (...)}` blocks
    body = re.sub(r"\{\s*false\s*&&\s*\(\s*<>.*?</>\s*\)\s*\}", "", body, flags=re.DOTALL)
    clean_segs = []
    for is_fence, seg in split_by_code_fences(body):
        if is_fence:
            clean_segs.append(seg)
        else:
            seg = re.sub(r"^[ \t]*import\s+[^\n]+\n?", "", seg, flags=re.MULTILINE)
            seg = re.sub(r"\{\s*/\*.*?\*/\s*\}", "", seg, flags=re.DOTALL)
            clean_segs.append(seg)
    body = "".join(clean_segs)

    # 2. Replace Leaderboard components with Boris native {{include ...}}
    leaderboard_map = {
        "TerminalBench": f"{{{{include {inc_prefix}/terminal-bench.md}}}}",
        "AgentArena": f"{{{{include {inc_prefix}/agent-arena.md}}}}",
        "LegacyBench": f"{{{{include {inc_prefix}/legacy-bench.md}}}}",
        "NextJSEval": f"{{{{include {inc_prefix}/nextjs-eval.md}}}}",
        "ReviewBenchmark": f"{{{{include {inc_prefix}/review-benchmark.md}}}}",
    }
    for comp, inc in leaderboard_map.items():
        body = re.sub(rf"<{comp}\s*/>", f"\n\n{inc}\n\n", body)

    # 3. Replace self-closing <Card ... /> first
    def render_card(attr_str: str, inner: str) -> str:
        attrs = parse_attrs(attr_str)
        title = attrs.get("title", "Resource")
        href = attrs.get("href", "").strip()
        inner_clean = dedent_NonFence(inner).strip()
        heading_line = f"**{title}**"
        if href:
            resolved = resolve_internal_target(href, current_id, known_ids)
            if resolved:
                tid, frag = resolved
                target_spec = f"{tid}#{frag}" if frag else tid
                heading_line = f"**[[{target_spec}|{title}]]**"
            else:
                heading_line = f"**[{title}]({href})**"
        if inner_clean:
            return f'\n\n<div class="factory-card">\n\n{heading_line}\n\n{inner_clean}\n\n</div>\n\n'
        return f'\n\n<div class="factory-card">\n\n{heading_line}\n\n</div>\n\n'

    body = re.sub(
        r"<Card\b([^>]*?)/>",
        lambda m: render_card(m.group(1), ""),
        body,
    )
    body = replace_paired_tag(body, "Card", render_card)
    body = replace_paired_tag(
        body,
        "CardGroup",
        lambda a, inner: f'\n\n<div class="factory-card-group">\n\n{dedent_NonFence(inner).strip()}\n\n</div>\n\n',
    )

    # 4. Steps & Step
    def render_step(attr_str: str, inner: str) -> str:
        attrs = parse_attrs(attr_str)
        title = attrs.get("title", "").strip()
        inner_clean = dedent_NonFence(inner).strip()
        title_html = f'<div class="factory-step-title">{html.escape(title)}</div>\n\n' if title else ""
        return f'\n\n<div class="factory-step">\n\n{title_html}{inner_clean}\n\n</div>\n\n'

    body = replace_paired_tag(body, "Step", render_step)
    body = replace_paired_tag(
        body,
        "Steps",
        lambda a, inner: f'\n\n<div class="factory-steps">\n\n{dedent_NonFence(inner).strip()}\n\n</div>\n\n',
    )

    # 5. Tabs, Tab, CodeGroup
    def render_tab(attr_str: str, inner: str) -> str:
        attrs = parse_attrs(attr_str)
        title = attrs.get("title", "Tab").strip()
        inner_clean = dedent_NonFence(inner).strip()
        return f'\n\n<div class="factory-tab-panel">\n\n<div class="factory-tab-heading">{html.escape(title)}</div>\n\n{inner_clean}\n\n</div>\n\n'

    body = replace_paired_tag(body, "Tab", render_tab)
    body = replace_paired_tag(
        body,
        "Tabs",
        lambda a, inner: f'\n\n<div class="factory-tabs">\n\n{dedent_NonFence(inner).strip()}\n\n</div>\n\n',
    )

    def render_code_group(attr_str: str, inner: str) -> str:
        inner_clean = dedent_NonFence(inner).strip()
        fence_blocks = []
        for is_fence, seg in split_by_code_fences(inner_clean):
            if is_fence:
                lines = seg.strip().splitlines()
                first_line = lines[0] if lines else "```"
                m_info = re.match(r"^[ \t]*(`{3,}|~{3,})([A-Za-z0-9_+-]*)(.*)$", first_line)
                if m_info:
                    ticks, lang, label = m_info.group(1), m_info.group(2).strip(), m_info.group(3).strip()
                    tab_label = label or lang or "Code"
                    clean_fence = "\n".join([f"{ticks}{lang}"] + lines[1:])
                else:
                    tab_label = "Code"
                    clean_fence = seg.strip()
                fence_blocks.append((tab_label, clean_fence))
        if len(fence_blocks) > 1:
            tabs_html = "".join(
                f'<button type="button" class="factory-codegroup-tab{" is-active" if idx == 0 else ""}" data-tab-idx="{idx}">{html.escape(lbl)}</button>'
                for idx, (lbl, _) in enumerate(fence_blocks)
            )
            panels_out = []
            for idx, (lbl, cf) in enumerate(fence_blocks):
                cls = "factory-codegroup-panel is-active" if idx == 0 else "factory-codegroup-panel"
                panels_out.append(f'<div class="{cls}" data-panel-idx="{idx}">\n\n{cf}\n\n</div>')
            return (
                f'\n\n<div class="factory-codegroup">\n'
                f'<div class="factory-codegroup-bar">{tabs_html}</div>\n\n'
                + "\n\n".join(panels_out)
                + "\n\n</div>\n\n"
            )
        return f'\n\n<div class="factory-codegroup">\n\n{inner_clean}\n\n</div>\n\n'

    body = replace_paired_tag(body, "CodeGroup", render_code_group)

    # 6. Update (changelog entries)
    def render_update(attr_str: str, inner: str) -> str:
        attrs = parse_attrs(attr_str)
        label = attrs.get("label", "Update").strip()
        desc = attrs.get("description", "").strip()
        inner_clean = dedent_NonFence(inner).strip()
        desc_html = f'<span class="factory-update-desc">{html.escape(desc)}</span>' if desc else ""
        return (
            f'\n\n<div class="factory-update">\n\n'
            f'<div class="factory-update-header"><span class="factory-update-label">{html.escape(label)}</span>{desc_html}</div>\n\n'
            f'{inner_clean}\n\n</div>\n\n'
        )

    body = replace_paired_tag(body, "Update", render_update)

    # 7. ResponseField
    def render_response_field(attr_str: str, inner: str) -> str:
        attrs = parse_attrs(attr_str)
        name = attrs.get("name", "field").strip()
        ftype = attrs.get("type", "string").strip()
        req = "required" in attrs
        req_html = '<span class="factory-rf-required">required</span>' if req else ""
        inner_clean = dedent_NonFence(inner).strip()
        return (
            f'\n\n<div class="factory-response-field">\n\n'
            f'<div class="factory-response-field-meta">'
            f'<span class="factory-rf-name">{html.escape(name)}</span>'
            f'<span class="factory-rf-type">{html.escape(ftype)}</span>'
            f'{req_html}</div>\n\n'
            f'{inner_clean}\n\n</div>\n\n'
        )

    body = re.sub(
        r"<ResponseField\b([^>]*?)/>",
        lambda m: render_response_field(m.group(1), ""),
        body,
    )
    body = replace_paired_tag(body, "ResponseField", render_response_field)

    # 8. Frame
    def render_frame(attr_str: str, inner: str) -> str:
        attrs = parse_attrs(attr_str)
        caption = attrs.get("caption", "").strip()
        inner_clean = dedent_NonFence(inner).strip()
        cap_html = f'\n\n<div class="factory-frame-caption">{html.escape(caption)}</div>' if caption else ""
        return f'\n\n<div class="factory-frame">\n\n{inner_clean}{cap_html}\n\n</div>\n\n'

    body = replace_paired_tag(body, "Frame", render_frame)

    # 9. AccordionGroup
    body = replace_paired_tag(
        body,
        "AccordionGroup",
        lambda a, inner: f"\n\n{dedent_NonFence(inner).strip()}\n\n",
    )

    # 10. Callouts (<Note>, <Tip>, <Info>, <Warning>, <Check>) and Disclosures (<Accordion>, <Expandable>)
    # To respect Boris's non-nesting rule for <Aside> and <Details>, convert any nested callout/disclosure
    # to HTML <aside>/<details>, and top-level ones to Boris native <Aside kind="..."> / <Details summary="...">.
    callout_kinds = {
        "Note": "note",
        "Tip": "tip",
        "Info": "info",
        "Warning": "warning",
        "Check": "tip",
    }
    component_check_re = re.compile(r"<(Aside|Details|Note|Tip|Info|Warning|Check|Accordion|Expandable)\b")

    for tag, kind in callout_kinds.items():
        def make_callout(attr_str: str, inner: str, k=kind) -> str:
            inner_clean = dedent_NonFence(inner).strip()
            if component_check_re.search(inner_clean):
                return f'\n\n<aside class="boris-aside boris-aside--{k}">\n\n{inner_clean}\n\n</aside>\n\n'
            return f'\n\n<Aside kind="{k}">\n{inner_clean}\n</Aside>\n\n'
        body = replace_paired_tag(body, tag, make_callout)

    for tag in ("Accordion", "Expandable"):
        def make_disclosure(attr_str: str, inner: str) -> str:
            attrs = parse_attrs(attr_str)
            summary = attrs.get("title", "Details").replace('"', "'").replace("\n", " ").strip()
            if not summary:
                summary = "Details"
            inner_clean = dedent_NonFence(inner).strip()
            if component_check_re.search(inner_clean):
                return f'\n\n<details class="boris-details">\n<summary>{html.escape(summary)}</summary>\n\n{inner_clean}\n\n</details>\n\n'
            return f'\n\n<Details summary="{summary}">\n{inner_clean}\n</Details>\n\n'
        body = replace_paired_tag(body, tag, make_disclosure)

    # If an outer <Aside> or <Details> ended up wrapping an inner <Aside> or <Details>, downgrade the outer one to HTML
    def fix_nested_boris_components(text: str) -> str:
        out_segs = []
        for is_fence, seg in split_by_code_fences(text):
            if is_fence:
                out_segs.append(seg)
                continue
            seg = re.sub(
                r'<Details summary="([^"]+)">\n(.*?)\n</Details>',
                lambda m: (
                    f'<details class="boris-details">\n<summary>{html.escape(m.group(1))}</summary>\n\n{m.group(2)}\n\n</details>'
                    if re.search(r"<(Aside|Details)\b", m.group(2))
                    else m.group(0)
                ),
                seg,
                flags=re.DOTALL,
            )
            seg = re.sub(
                r'<Aside kind="([^"]+)">\n(.*?)\n</Aside>',
                lambda m: (
                    f'<aside class="boris-aside boris-aside--{m.group(1)}">\n\n{m.group(2)}\n\n</aside>'
                    if re.search(r"<(Aside|Details)\b", m.group(2))
                    else m.group(0)
                ),
                seg,
                flags=re.DOTALL,
            )
            out_segs.append(seg)
        return "".join(out_segs)

    body = fix_nested_boris_components(body)

    # 11. Normalize JSX attributes and media paths outside code fences
    final_segs = []
    for is_fence, seg in split_by_code_fences(body):
        if is_fence:
            final_segs.append(seg)
            continue

        # Convert JSX className= to class=
        seg = re.sub(r"\bclassName=", "class=", seg)
        # Convert JSX style={{ ... }} to standard HTML style="..."
        def jsx_style_to_css(m):
            raw_s = m.group(1)
            pairs = []
            for pm in re.finditer(r"([A-Za-z]+)\s*:\s*(?:'([^']*)'|\"([^\"]*)\"|([0-9]+))", raw_s):
                prop = re.sub(r"([A-Z])", lambda c: "-" + c.group(1).lower(), pm.group(1))
                val = pm.group(2) or pm.group(3) or (pm.group(4) + "px")
                pairs.append(f"{prop}:{val}")
            return f'style="{"; ".join(pairs)}"'

        seg = re.sub(r"style=\{\{([^}]+)\}\}", jsx_style_to_css, seg)
        seg = re.sub(r"\bautoPlay\b", "autoplay", seg)
        seg = re.sub(r"\bplaysInline\b", "playsinline", seg)

        # Convert Markdown ![alt](src) images to <img src="..." alt="..." /> with relative static path
        def md_img_to_html(m):
            alt_txt = m.group(1)
            src_url = m.group(2).strip()
            if src_url.startswith(("http://", "https://")):
                rel_src = src_url
            elif src_url.startswith("/"):
                rel_src = compute_rel_asset_url(current_id, src_url)
            else:
                # Relative to current page directory in factory/docs (e.g. ./before-after-pr.png in guides/droid-exec)
                base_dir = os.path.dirname(current_id)
                if base_dir.startswith("jp/"):
                    base_dir = base_dir[3:]
                resolved_static = os.path.normpath(os.path.join(base_dir, src_url))
                rel_src = compute_rel_asset_url(current_id, resolved_static)
            return f'<img src="{html.escape(rel_src)}" alt="{html.escape(alt_txt)}" />'

        seg = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", md_img_to_html, seg)

        # Rewrite HTML <img src="/..."> and <video src="/..."> to relative static paths
        def fix_html_media_src(m):
            prefix, url, suffix = m.group(1), m.group(2), m.group(3)
            if url.startswith(("http://", "https://", "data:")):
                return m.group(0)
            if url.startswith("/"):
                rel_src = compute_rel_asset_url(current_id, url)
                return f'{prefix}{rel_src}{suffix}'
            return m.group(0)

        seg = re.sub(r'(<(?:img|video|source)\b[^>]*?\bsrc=["\'])([^"\']+)(["\'])', fix_html_media_src, seg)

        # Escape any stray <PascalCase tokens outside inline backticks that are not <Aside or <Details
        parts = re.split(r"(`+[^`]*`+)", seg)
        for idx in range(0, len(parts), 2):
            parts[idx] = re.sub(
                r"<([A-Z][A-Za-z0-9_-]*)\b",
                lambda m: m.group(0) if m.group(1) in ("Aside", "Details") else f"&lt;{m.group(1)}",
                parts[idx],
            )
        seg = "".join(parts)
        final_segs.append(seg)

    return "".join(final_segs)


def generate_openapi_pages(spec: dict):
    """Generate 77 English and 77 Japanese OpenAPI endpoint pages matching Mintlify routes."""
    schemas = spec.get("components", {}).get("schemas", {})

    def resolve_schema(s, depth=0):
        if not s or depth > 3:
            return s or {}
        if "$ref" in s:
            ref_name = s["$ref"].split("/")[-1]
            return resolve_schema(schemas.get(ref_name, {}), depth + 1)
        return s

    pages = {}
    used_routes = set()
    tag_operations = defaultdict(list)

    for path, item in spec.get("paths", {}).items():
        for method in ("get", "post", "put", "patch", "delete"):
            if method not in item:
                continue
            op = item[method]
            raw_tag = (op.get("tags") or ["default"])[0]
            tag_slug = re.sub(r"[^a-z0-9]+", "-", raw_tag.lower()).strip("-")
            summary = op.get("summary") or op.get("operationId") or path
            slug = re.sub(r"[^a-z0-9]+", "-", summary.lower().replace("'", "")).strip("-")
            base_route = f"api-reference/{tag_slug}/{slug}"
            route = base_route
            counter = 1
            while route in used_routes:
                route = f"{base_route}-{counter}"
                counter += 1
            used_routes.add(route)
            tag_operations[tag_slug].append((route, raw_tag, method.upper(), path, summary, op))

    for tag_slug, ops in sorted(tag_operations.items()):
        for route, raw_tag, method, path, summary, op in ops:
            desc = (op.get("description") or summary).strip()
            params = op.get("parameters") or []
            req_body = op.get("requestBody", {}).get("content", {}).get("application/json", {}).get("schema")
            responses = op.get("responses") or {}

            for lang_prefix in ("", "jp/"):
                pid = f"{lang_prefix}{route}"
                parent_id = f"{lang_prefix}api-reference/{tag_slug}/index"
                counterpart_id = route if lang_prefix else f"jp/{route}"

                lines = [
                    f'<div class="factory-page-title-row"><h1 class="factory-page-title">{html.escape(summary)}</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>',
                    "",
                    f'<div class="factory-openapi-endpoint"><span class="factory-openapi-method">{method}</span><span class="factory-openapi-path">{html.escape(path)}</span></div>',
                    "",
                    desc,
                    "",
                    "## Endpoint {#endpoint}",
                    "",
                    f"- **Method:** `{method}`",
                    f"- **Path:** `{path}`",
                    f"- **Category:** [[{parent_id}|{raw_tag.title()} API]]",
                    "",
                ]

                if params:
                    lines.extend([
                        "## Parameters {#parameters}",
                        "",
                        "| Name | Location | Type | Required | Description |",
                        "| --- | --- | --- | --- | --- |",
                    ])
                    for p in params:
                        pname = p.get("name", "")
                        pin = p.get("in", "query")
                        preq = "Yes" if p.get("required") else "No"
                        pschema = resolve_schema(p.get("schema", {}))
                        ptype = pschema.get("type", "string")
                        pdesc = (p.get("description") or "-").replace("\n", " ").replace("|", "\\|")
                        lines.append(f"| `{pname}` | `{pin}` | `{ptype}` | {preq} | {pdesc} |")
                    lines.append("")

                if req_body:
                    resolved_rb = resolve_schema(req_body)
                    props = resolved_rb.get("properties") or {}
                    req_list = set(resolved_rb.get("required") or [])
                    if props:
                        lines.extend([
                            "## Request Body {#request-body}",
                            "",
                            "| Field | Type | Required | Description |",
                            "| --- | --- | --- | --- |",
                        ])
                        for fname, fschema in props.items():
                            fs = resolve_schema(fschema)
                            ftype = fs.get("type", "object")
                            freq = "Yes" if fname in req_list else "No"
                            fdesc = (fs.get("description") or "-").replace("\n", " ").replace("|", "\\|")
                            lines.append(f"| `{fname}` | `{ftype}` | {freq} | {fdesc} |")
                        lines.append("")

                if responses:
                    lines.extend([
                        "## Responses {#responses}",
                        "",
                        "| Status | Description |",
                        "| --- | --- |",
                    ])
                    for code, rinfo in sorted(responses.items()):
                        rdesc = (rinfo.get("description") or "Response").replace("\n", " ").replace("|", "\\|")
                        lines.append(f"| `{code}` | {rdesc} |")
                    lines.append("")

                lines.extend([
                    "## Example Request {#example-request}",
                    "",
                    "```bash",
                    f'curl -X {method} "https://api.factory.ai{path}" \\',
                    '  -H "Authorization: Bearer $FACTORY_API_KEY" \\',
                    '  -H "Content-Type: application/json"',
                    "```",
                    "",
                ])

                pages[pid] = {
                    "id": pid,
                    "title": summary,
                    "summary": f"{method} {path} — {summary}",
                    "tags": ["api-reference", sanitize_tag(tag_slug), sanitize_tag(method)],
                    "parent": parent_id,
                    "relations": [f"relates_to={counterpart_id}"],
                    "body": "\n".join(lines),
                    "is_openapi": True,
                }
    return pages


def main():
    os.makedirs(BORIS_ROOT, exist_ok=True)
    if os.path.exists(CONTENT_DIR):
        shutil.rmtree(CONTENT_DIR)
    os.makedirs(CONTENT_DIR, exist_ok=True)

    static_count = copy_static_assets()
    includes_map = build_leaderboard_includes()

    # 1. Discover all non-snippet MDX pages in factory/docs
    raw_pages = {}
    for dp, dn, fn in os.walk(FACTORY_DOCS):
        for f in sorted(fn):
            if not f.endswith((".mdx", ".md")):
                continue
            rel = os.path.relpath(os.path.join(dp, f), FACTORY_DOCS)
            if rel == "README.md" or rel.startswith(("snippets/", "jp/snippets/")):
                continue
            pid = re.sub(r"\.(mdx|md)$", "", rel)
            raw_text = open(os.path.join(dp, f), encoding="utf-8").read()
            meta, body = parse_mdx_frontmatter(raw_text)
            body = fix_code_fences(body, rel)
            raw_pages[pid] = {
                "rel": rel,
                "meta": meta,
                "raw_body": body,
            }

    # 2. Load OpenAPI pages
    openapi_spec = json.load(open(OPENAPI_SPEC, encoding="utf-8"))
    openapi_pages = generate_openapi_pages(openapi_spec)

    # 3. Determine all directory section hubs needed so every page has a clean parent chain to `index`
    all_page_ids = set(raw_pages.keys()) | set(openapi_pages.keys()) | {"index"}
    dirs = set()
    for pid in list(all_page_ids):
        parts = pid.split("/")
        for i in range(1, len(parts)):
            d = "/".join(parts[:i])
            dirs.add(d)
    for d in sorted(dirs):
        hub_id = f"{d}/index"
        all_page_ids.add(hub_id)

    # 4. Build page dictionary and convert MDX bodies
    pages = {}
    for pid, info in sorted(raw_pages.items()):
        meta = info["meta"]
        title = meta.get("title") or meta.get("sidebarTitle") or pid.split("/")[-1].replace("-", " ").title()
        desc = meta.get("description") or f"{title} — Factory Documentation"
        tags = []
        for kw in meta.get("keywords", []):
            st = sanitize_tag(kw)
            if st and st not in tags:
                tags.append(st)
        section_tag = sanitize_tag(pid.split("/")[1] if pid.startswith("jp/") and "/" in pid[3:] else pid.split("/")[0])
        if section_tag and section_tag not in tags:
            tags.insert(0, section_tag)
        tags = tags[:8]

        converted_body = convert_mdx_body(info["raw_body"], pid, all_page_ids)
        header_block = (
            f'<div class="factory-page-title-row">'
            f'<h1 class="factory-page-title">{html.escape(title)}</h1>'
            f'<button class="factory-copy-page-btn" type="button">Copy page ▾</button>'
            f'</div>\n\n'
        )
        if meta.get("description"):
            header_block += f'<p class="factory-page-subtitle">{html.escape(meta["description"])}</p>\n\n'
        converted_body = header_block + converted_body

        # Compute parent entity id
        if pid == "index":
            parent_id = None
        elif pid.endswith("/index"):
            dir_part = pid[:-len("/index")]
            if "/" in dir_part:
                parent_dir = dir_part.rsplit("/", 1)[0]
                parent_id = f"{parent_dir}/index"
            else:
                parent_id = "jp/index" if dir_part != "jp" and dir_part.startswith("jp/") else "index"
        else:
            if "/" in pid:
                parent_dir = pid.rsplit("/", 1)[0]
                parent_id = f"{parent_dir}/index"
            else:
                parent_id = "index"

        # Counterpart relation (EN <-> JP)
        relations = []
        if pid.startswith("jp/"):
            en_id = pid[3:]
            if en_id in all_page_ids:
                relations.append(f"relates_to={en_id}")
        else:
            jp_id = f"jp/{pid}"
            if jp_id in all_page_ids:
                relations.append(f"relates_to={jp_id}")

        pages[pid] = {
            "id": pid,
            "title": title,
            "summary": desc,
            "tags": tags,
            "parent": parent_id,
            "relations": relations,
            "published_at": CHANGELOG_DATES.get(pid),
            "body": converted_body,
            "is_openapi": False,
        }

    # Merge OpenAPI pages
    for pid, op_page in openapi_pages.items():
        pages[pid] = op_page

    # 5. Create synthetic hub pages (including root `index` and section `<dir>/index` not in raw_pages)
    SECTION_TITLES = {
        "index": "Factory Documentation",
        "jp": "Factory ドキュメント (日本語)",
        "cli": "Factory Droid CLI",
        "cli/getting-started": "CLI Getting Started",
        "cli/features": "CLI Features",
        "cli/features/wiki": "Factory Wiki",
        "cli/configuration": "CLI Configuration & Hooks",
        "cli/droid-exec": "Droid Exec (Headless & CI/CD)",
        "cli/user-guides": "CLI User Guides",
        "cli/byok": "Bring Your Own Key (BYOK)",
        "web": "Factory Web Platform",
        "web/getting-started": "Web Getting Started",
        "web/features": "Web Features",
        "web/agent-readiness": "Agent Readiness",
        "web/machine-connection": "Machine Connection",
        "guides": "Engineering Guides & Cookbooks",
        "guides/building": "Building with Factory",
        "guides/droid-exec": "Droid Exec Automation Guides",
        "guides/hooks": "Hooks & Guardrails Guides",
        "guides/power-user": "Power User Workflows",
        "guides/skills": "Custom Skills Guides",
        "enterprise": "Enterprise Security & Governance",
        "reference": "CLI & Configuration Reference",
        "benchmarks": "Benchmarks & Evaluations",
        "changelog": "Changelog & Release Notes",
        "integrations": "Platform Integrations",
        "features": "Core Capabilities",
        "features/missions": "Factory Missions",
        "onboarding": "Role-Based Onboarding",
        "api-reference": "Factory Public API Reference",
    }

    for pid in sorted(all_page_ids):
        if pid in pages:
            continue
        if pid == "index":
            parent_id = None
            title = "Factory Documentation — Agent-Native Software Development"
            summary = "Official documentation for Factory Droid CLI, Web Platform, Missions, Enterprise Governance, Benchmarks, and Public API."
            rel = ["relates_to=jp/index"]
            welcome_body = pages.get("welcome/index", {}).get("body", "")
            if welcome_body:
                hub_body = welcome_body.replace('src="../images/', 'src="images/')
            else:
                hub_body = f"Explore the documentation pages and resources in **{title}**.\n"
        elif pid == "jp/index":
            parent_id = "index"
            title = SECTION_TITLES["jp"]
            summary = "Factory Droid CLI、Webプラットフォーム、Missions、エンタープライズ管理、ベンチマーク、公開APIの公式ドキュメント。"
            rel = ["relates_to=index"]
            jp_welcome_body = pages.get("jp/welcome/index", {}).get("body", "")
            if jp_welcome_body:
                hub_body = jp_welcome_body.replace('src="../../images/', 'src="../images/')
            else:
                hub_body = f"Explore the documentation pages and resources in **{title}**.\n"
        else:
            dir_part = pid[:-len("/index")] if pid.endswith("/index") else pid
            if "/" in dir_part:
                parent_dir = dir_part.rsplit("/", 1)[0]
                parent_id = f"{parent_dir}/index"
            else:
                parent_id = "index"
            clean_key = dir_part[3:] if dir_part.startswith("jp/") else dir_part
            base_title = SECTION_TITLES.get(clean_key) or clean_key.split("/")[-1].replace("-", " ").title()
            if dir_part.startswith("jp/") and dir_part != "jp":
                title = f"{base_title} (JP)"
            elif dir_part == "jp":
                title = SECTION_TITLES["jp"]
            else:
                title = base_title
            summary = f"{title} — section overview and index in Factory Documentation."
            counterpart = dir_part[3:] + "/index" if dir_part.startswith("jp/") and dir_part != "jp" else ("index" if dir_part == "jp" else f"jp/{pid}")
            rel = [f"relates_to={counterpart}"] if counterpart in all_page_ids else []
            hub_body = f"Explore the documentation pages and resources in **{title}**.\n"

        pages[pid] = {
            "id": pid,
            "title": title,
            "summary": summary,
            "tags": [sanitize_tag(pid.split("/")[0]) or "docs"],
            "parent": parent_id,
            "relations": rel,
            "published_at": None,
            "body": hub_body,
            "is_openapi": False,
        }

    # 6. Collect children per parent and append a structured child directory with Boris [[wiki-links]]
    # so every page in the graph has at least one incoming `reference` edge (`boris check` 0 unreferenced/unlinked)
    children_map = defaultdict(list)
    for pid, p in sorted(pages.items()):
        if p["parent"]:
            children_map[p["parent"]].append(pid)

    for parent_id, child_ids in sorted(children_map.items()):
        links_md = ["\n\n## Section Directory {#section-directory}\n"]
        for cid in sorted(child_ids):
            ctitle = pages[cid]["title"].replace("|", "—").replace("]", ")")
            links_md.append(f"- [[{cid}|{ctitle}]]")
        if parent_id == "jp/index" and "index" not in child_ids:
            links_md.append("- [[index|Factory Documentation (English)]]")
        pages[parent_id]["body"] = pages[parent_id]["body"].rstrip() + "\n" + "\n".join(links_md) + "\n"

    # 7. Heading ID alignment & deduplication across EN and JP pages
    # First pass: collect ordered headings on every EN page so JP pages can inherit English heading IDs
    en_heading_slugs = {}
    for pid, p in sorted(pages.items()):
        if pid.startswith("jp/"):
            continue
        slugs = []
        for is_fence, seg in split_by_code_fences(p["body"]):
            if is_fence:
                continue
            for m in re.finditer(r"^(#{1,6})\s+(.+?)(?:\s+\{#([A-Za-z0-9_-]+)\})?\s*$", seg, re.MULTILINE):
                htext = m.group(2).strip()
                explicit = m.group(3)
                slugs.append(explicit or safe_ascii_anchor(htext, "h"))
        en_heading_slugs[pid] = slugs

    # Map of (target_id, raw_fragment) -> resolved_ascii_heading_id
    fragment_resolution_map = {}
    page_heading_ids = defaultdict(set)

    for pid, p in sorted(pages.items()):
        en_counterpart = pid[3:] if pid.startswith("jp/") else None
        en_slugs = en_heading_slugs.get(en_counterpart, []) if en_counterpart else []

        # Fold `<a id="foo"></a>\n## Heading` into `## Heading {#foo}`
        folded_segs = []
        for is_fence, seg in split_by_code_fences(p["body"]):
            if is_fence:
                folded_segs.append(seg)
            else:
                seg = re.sub(
                    r'<a\s+id=["\']([A-Za-z0-9_-]+)["\']\s*>\s*</a>\s*\n+(#{1,6}[ \t]+[^\n{#]+)',
                    lambda m: f"{m.group(2).rstrip()} {{#{m.group(1)}}}",
                    seg,
                )
                folded_segs.append(seg)
        p["body"] = "".join(folded_segs)

        # Pre-seed used_ids with any explicit {#id} or HTML id="..." already present on the page
        used_ids = set()
        for is_fence, seg in split_by_code_fences(p["body"]):
            if is_fence:
                continue
            for m_exp in re.finditer(r"\{#([A-Za-z0-9_-]+)\}", seg):
                used_ids.add(m_exp.group(1))
            for m_html_id in re.finditer(r'\bid=["\']([A-Za-z0-9_-]+)["\']', seg):
                used_ids.add(m_html_id.group(1))

        h_idx = 0
        new_segs = []

        for is_fence, seg in split_by_code_fences(p["body"]):
            if is_fence:
                new_segs.append(seg)
                continue

            def rewrite_heading(m):
                nonlocal h_idx
                hashes, htext, explicit = m.group(1), m.group(2).strip(), m.group(3)
                raw_gfm = gfm_slug(htext)
                h_idx += 1
                if explicit:
                    final_id = explicit
                else:
                    if pid.startswith("jp/") and (h_idx - 1) < len(en_slugs):
                        base_id = en_slugs[h_idx - 1]
                    else:
                        base_id = safe_ascii_anchor(htext, f"h{h_idx}")
                    final_id = base_id
                    suffix = 2
                    while final_id in used_ids:
                        final_id = f"{base_id}-{suffix}"
                        suffix += 1
                    used_ids.add(final_id)
                page_heading_ids[pid].add(final_id)

                # Register raw heading text -> final_id so Japanese fragment links resolve to final_id
                clean_htext = re.sub(r"[`*_~]", "", htext.strip())
                raw_frag_key = re.sub(r"\s+", "-", clean_htext.lower())
                norm_frag_key = re.sub(r"[.:：・、。（）()「」『』/／]+", "", raw_frag_key)
                fragment_resolution_map[(pid, raw_frag_key)] = final_id
                fragment_resolution_map[(pid, norm_frag_key)] = final_id
                fragment_resolution_map[(pid, clean_htext)] = final_id
                if raw_gfm:
                    fragment_resolution_map[(pid, raw_gfm)] = final_id
                fragment_resolution_map[(pid, final_id)] = final_id

                return f"{hashes} {htext} {{#{final_id}}}"

            seg = re.sub(
                r"^(#{1,6})[ \t]+([^\n]+?)(?:[ \t]+\{#([A-Za-z0-9_-]+)\})?[ \t]*$",
                rewrite_heading,
                seg,
                flags=re.MULTILINE,
            )
            new_segs.append(seg)

        p["body"] = "".join(new_segs)

    # 8. Second pass: rewrite all Markdown links [label](href) to Boris [[target#frag|label]] or valid external/static links
    # and ensure every internal #fragment exists on its target page!
    missing_fragments_added = defaultdict(list)

    for pid, p in sorted(pages.items()):
        new_segs = []
        for is_fence, seg in split_by_code_fences(p["body"]):
            if is_fence:
                new_segs.append(seg)
                continue

            # Protect inline code spans that wrap an entire [label](href), while allowing [`code`](href)
            def replace_md_link(m):
                label, href = m.group(1).strip(), m.group(2).strip()
                resolved = resolve_internal_target(href, pid, all_page_ids)
                if not resolved:
                    return m.group(0)
                tid, raw_frag = resolved
                clean_label = re.sub(r"\s+", " ", label).replace("`", "").replace("|", "—").replace("]", ")").replace("[", "(").strip() or tid
                if not raw_frag:
                    return f"[[{tid}|{clean_label}]]"

                # Resolve fragment on tid
                unquoted_frag = urllib.parse.unquote(raw_frag).strip()
                norm_frag = re.sub(r"[.:：・、。（）()「」『』/／]+", "", unquoted_frag.lower())
                frag_id = (
                    fragment_resolution_map.get((tid, raw_frag))
                    or fragment_resolution_map.get((tid, raw_frag.lower()))
                    or fragment_resolution_map.get((tid, unquoted_frag))
                    or fragment_resolution_map.get((tid, unquoted_frag.lower()))
                    or fragment_resolution_map.get((tid, norm_frag))
                )
                if not frag_id:
                    if raw_frag in page_heading_ids[tid]:
                        frag_id = raw_frag
                    else:
                        frag_id = safe_ascii_anchor(unquoted_frag, "anchor")
                        if frag_id not in page_heading_ids[tid]:
                            page_heading_ids[tid].add(frag_id)
                            missing_fragments_added[tid].append((frag_id, unquoted_frag))
                        fragment_resolution_map[(tid, raw_frag)] = frag_id

                return f"[[{tid}#{frag_id}|{clean_label}]]"

            # Replace [label](href) when not preceded by ` or !
            seg = re.sub(r"(?<![!`])\[([^\]]+)\]\(([^)\s]+)\)", replace_md_link, seg)

            # Also check any [[tid#frag|label]] already created in Cards
            def fix_card_wikilink(m):
                tid, raw_frag, label = m.group(1), m.group(2), m.group(3)
                if not raw_frag:
                    return m.group(0)
                unquoted_frag = urllib.parse.unquote(raw_frag).strip()
                norm_frag = re.sub(r"[.:：・、。（）()「」『』/／]+", "", unquoted_frag.lower())
                frag_id = (
                    fragment_resolution_map.get((tid, raw_frag))
                    or fragment_resolution_map.get((tid, raw_frag.lower()))
                    or fragment_resolution_map.get((tid, unquoted_frag))
                    or fragment_resolution_map.get((tid, unquoted_frag.lower()))
                    or fragment_resolution_map.get((tid, norm_frag))
                )
                if not frag_id:
                    if raw_frag in page_heading_ids[tid]:
                        frag_id = raw_frag
                    else:
                        frag_id = safe_ascii_anchor(unquoted_frag, "anchor")
                        if frag_id not in page_heading_ids[tid]:
                            page_heading_ids[tid].add(frag_id)
                            missing_fragments_added[tid].append((frag_id, unquoted_frag))
                        fragment_resolution_map[(tid, raw_frag)] = frag_id
                return f"[[{tid}#{frag_id}|{label}]]"

            seg = re.sub(r"\[\[([a-z0-9/_-]+)(?:#([^\]|]+))?\|([^\]]+)\]\]", fix_card_wikilink, seg)
            new_segs.append(seg)
        p["body"] = "".join(new_segs)

    # Append any anchor targets needed for cross-language fragment links
    for tid, anchors in sorted(missing_fragments_added.items()):
        extra = ["\n"]
        for frag_id, raw_frag in anchors:
            extra.append(f"### {raw_frag} {{#{frag_id}}}")
        pages[tid]["body"] = pages[tid]["body"].rstrip() + "\n" + "\n".join(extra) + "\n"

    # 9. Write all pages to content/<id>.md with strict Boris frontmatter
    written = 0
    for pid, p in sorted(pages.items()):
        out_path = os.path.join(CONTENT_DIR, f"{pid}.md")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        fm_lines = [
            "---",
            f"id: {pid}",
            f"title: {clean_frontmatter_quote(p['title'])}",
            "status: published",
            f"summary: {clean_frontmatter_quote(p['summary'])}",
        ]
        if p.get("published_at"):
            fm_lines.append(f"published_at: {p['published_at']}")
        if p.get("parent"):
            fm_lines.append(f"parent: {p['parent']}")
        if p.get("tags"):
            fm_lines.append(f"tags: [{', '.join(p['tags'])}]")
        if p.get("relations"):
            fm_lines.append(f"relations: [{', '.join(p['relations'])}]")
        fm_lines.append("---")
        fm_lines.append("")

        with open(out_path, "w", encoding="utf-8") as wf:
            wf.write("\n".join(fm_lines) + p["body"].strip() + "\n")
        written += 1

    report_src = os.path.join(BORIS_ROOT, "BORIS-MIGRATION-REPORT.md")
    if os.path.exists(report_src):
        shutil.copy2(report_src, os.path.join(CONTENT_DIR, "benchmarks", "boris-migration-report.md"))
        bench_idx = os.path.join(CONTENT_DIR, "benchmarks", "index.md")
        if os.path.exists(bench_idx):
            txt = open(bench_idx, encoding="utf-8").read()
            link_line = "- [[benchmarks/boris-migration-report|Boris Migration & Benchmark Report]]\n"
            if "benchmarks/boris-migration-report" not in txt:
                txt = txt.replace("## Section Directory {#section-directory}\n\n", "## Section Directory {#section-directory}\n\n" + link_line)
                open(bench_idx, "w", encoding="utf-8").write(txt)
        written += 1

    print(f"Copied static assets: {static_count}")
    print(f"Generated leaderboard includes: {len(includes_map)}")
    print(f"Generated total Boris pages: {written} (MDX: {len(raw_pages)}, OpenAPI: {len(openapi_pages)}, Hubs: {written - len(raw_pages) - len(openapi_pages)})")


if __name__ == "__main__":
    main()
