<div align="center">
  <h1>🐾 Nuzzle — Codex Pets</h1>
  <p><strong>A living companion studio for AI coding agents with animated 8×9 anime sprite atlases.</strong></p>
  <p>
    Nuzzle combines the agent-aware interaction model and lifecycle event vocabulary from <a href="https://github.com/ChanceYu/CoPet">CoPet</a> with the 8×9 Codex-compatible anime pet sprite atlas collection from <a href="https://github.com/chenxin-dlut/codex-anime-pets">codex-anime-pets</a>.
  </p>
  <p>
    <a href="#features">Features</a> •
    <a href="#supported-agents">Supported Agents</a> •
    <a href="#pet-collection">Pet Collection</a> •
    <a href="#atlas-specifications">8×9 Atlas Specs</a> •
    <a href="#quick-start">Quick Start</a> •
    <a href="#contributors--credits">Contributors</a> •
    <a href="#license">License</a>
  </p>
</div>

---

## ✦ Features

- **Real-Time Agent Reactions**: Reacitve companion animations respond in real time to Agent prompts, tool calls, thinking/waiting, completions, and error states.
- **8×9 Sprite Animation Engine**: CSS `@keyframes` frame-stepping engine rendering continuous animations for idle breathing, pat/waving reactions, energetic running/working, and resting states.
- **Interactive Companion Stage**: Click or pat your active companion to trigger animated reactions, floating sparkle/heart particle bursts, and synthesized Web Audio micro-chimes.
- **Dynamic Companion Switching**: Switch your featured companion from the Quick Dispatch Strip, Pet Library, or Command Palette with instant cross-view state synchronization.
- **Pet Library & Filtering**: Catalog of 8×9 anime sprite atlases with instant search and vibe filtering (`all`, `anime`, `cozy`, `chaos`).
- **Command Palette (`⌘ K` / `Ctrl+K`)**: Fast keyboard-driven command palette with live query filtering, number shortcuts (`1`–`4`), arrow key navigation, and quick companion dispatching.
- **Customizable Preferences**: Dedicated settings sub-tabs for **Appearance** (pet scale `S`/`M`/`L`, film grain overlay, animations), **Behavior** (agent messaging, start greeting, float mode), **Sound** (reaction micro-tones, completion alerts), and **Privacy** (100% local-first storage reset).
- **Local-First & Zero Cloud**: All state, settings, and favorites are stored locally in your browser/device with zero telemetry and zero external tracking.

---

## 🤖 Supported Agents

Nuzzle is designed around the dependable local hook event model pioneered by CoPet, bridging lifecycle events from leading AI coding agents:

| Agent | Integration Model | Default Config Path |
| :--- | :--- | :--- |
| **Claude Code** | JSON hooks | `~/.claude/settings.json` |
| **Codex** | JSON hooks + trusted hashes | `~/.codex/hooks.json`, `~/.codex/config.toml` |
| **Antigravity** | JSON hooks | `~/.gemini/config/hooks.json` |
| **OpenCode** | JS plugin + config entry | `~/.config/opencode/plugins/copet.js` |
| **Cursor** | JSON hooks | `~/.cursor/hooks.json` |
| **Copilot CLI** | JSON hook file | `~/.copilot/hooks/copet.json` |
| **Pi** | TypeScript extension | `~/.pi/agent/extensions/copet/index.ts` |
| **Gemini** | JSON hooks | `~/.gemini/settings.json` |

---

## 🎭 Pet Collection

The included pet collection features full 8×9 animation sprite sheets:

| Companion | Vibe | Element | Lore Note |
| :--- | :--- | :--- | :--- |
| **Hu Tao** | `chaos` | Pyro | *“If there’s work to do, I’ll haunt it.”* · spirited & lively |
| **Furina** | `anime` | Hydro | *“Let the drama of code execution unfold!”* · dramatic & theatrical |
| **Raiden** | `cozy` | Electro | *“Transcendence requires uninterrupted focus.”* · zen & focused |
| **Ganyu** | `cozy` | Cryo | *“Overtime again? I brought extra tea...”* · gentle & hardworking |
| **Klee** | `chaos` | Pyro | *“Spark Knight Klee reporting for bug hunting!”* · energetic & explosive |
| **Anya** | `anime` | Esper | *“Waku waku! Agent is planning something big!”* · telepathic & curious |
| **Aiko** | `anime` | Anemo | *“Every line of code is a new little adventure.”* · bright & explorer |
| **Ayaka** | `cozy` | Cryo | *“May your compilation be swift and graceful.”* · elegant precision |

