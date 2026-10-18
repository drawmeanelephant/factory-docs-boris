Benchmark from [Factory](https://www.factory.ai/news/legacy-bench) measuring AI agent performance on legacy engineering tasks across COBOL, Java 7, BASIC, C89, Fortran, and Assembly.

### Results — Overall Pass Rate {#legacy-bench-results-overall-pass-rate}
<div class="factory-chart">
  <div class="factory-chart-header"><span class="factory-chart-title">Legacy Bench</span><span class="factory-chart-axis">Accuracy (%)</span></div>
  <div class="factory-chart-row factory-chart-row--highlight"><div class="factory-chart-label">Factory Droid (GPT-5.3 Codex)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:42.5%"></div></div><div class="factory-chart-val">42.5%</div></div>
  <div class="factory-chart-row factory-chart-row--highlight"><div class="factory-chart-label">Factory Droid (GPT-5.4)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:40.7%"></div></div><div class="factory-chart-val">40.7%</div></div>
  <div class="factory-chart-row"><div class="factory-chart-label">Codex CLI (GPT-5.4)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:40.1%"></div></div><div class="factory-chart-val">40.1%</div></div>
  <div class="factory-chart-row"><div class="factory-chart-label">Codex CLI (GPT-5.3 Codex)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:39.4%"></div></div><div class="factory-chart-val">39.4%</div></div>
  <div class="factory-chart-row factory-chart-row--highlight"><div class="factory-chart-label">Factory Droid (Gemini 3.1 Pro)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:38.7%"></div></div><div class="factory-chart-val">38.7%</div></div>
  <div class="factory-chart-row"><div class="factory-chart-label">Gemini CLI (Gemini 3.1 Pro)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:36.0%"></div></div><div class="factory-chart-val">36.0%</div></div>
  <div class="factory-chart-row factory-chart-row--highlight"><div class="factory-chart-label">Factory Droid (Claude Opus 4.6)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:34.6%"></div></div><div class="factory-chart-val">34.6%</div></div>
  <div class="factory-chart-row"><div class="factory-chart-label">Claude Code (Claude Opus 4.6)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:33.0%"></div></div><div class="factory-chart-val">33.0%</div></div>
  <div class="factory-chart-row factory-chart-row--highlight"><div class="factory-chart-label">Factory Droid (GLM-5)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:32.2%"></div></div><div class="factory-chart-val">32.2%</div></div>
  <div class="factory-chart-row"><div class="factory-chart-label">Cursor (Composer 2)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:31.0%"></div></div><div class="factory-chart-val">31.0%</div></div>
  <div class="factory-chart-row factory-chart-row--highlight"><div class="factory-chart-label">Factory Droid (Gemini 3 Flash)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:27.2%"></div></div><div class="factory-chart-val">27.2%</div></div>
  <div class="factory-chart-row factory-chart-row--highlight"><div class="factory-chart-label">Factory Droid (Kimi K2.5)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:16.9%"></div></div><div class="factory-chart-val">16.9%</div></div>
</div>

*Last updated: April 2026*

### Methodology {#legacy-bench-methodology}
| Stage | Description |
|-------|-------------|
| **Task set** | Hundreds of tasks across six legacy language families, with ten representative open samples |
| **Task format** | Natural language instruction, containerized source environment, reference solution, and hidden verification tests |
| **Task types** | Bug fixing, implementation, migration, and other legacy engineering work |
| **Evaluation** | Harbor-compatible tasks requiring agents to understand the specification, produce working code, and pass verification |
| **Scoring** | Pass rate across hidden tests for 12 model-agent combinations |

### Benchmark Mix {#legacy-bench-benchmark-mix}
| Language | Share | Example domains |
|----------|-------|-----------------|
| **COBOL** | 46% | Financial settlement, payroll processing, insurance claims, telecom billing, VSAM file handling |
| **Java 7** | 32% | Enterprise middleware, CDR processing, warehouse logistics, binary parsing, EJB patterns |
| **BASIC** | 6% | Business applications, accounting, data processing |
| **C89** | 5% | Systems programming, low-level debugging, protocol implementation |
| **Fortran** | 5% | Scientific computing, numerical methods, physics simulation |
| **Assembly** | 5% | x86 firmware parsing, protocol decoding, hardware simulation |

Agents score highest on Java 7 bug fixing, where compiler and runtime feedback expose errors. COBOL remains hardest: 31 of the 44 tasks no model solved are COBOL.

<div class="factory-card">

**[Legacy-Bench](https://github.com/factory-ai/legacy-bench)**

View sample tasks and the evaluation harness on GitHub

</div>

<div class="factory-card">

**[Read the writeup](https://www.factory.ai/news/legacy-bench)**

Legacy-Bench: Can AI Agents Maintain the World's Most Critical Software?

</div>
