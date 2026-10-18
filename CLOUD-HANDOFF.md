# Cloud agent handoff

This repository contains a Boris 0.9.0 conversion of Factory documentation.
The public site is https://drawmeanelephant.github.io/factory-docs-boris/.
GitHub Actions builds and deploys pushes to `main`; pull requests build and
validate without deploying.

## First priority: theme contrast, not a redesign

Keep the existing layout and content. Correct paired foreground/background
colors in `themes/factory/assets/css/factory.css` for both light and dark modes:

- The dark header keeps near-black labels in light mode.
- Benchmark charts keep dark backgrounds but inherit dark labels.
- Callout bodies retain pale text on light backgrounds.
- Active sidebar links can become white-on-white.
- Code text is approximately 1.17:1 contrast in light mode.

Check the quickstart, migration report, and NextJS benchmark in both themes.
Normal-sized text should meet at least 4.5:1 contrast.

## Keep the working navigation and search

The theme now scopes sidebars by section and language. Language switching,
primary tabs, theme persistence, and Copy page have been browser-tested.
Search consumes Boris's real `path`, `title`, and `sections` index fields,
including prose and code, with locale-specific results and valid links.
Deployment-prefix handling supports the `/factory-docs-boris/` Pages path.

Run:

```bash
git lfs pull
python3 scripts/restore-media.py
node --test tests/*.test.cjs
python3 -m unittest discover -s tests -p 'test_*.py'
boris validate --profile boris.json
boris build --profile boris.json --incremental -j 4
boris proof verify --html-dir dist --max-errors 0 --max-warnings 0 --block-code HTML_DUPLICATE_ID
boris watch --profile boris.json --serve --port 4200
```

Use **Boris 0.9.0**, not 0.8.2. CI builds the exact pinned compiler source; no
compiler binary is committed.

## Separate remaining work

- At a 390 px viewport the fixed three-column grid leaves the article 0 px
  wide. Add a responsive navigation/TOC treatment.
- Japanese pages acquire `lang="ja"` in JavaScript, but raw templates still
  declare English.
- The converter's nested-component parsing, quoted `>` attributes, required
  curl inputs, response schemas, parameter descriptions, and positional
  Japanese anchors have verified defects. Treat API and anchor fidelity as
  follow-up correctness work, not CSS changes.

**Do not run `convert_factory_to_boris.py` against the delivered tree as-is.**
It deletes `content/` and `static/` before validating the source checkout.
Validate inputs first and generate into staging before attempting regeneration.

The benchmark report contains historical cloud measurements, not guaranteed
current numbers. Do not infer UI correctness from the three mechanical proof
checks.