---

## 📐 8×9 Atlas Specifications

The sprite sheet atlases in `public/pets/` follow the standard Codex 8×9 layout:

- **Dimensions**: `1536 × 2070` pixels (or `1536 × 1872` WebP).
- **Grid Layout**: `8 columns × 9 rows`.
- **Cell Size**: `192 × 230` pixels per frame.
- **Row Mapping**:
  - **Row 0**: `idle` (6 active frames)
  - **Row 1**: `running-right` (8 active frames)
  - **Row 2**: `running-left` (8 active frames)
  - **Row 3**: `waving` (4 active frames) — *Pat & greeting reaction*
  - **Row 4**: `jumping` (5 active frames) — *Excited & happy state*
  - **Row 5**: `failed` (8 active frames) — *Agent error state*
  - **Row 6**: `waiting` (6 active frames) — *Thinking & resting state*
  - **Row 7**: `running` (6 active frames) — *Active tool call / work state*
  - **Row 8**: `review` (6 frames) — *Code review & summary state*

---

## 🚀 Quick Start

This workspace is intentionally dependency-light with zero runtime build requirements.

### 1. Run Locally

Serve the project root with any static HTTP server:

```bash
# Using Python 3
python3 -m http.server 4173
```

Then open **[http://localhost:4173](http://localhost:4173)** in your browser.

### 2. Automated Verification & Testing

Run the automated Playwright test suite to verify UI rendering, animation states, settings sub-tabs, and command palette navigation:

```bash
python3 verify_app.py
```

---

## 📂 Project Structure

```
Nuzzle-Codex-pets/
├── index.html            # Main HTML5 application shell & view panels
├── styles.css            # Unified CSS3 design system & 8x9 animation engine
├── app.js                # Core JS logic, state store & audio synthesizers
├── pets -> public/pets   # Symlink for root-relative asset routing
├── public/
│   ├── pets/             # 8 character 8x9 sprite sheets + avatar badges
│   └── source-notes/     # Reference source notes
├── verify_app.py         # Playwright end-to-end automated test suite
├── inspect_overview.py   # Full-page screenshot inspection script
├── LICENSE               # MIT License & upstream attributions
└── README.md             # Project documentation & credits
```

---

## 👥 Contributors & Credits

Nuzzle is built on the shoulders of two open-source projects:

- **[CoPet](https://github.com/ChanceYu/CoPet)**: Created and maintained by **[@ChanceYu](https://github.com/ChanceYu)** and contributors. CoPet pioneered the agent-aware desktop pet interaction model, lifecycle hook event architecture, and desktop companion vocabulary.
- **[codex-anime-pets](https://github.com/chenxin-dlut/codex-anime-pets)**: Created and maintained by **[@chenxin-dlut (Xin Chen)](https://github.com/chenxin-dlut)** and **[@webbrain-one](https://github.com/webbrain-one)**. Provided the 8×9 Codex-compatible anime pet sprite atlas collection and contact sheet specifications.
- **[Nuzzle Studio](https://github.com/satiricalguru/Nuzzle-Codex-pets)**: Maintained by **[@satiricalguru](https://github.com/satiricalguru)**.

---

## 📄 License & Disclaimers

- **Code & Documentation**: Licensed under the [MIT License](LICENSE) © 2026 Nuzzle Contributors, ChanceYu, and Xin Chen.
- **Pet Sprite Sheet Assets**: The character sprite sheet images in `public/pets/` are fan-made generated art interpretations inspired by anime and game characters. No license is granted to any underlying third-party character, trademark, or franchise. All copyrights and trademarks remain with their respective rights holders. This project is unofficial, non-commercial, and not affiliated with or endorsed by any rights holder.
