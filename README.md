# Awesome Coding Agent Sessions [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

A curated list of open-source tools that search, inspect, replay, export, migrate, analyze, or manage coding-agent sessions and transcripts.

The list focuses on the session data layer: what happens after coding agents write history to JSONL, SQLite, or another local store. It complements broader directories instead of cataloging coding agents themselves.

## Contents

- [Scope](#scope)
- [How to choose](#how-to-choose)
- [Comparison matrix](#comparison-matrix)
- [Projects](#projects)
  - [Discovery & Search](#discovery--search)
  - [Viewing & Replay](#viewing--replay)
  - [Export, Migration & Handoff](#export-migration--handoff)
  - [Session Management](#session-management)
  - [Analytics & Cost](#analytics--cost)
- [Related lists](#related-lists)
- [Contributing](#contributing)
- [License](#license)

## Scope

Included projects must directly read, write, index, transform, render, resume, or analyze coding-agent session, history, or transcript data.

This list intentionally excludes:

- General coding-agent directories and model comparisons.
- Orchestrators that launch agents but do not preserve or process session state.
- Generic LLM observability, memory, prompt, MCP, or context-engineering tools.
- Closed-source products and source-available repositories without an open-source license.
- Abandoned forks that add no distinct session capability.

## How to choose

Start with the workflow you need, then use supported agents and interface as hard filters:

- **Find past work:** Discovery & Search.
- **Read, audit, or demonstrate a run:** Viewing & Replay.
- **Move work between tools or machines:** Export, Migration & Handoff.
- **Control many live terminals:** Session Management.
- **Understand time, tokens, or cost:** Analytics & Cost.

Stars are shown as a live adoption signal, never as a quality score. A focused low-star tool can be a better fit than a popular general-purpose one.

<!-- catalog:start -->

## Comparison matrix

**Catalog:** 15 projects across 5 categories. Repository metadata was last checked on **2026-11-26**.

> Stars are live badges loaded from GitHub via Shields.io. They show adoption, not quality, and are never an inclusion threshold. Supported-agent and scope claims come from each project's documentation.

| Project | Category | Stars | Supported agents | Interface | Best for | License |
|---|---|---:|---|---|---|---|
| [Agent Deck](https://github.com/asheshgoplani/agent-deck) | Session Management | [![GitHub stars](https://img.shields.io/github/stars/asheshgoplani/agent-deck?style=flat&label=stars)](https://github.com/asheshgoplani/agent-deck/stargazers)<br><sub>1,308 on 2026-11-26</sub> | Claude Code<br>Codex<br>OpenCode<br>Gemini CLI<br>Other CLIs | TUI<br>Web | Developers coordinating many concurrent terminal-agent sessions across projects. | `MIT` |
| [Agent Session Resume](https://github.com/hacktivist123/agent-session-resume) | Export, Migration & Handoff | [![GitHub stars](https://img.shields.io/github/stars/hacktivist123/agent-session-resume?style=flat&label=stars)](https://github.com/hacktivist123/agent-session-resume/stargazers)<br><sub>243 on 2026-11-26</sub> | Claude Code<br>Codex<br>Cursor<br>Antigravity<br>OpenCode<br>Copilot | Agent skill<br>Python helpers | Cross-agent handoffs where the next agent must recover unfinished work safely. | `MIT` |
| [Agent Sessions](https://github.com/jazzyalex/agent-sessions) | Discovery & Search | [![GitHub stars](https://img.shields.io/github/stars/jazzyalex/agent-sessions?style=flat&label=stars)](https://github.com/jazzyalex/agent-sessions/stargazers)<br><sub>953 on 2026-11-26</sub> | Claude Code<br>Codex<br>OpenCode<br>Cursor<br>Copilot CLI<br>Pi<br>Kimi Code<br>Other | macOS app | Developers who want one local visual history across many coding agents. | `MIT` |
| [CCManager](https://github.com/kbwo/ccmanager) | Session Management | [![GitHub stars](https://img.shields.io/github/stars/kbwo/ccmanager?style=flat&label=stars)](https://github.com/kbwo/ccmanager/stargazers)<br><sub>1,281 on 2026-11-26</sub> | Claude Code<br>Codex<br>Gemini CLI<br>Cursor<br>Copilot CLI<br>Cline<br>OpenCode<br>Kimi CLI | TUI | Developers who want worktree-aware multi-agent session control in one terminal UI. | `MIT` |
| [ccusage](https://github.com/ccusage/ccusage) | Analytics & Cost | [![GitHub stars](https://img.shields.io/github/stars/ccusage/ccusage?style=flat&label=stars)](https://github.com/ccusage/ccusage/stargazers)<br><sub>19,597 on 2026-11-26</sub> | Claude Code<br>Codex<br>OpenCode<br>Gemini CLI<br>Copilot CLI<br>Kimi<br>Other | CLI | Teams or individuals comparing local token usage and cost across many agent CLIs. | `MIT` |
| [Claude Code Trace](https://github.com/delexw/claude-code-trace) | Viewing & Replay | [![GitHub stars](https://img.shields.io/github/stars/delexw/claude-code-trace?style=flat&label=stars)](https://github.com/delexw/claude-code-trace/stargazers)<br><sub>392 on 2026-11-26</sub> | Claude Code | Desktop<br>Web<br>TUI | Local debugging and real-time inspection of Claude Code sessions. | `MIT` |
| [claude-replay](https://github.com/es617/claude-replay) | Viewing & Replay | [![GitHub stars](https://img.shields.io/github/stars/es617/claude-replay?style=flat&label=stars)](https://github.com/es617/claude-replay/stargazers)<br><sub>862 on 2026-11-26</sub> | Claude Code<br>Codex<br>Cursor<br>Gemini CLI<br>OpenCode<br>Kimi Code | CLI<br>Web editor<br>HTML | Sharing, teaching, documenting, or reviewing agent sessions without video capture. | `MIT` |
| [Clawd Insights](https://github.com/yx0716/clawd-insights) | Analytics & Cost | [![GitHub stars](https://img.shields.io/github/stars/yx0716/clawd-insights?style=flat&label=stars)](https://github.com/yx0716/clawd-insights/stargazers)<br><sub>44 on 2026-11-26</sub> | Claude Code<br>Codex<br>Cursor<br>Other | Desktop<br>Web dashboard | macOS users who want qualitative reviews and timeline analytics over local sessions. | `AGPL-3.0` |
| [Codex History](https://github.com/nishantdesai/codex-history) | Discovery & Search | [![GitHub stars](https://img.shields.io/github/stars/nishantdesai/codex-history?style=flat&label=stars)](https://github.com/nishantdesai/codex-history/stargazers)<br><sub>10 on 2026-11-26</sub> | Codex | CLI | Terminal users who need conservative, scriptable access to Codex history. | `MIT` |
| [Codex History Viewer](https://github.com/HizTam/codex-history-viewer) | Discovery & Search | [![GitHub stars](https://img.shields.io/github/stars/HizTam/codex-history-viewer?style=flat&label=stars)](https://github.com/HizTam/codex-history-viewer/stargazers)<br><sub>49 on 2026-11-26</sub> | Codex<br>Claude Code | VS Code | VS Code users who want session history integrated with their editor workflow. | `MIT` |
| [Codex Session Export](https://github.com/MeXenon/codex-session-export) | Export, Migration & Handoff | [![GitHub stars](https://img.shields.io/github/stars/MeXenon/codex-session-export?style=flat&label=stars)](https://github.com/MeXenon/codex-session-export/stargazers)<br><sub>129 on 2026-11-26</sub> | Codex | TUI<br>CLI | Codex users who need fine-grained control over what enters an exported transcript. | `Apache-2.0` |
| [Codex Session Exporter](https://github.com/linfanxxxx/codex-session-exporter) | Export, Migration & Handoff | [![GitHub stars](https://img.shields.io/github/stars/linfanxxxx/codex-session-exporter?style=flat&label=stars)](https://github.com/linfanxxxx/codex-session-exporter/stargazers)<br><sub>20 on 2026-11-26</sub> | Codex | CLI | Moving complete Codex sessions between clients or machines while preserving metadata. | `MIT` |
| [Recensa](https://github.com/S40911120/recensa) | Viewing & Replay | [![GitHub stars](https://img.shields.io/github/stars/S40911120/recensa?style=flat&label=stars)](https://github.com/S40911120/recensa/stargazers)<br><sub>73 on 2026-11-26</sub> | Claude Code | Self-hosted web<br>Docker | Private browser-based review of a large local Claude Code transcript archive. | `MIT` |
| [sessions](https://github.com/nicknisi/sessions) | Discovery & Search | [![GitHub stars](https://img.shields.io/github/stars/nicknisi/sessions?style=flat&label=stars)](https://github.com/nicknisi/sessions/stargazers)<br><sub>53 on 2026-11-26</sub> | Claude Code<br>Codex<br>Pi<br>OpenCode | CLI<br>MCP<br>HTML report | Developers who want searchable history to double as agent-accessible project memory. | `MIT` |
| [UniSessions](https://github.com/vibheksoni/session-export) | Export, Migration & Handoff | [![GitHub stars](https://img.shields.io/github/stars/vibheksoni/session-export?style=flat&label=stars)](https://github.com/vibheksoni/session-export/stargazers)<br><sub>24 on 2026-11-26</sub> | Codex<br>Claude Code<br>Pi<br>OpenCode<br>Devin<br>Factory<br>Windsurf | Python SDK<br>CLI<br>MCP | Developers building migration, recall, or dataset pipelines across agent formats. | `MIT` |

## Projects

### Discovery & Search

Find, index, inspect, and resume historical sessions across projects or agents.

- [Agent Sessions](https://github.com/jazzyalex/agent-sessions) — Local-first macOS app for browsing, searching, analyzing, and resuming coding-agent session history. **Agents:** Claude Code, Codex, OpenCode, Cursor, Copilot CLI, Pi, Kimi Code, Other. **Interface:** macOS app. **Best for:** Developers who want one local visual history across many coding agents. **License:** `MIT`. [![GitHub stars](https://img.shields.io/github/stars/jazzyalex/agent-sessions?style=flat&label=stars)](https://github.com/jazzyalex/agent-sessions/stargazers)
- [Codex History](https://github.com/nishantdesai/codex-history) — Read-only CLI for searching, inspecting, and exporting locally stored Codex sessions. **Agents:** Codex. **Interface:** CLI. **Best for:** Terminal users who need conservative, scriptable access to Codex history. **License:** `MIT`. [![GitHub stars](https://img.shields.io/github/stars/nishantdesai/codex-history?style=flat&label=stars)](https://github.com/nishantdesai/codex-history/stargazers)
- [Codex History Viewer](https://github.com/HizTam/codex-history-viewer) — VS Code extension for searching, organizing, inspecting, and resuming Codex and Claude Code sessions. **Agents:** Codex, Claude Code. **Interface:** VS Code. **Best for:** VS Code users who want session history integrated with their editor workflow. **License:** `MIT`. [![GitHub stars](https://img.shields.io/github/stars/HizTam/codex-history-viewer?style=flat&label=stars)](https://github.com/HizTam/codex-history-viewer/stargazers)
- [sessions](https://github.com/nicknisi/sessions) — Unified full-text search, resume, MCP recall, and usage reporting over multiple coding-agent histories. **Agents:** Claude Code, Codex, Pi, OpenCode. **Interface:** CLI, MCP, HTML report. **Best for:** Developers who want searchable history to double as agent-accessible project memory. **License:** `MIT`. [![GitHub stars](https://img.shields.io/github/stars/nicknisi/sessions?style=flat&label=stars)](https://github.com/nicknisi/sessions/stargazers)

### Viewing & Replay

Turn raw session logs into readable, auditable, or shareable timelines.

- [Claude Code Trace](https://github.com/delexw/claude-code-trace) — Cross-platform viewer for browsing, searching, and live-tailing Claude Code JSONL session logs. **Agents:** Claude Code. **Interface:** Desktop, Web, TUI. **Best for:** Local debugging and real-time inspection of Claude Code sessions. **License:** `MIT`. [![GitHub stars](https://img.shields.io/github/stars/delexw/claude-code-trace?style=flat&label=stars)](https://github.com/delexw/claude-code-trace/stargazers)
- [claude-replay](https://github.com/es617/claude-replay) — Converts coding-agent transcripts into self-contained interactive HTML replays with optional redaction. **Agents:** Claude Code, Codex, Cursor, Gemini CLI, OpenCode, Kimi Code. **Interface:** CLI, Web editor, HTML. **Best for:** Sharing, teaching, documenting, or reviewing agent sessions without video capture. **License:** `MIT`. [![GitHub stars](https://img.shields.io/github/stars/es617/claude-replay?style=flat&label=stars)](https://github.com/es617/claude-replay/stargazers)
- [Recensa](https://github.com/S40911120/recensa) — Self-hosted local web viewer that indexes Claude Code transcripts for reading, search, replay, and audit. **Agents:** Claude Code. **Interface:** Self-hosted web, Docker. **Best for:** Private browser-based review of a large local Claude Code transcript archive. **License:** `MIT`. [![GitHub stars](https://img.shields.io/github/stars/S40911120/recensa?style=flat&label=stars)](https://github.com/S40911120/recensa/stargazers)

### Export, Migration & Handoff

Move session content between files, machines, clients, or agent formats.

- [Agent Session Resume](https://github.com/hacktivist123/agent-session-resume) — Reusable agent skill and helper scripts for reconstructing prior work and continuing from historical transcripts. **Agents:** Claude Code, Codex, Cursor, Antigravity, OpenCode, Copilot. **Interface:** Agent skill, Python helpers. **Best for:** Cross-agent handoffs where the next agent must recover unfinished work safely. **License:** `MIT`. [![GitHub stars](https://img.shields.io/github/stars/hacktivist123/agent-session-resume?style=flat&label=stars)](https://github.com/hacktivist123/agent-session-resume/stargazers)
- [Codex Session Export](https://github.com/MeXenon/codex-session-export) — Terminal-native tool for selecting, filtering, and exporting local Codex JSONL sessions to Markdown. **Agents:** Codex. **Interface:** TUI, CLI. **Best for:** Codex users who need fine-grained control over what enters an exported transcript. **License:** `Apache-2.0`. [![GitHub stars](https://img.shields.io/github/stars/MeXenon/codex-session-export?style=flat&label=stars)](https://github.com/MeXenon/codex-session-export/stargazers)
- [Codex Session Exporter](https://github.com/linfanxxxx/codex-session-exporter) — CLI for exporting Codex sessions to Markdown, HTML, or portable bundles and importing bundles elsewhere. **Agents:** Codex. **Interface:** CLI. **Best for:** Moving complete Codex sessions between clients or machines while preserving metadata. **License:** `MIT`. [![GitHub stars](https://img.shields.io/github/stars/linfanxxxx/codex-session-exporter?style=flat&label=stars)](https://github.com/linfanxxxx/codex-session-exporter/stargazers)
- [UniSessions](https://github.com/vibheksoni/session-export) — SDK-first converter for moving sessions among coding-agent formats and exporting training or trace datasets. **Agents:** Codex, Claude Code, Pi, OpenCode, Devin, Factory, Windsurf. **Interface:** Python SDK, CLI, MCP. **Best for:** Developers building migration, recall, or dataset pipelines across agent formats. **License:** `MIT`. [![GitHub stars](https://img.shields.io/github/stars/vibheksoni/session-export?style=flat&label=stars)](https://github.com/vibheksoni/session-export/stargazers)

### Session Management

Run, group, switch, monitor, or preserve multiple active coding-agent sessions.

- [Agent Deck](https://github.com/asheshgoplani/agent-deck) — Terminal command center for grouping, switching, forking, and monitoring active coding-agent sessions. **Agents:** Claude Code, Codex, OpenCode, Gemini CLI, Other CLIs. **Interface:** TUI, Web. **Best for:** Developers coordinating many concurrent terminal-agent sessions across projects. **License:** `MIT`. [![GitHub stars](https://img.shields.io/github/stars/asheshgoplani/agent-deck?style=flat&label=stars)](https://github.com/asheshgoplani/agent-deck/stargazers)
- [CCManager](https://github.com/kbwo/ccmanager) — TUI for managing multiple coding-agent sessions across projects and Git worktrees without requiring tmux. **Agents:** Claude Code, Codex, Gemini CLI, Cursor, Copilot CLI, Cline, OpenCode, Kimi CLI. **Interface:** TUI. **Best for:** Developers who want worktree-aware multi-agent session control in one terminal UI. **License:** `MIT`. [![GitHub stars](https://img.shields.io/github/stars/kbwo/ccmanager?style=flat&label=stars)](https://github.com/kbwo/ccmanager/stargazers)

### Analytics & Cost

Analyze activity, tokens, cost, and recurring patterns from local session data.

- [ccusage](https://github.com/ccusage/ccusage) — CLI that reads local coding-agent usage records and reports token consumption and estimated cost. **Agents:** Claude Code, Codex, OpenCode, Gemini CLI, Copilot CLI, Kimi, Other. **Interface:** CLI. **Best for:** Teams or individuals comparing local token usage and cost across many agent CLIs. **License:** `MIT`. [![GitHub stars](https://img.shields.io/github/stars/ccusage/ccusage?style=flat&label=stars)](https://github.com/ccusage/ccusage/stargazers)
- [Clawd Insights](https://github.com/yx0716/clawd-insights) — Local-first dashboard for session timelines, AI-generated reviews, activity analysis, and analysis-cost tracking. **Agents:** Claude Code, Codex, Cursor, Other. **Interface:** Desktop, Web dashboard. **Best for:** macOS users who want qualitative reviews and timeline analytics over local sessions. **License:** `AGPL-3.0`. [![GitHub stars](https://img.shields.io/github/stars/yx0716/clawd-insights?style=flat&label=stars)](https://github.com/yx0716/clawd-insights/stargazers)

<!-- catalog:end -->

## Related lists

- [Awesome CLI Coding Agents](https://github.com/bradAGI/awesome-cli-coding-agents) — broad directory of terminal-native coding agents and harnesses.
- [Awesome Codex CLI](https://github.com/RoggeOhta/awesome-codex-cli) — Codex-specific tools, skills, plugins, and resources.
- [Awesome Context Engineering](https://github.com/yzfly/awesome-context-engineering) — broader context-management techniques, resources, and tools.

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a project. The list is curated rather than exhaustive; every entry needs a concrete session-data capability and a verified open-source license.

Run the local checks before opening a pull request:

```sh
make render
make check
```

## License

This list is released under [CC0 1.0 Universal](LICENSE).
