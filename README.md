# Unofficial Factory Documentation — Boris Compiler Demo

> **Unofficial and independent.** This repository, site, and benchmark report
> are not affiliated with, endorsed by, sponsored by, or maintained by Factory,
> Factory AI, or the makers of Droid. This historical snapshot is not official
> documentation, pricing, or support. Names and marks belong to their respective
> owners. Use https://docs.factory.ai for current official information.

Complete conversion of [`factory-ai/factory/docs`](https://github.com/factory-ai/factory/tree/main/docs) from **Mintlify CLI (`mintlify@4.2.1059`)** to **Boris (`boris/0.9.0`)**, a graph-native publication compiler written in **Zig 0.17.0**.

**Published site:** https://drawmeanelephant.github.io/factory-docs-boris/

Pricing and support pages are intentionally excluded in both languages.
Every published page has static non-affiliation notices and `noindex, nofollow,
noarchive` metadata. `robots.txt` allows crawling so search engines can read those
directives; it does not block crawlers from seeing the `noindex` tags.
See [CLOUD-HANDOFF.md](CLOUD-HANDOFF.md) for the remaining fixes.

## Contents of This Repository

- `boris.json` — Boris publication profile (`github-pages` target, OpenGraph head defaults, `rss.xml`, `sitemap.xml`, `trunk.html` + `main.html` layout rules).
- `content/` — **485** validated pages and **10** raw chart includes, including English and Japanese documentation, API references, section hubs, and the migration report, excluding pricing and support.
- `themes/factory/` — Factory dark theme (`layouts/main.html`, `layouts/trunk.html`, `assets/css/factory.css`, `assets/js/factory.js`) matching Mintlify's 2-row top header, section-scoped sidebar, callout boxes, interactive code groups, and right TOC.
- `static/` — All copied static media assets (`images/`, diagrams, GIFs, MP4 videos).
- `screenshots/` — Side-by-side `1440×1080` visual comparison screenshots (`01-quickstart-compare.png` through `06-jp-quickstart-compare.png`) and full-page screenshots of the rendered migration & benchmark report (`07-boris-migration-report-part1.png` – `part3.png`).
- `convert_factory_to_boris.py` — Deterministic Python 3 transpiler that converts `factory/docs` MDX + `openapi.json` into `content/` in `2.13s`.
- `BORIS-MIGRATION-REPORT.md` — Full benchmark, VM hardware analysis, and architectural trade-off report.
- `llms.txt` — Generated LLM context index.

## Quickstart (Build, Validate, Proof Verify, & Serve)

With `boris` (`0.9.0`) on your `PATH`:

```bash
# Fetch the videos and GIFs stored in Git LFS after cloning
git lfs pull
python3 scripts/restore-media.py

# 1. Config & schema preflight (~98 ms)
boris check

# 2. Full corpus + Trunk-Satellite graph + link audit (~789 ms)
boris validate --profile boris.json

# 3. Compile all 490 HTML pages, search index, sitemap, and RSS (~2.18s cold / ~1.34s incremental)
boris build --profile boris.json --incremental -j 4

# 4. Run strict 0-error, 0-warning post-build proof check (~1.4 ms)
boris proof verify --html-dir dist --max-errors 0 --max-warnings 0 --block-code HTML_DUPLICATE_ID

# 5. Live preview server with instant browser reload
boris watch --profile boris.json --serve --port 4200
```

Do not rerun the converter over this tree until its input-validation/deletion
issue is fixed; see [CLOUD-HANDOFF.md](CLOUD-HANDOFF.md). The generated content is
already included and builds without the original Factory checkout.

## Theme Regression Tests

The theme consumes Boris's rendered search index directly, including page paths,
section headings, prose, and code. Search results stay in the current language.
Run the dependency-free client tests with Node.js 18 or later:

```bash
node --test tests/*.test.cjs
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/check-site-policy.py --html-dir dist
```

## GitHub Pages

`.github/workflows/pages.yml` runs tests, builds Boris **0.9.0** from pinned
commit `66efcfb586b4342fe69d5a51962cb6d201e4dfc2` with Zig **0.17.0**, compiles
this site, and enforces zero-error/zero-warning proof checks. It publishes only
verified site payloads, not compiler binaries, caches, or local review files.

Pushes to `main` deploy automatically. Pull requests run the same build checks
without deploying. Pages uses GitHub Actions and the default project URL; no
custom domain is configured. The build reads the Pages URL from GitHub and uses
it for canonical URLs, OpenGraph metadata, sitemap, and RSS.

For a local Pages-equivalent build:

```bash
python3 scripts/pages-profile.py --base-url https://drawmeanelephant.github.io/factory-docs-boris
boris build --profile .boris-pages-profile.json -j 4
python3 scripts/prepare-pages.py
```

## Benchmark Summary (2-Core / 4-vCPU KVM VM)

| Pipeline Stage | Mintlify `4.2.1059` | Boris `0.9.0` | Speedup | Boris Peak RSS |
| :--- | ---: | ---: | ---: | ---: |
| Config & Schema Preflight | `12.50s` | **98.0 ms** | **127.6x faster** | `11.3 MB` |
| Full Corpus + Broken-Link Audit | `26.48s – 30.65s` | **788.6 ms** | **33.6x – 38.9x faster** | `24.4 MB` |
| Cold Static HTML Build (`-j 4`) | `84.30s` (`402` HTML) | **2.179s** (`490` HTML) | **38.7x faster** | `158.7 MB` |
| Incremental Warm Build (`--incremental -j 4`) | `84.30s` | **1.337s** (`490` HTML) | **63.1x faster** | `104.2 MB` |
| Post-Build Proof Gate (`3/3 checks`) | N/A | **1.4 ms** | — | `11.3 MB` |

See [`BORIS-MIGRATION-REPORT.md`](BORIS-MIGRATION-REPORT.md) (or `/benchmarks/boris-migration-report.html` in the built site) for the full hardware disclosure, VM multithreading caveats, and architectural trade-offs.
