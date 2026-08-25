<div align="center">

  <img src="https://raw.githubusercontent.com/satiricalguru/Nuzzle-Codex-pets/main/public/nuzzle-logo.png" alt="Nuzzle Logo" width="160" />

  # 🐾 Nuzzle — Codex Pets

  <p><strong>A living companion studio for every AI coding agent.</strong></p>
  <p>
    Nuzzle combines the agent-aware interaction model and lifecycle event vocabulary from <a href="https://github.com/ChanceYu/CoPet"><strong>CoPet</strong></a> with the 8×9 Codex-compatible anime pet sprite atlas collection from <a href="https://github.com/chenxin-dlut/codex-anime-pets"><strong>codex-anime-pets</strong></a>.
  </p>

  <p>
    <a href="https://github.com/satiricalguru/Nuzzle-Codex-pets/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-coral?style=for-the-badge&color=ef7861" alt="MIT License" /></a>
    <img src="https://img.shields.io/badge/Local--First-100%25-green?style=for-the-badge&color=66a76e" alt="Local First" />
    <img src="https://img.shields.io/badge/Dependencies-0%20Runtime-yellow?style=for-the-badge&color=e7bc55" alt="Zero Dependencies" />
    <img src="https://img.shields.io/badge/Agents-8%20Supported-purple?style=for-the-badge&color=9e624d" alt="8 Agents Supported" />
  </p>

  <p>
    <a href="#-showcase--previews">Showcase</a> •
    <a href="#-features">Features</a> •
    <a href="#-supported-agents">Supported Agents</a> •
    <a href="#-built-in-pets-gallery">Built-in Pets</a> •
    <a href="#-anime-companions-collection">Anime Companions</a> •
    <a href="#-89-atlas-specifications">8×9 Atlas Specs</a> •
    <a href="#-quick-start">Quick Start</a> •
    <a href="#-contributors--project-credits">Contributors</a> •
    <a href="#-license">License</a>
  </p>

</div>

---

## 🎬 Showcase & Previews

<div align="center">
  <img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/banner.png" alt="CoPet Desktop Companion Banner" width="950" style="border-radius: 12px; margin-bottom: 16px;" />
</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/animations/codex-anime-pets-showcase.gif" alt="Animated Showcase of 8x9 Anime Pets" width="700" style="border-radius: 10px;" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/gallery/codex-anime-pets-gallery.jpg" alt="Codex Anime Pets Gallery Poster" width="950" style="border-radius: 10px;" />
</p>

---

## ✨ Features

- ⚡ **Real-Time Agent Reactions**: Companions react instantly to agent prompts, tool execution, thinking/waiting, completions, and error states.
- 🎨 **8×9 Sprite Animation Engine**: High-performance CSS frame-stepping engine rendering continuous animations for idle breathing, pat/waving reactions, energetic running/working, and resting states.
- ♡ **Interactive Companion Stage**: Click or pat your active companion to trigger animated reactions, floating sparkle/heart particle bursts, and synthesized Web Audio micro-chimes.
- 🔄 **Dynamic Companion Switching**: Switch your featured companion from the Quick Dispatch Strip, Pet Library, or Command Palette with instant cross-view state synchronization.
- 📚 **Pet Library & Filtering**: Catalog of 8×9 anime sprite atlases with instant search and vibe filtering (`all`, `anime`, `cozy`, `chaos`).
- ⌨️ **Command Palette (`⌘ K` / `Ctrl+K`)**: Fast keyboard-driven command palette with live query filtering, number shortcuts (`1`–`4`), arrow key navigation, and quick companion dispatching.
- ⚙️ **Customizable Preferences**: Dedicated settings sub-tabs for **Appearance** (pet scale `S`/`M`/`L`, film grain overlay, animations), **Behavior** (agent messaging, start greeting, float mode), **Sound** (reaction micro-tones, completion alerts), and **Privacy** (100% local-first storage reset).
- 🛡️ **100% Local-First & Zero Cloud**: All state, settings, and favorites are stored locally in your browser/device with zero telemetry, zero tokens leaving your machine, and atomic local writes.

---

## 🤖 Supported Agents

Nuzzle bridges lifecycle events across all leading AI coding assistants:

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

## 🐶 Built-in Pets Gallery

Living animated pixel pets from the original CoPet companion collection:

<table>
  <tr>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/copet-neo.gif" width="96" alt="CoPet Neo" /><br /><sub><b>CoPet Neo</b></sub></td>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/copet-nia.gif" width="96" alt="CoPet Nia" /><br /><sub><b>CoPet Nia</b></sub></td>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/copet-mecha.gif" width="96" alt="CoPet Mecha" /><br /><sub><b>CoPet Mecha</b></sub></td>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/dj-fuzz.gif" width="96" alt="DJ Fuzz" /><br /><sub><b>DJ Fuzz</b></sub></td>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/dog.gif" width="96" alt="Lucky Dog" /><br /><sub><b>Lucky Dog</b></sub></td>
  </tr>
  <tr>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/dragon.gif" width="96" alt="Azure Dragon" /><br /><sub><b>Azure Dragon</b></sub></td>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/duck.gif" width="96" alt="Waddly Duck" /><br /><sub><b>Waddly Duck</b></sub></td>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/goat.gif" width="96" alt="Cloud Goat" /><br /><sub><b>Cloud Goat</b></sub></td>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/goku.gif" width="96" alt="Goku" /><br /><sub><b>Goku</b></sub></td>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/horse.gif" width="96" alt="Chestnut Horse" /><br /><sub><b>Chestnut Horse</b></sub></td>
  </tr>
  <tr>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/monkey.gif" width="96" alt="Clever Monkey" /><br /><sub><b>Clever Monkey</b></sub></td>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/orange-cat.gif" width="96" alt="Orange Cat" /><br /><sub><b>Orange Cat</b></sub></td>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/ox.gif" width="96" alt="Cream Ox" /><br /><sub><b>Cream Ox</b></sub></td>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/panda.gif" width="96" alt="Panda" /><br /><sub><b>Panda</b></sub></td>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/pig.gif" width="96" alt="Blush Pig" /><br /><sub><b>Blush Pig</b></sub></td>
  </tr>
  <tr>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/rabbit.gif" width="96" alt="White Rabbit" /><br /><sub><b>White Rabbit</b></sub></td>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/rat.gif" width="96" alt="Pearl Rat" /><br /><sub><b>Pearl Rat</b></sub></td>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/rooster.gif" width="96" alt="Golden Rooster" /><br /><sub><b>Golden Rooster</b></sub></td>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/snake.gif" width="96" alt="Jade Snake" /><br /><sub><b>Jade Snake</b></sub></td>
    <td align="center"><img src="https://raw.githubusercontent.com/ChanceYu/CoPet/main/public/pets/tiger.gif" width="96" alt="Striped Tiger" /><br /><sub><b>Striped Tiger</b></sub></td>
  </tr>
</table>

---

## 🌸 Anime Companions Collection

8×9 sprite atlas anime companions packaged for Codex:

| Companion | Preview | Vibe | Lore & Personality | Contact Sheet |
| :--- | :---: | :---: | :--- | :---: |
| **Hu Tao**<br><sub>`hu-tao`</sub> | <img src="https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/previews/hu-tao.png" width="100" alt="Hu Tao" /> | `chaos` · Pyro | *“If there’s work to do, I’ll haunt it.”* · spirited & lively | [Full 8×9 Atlas](https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/contact-sheets/hu-tao.png) |
| **Furina**<br><sub>`furina`</sub> | <img src="https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/previews/furina.png" width="100" alt="Furina" /> | `anime` · Hydro | *“Let the drama of code execution unfold!”* · dramatic | [Full 8×9 Atlas](https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/contact-sheets/furina.png) |
| **Raiden**<br><sub>`raiden`</sub> | <img src="https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/previews/raiden.png" width="100" alt="Raiden" /> | `cozy` · Electro | *“Transcendence requires uninterrupted focus.”* · zen | [Full 8×9 Atlas](https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/contact-sheets/raiden.png) |
| **Ganyu**<br><sub>`ganyu`</sub> | <img src="https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/previews/ganyu.png" width="100" alt="Ganyu" /> | `cozy` · Cryo | *“Overtime again? I brought extra tea...”* · gentle | [Full 8×9 Atlas](https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/contact-sheets/ganyu.png) |
| **Klee**<br><sub>`klee`</sub> | <img src="https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/previews/klee.png" width="100" alt="Klee" /> | `chaos` · Pyro | *“Spark Knight Klee reporting for bug hunting!”* · energetic | [Full 8×9 Atlas](https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/contact-sheets/klee.png) |
| **Anya**<br><sub>`anya`</sub> | <img src="https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/previews/anya.png" width="100" alt="Anya" /> | `anime` · Esper | *“Waku waku! Agent is planning something big!”* · mind reader | [Full 8×9 Atlas](https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/contact-sheets/anya.png) |
| **Aiko**<br><sub>`aiko`</sub> | <img src="https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/previews/aiko.png" width="100" alt="Aiko" /> | `anime` · Anemo | *“Every line of code is a new little adventure.”* · bright | [Full 8×9 Atlas](https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/contact-sheets/aiko.png) |
| **Ayaka**<br><sub>`ayaka`</sub> | <img src="https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/previews/ayaka.png" width="100" alt="Ayaka" /> | `cozy` · Cryo | *“May your compilation be swift and graceful.”* · precision | [Full 8×9 Atlas](https://raw.githubusercontent.com/chenxin-dlut/codex-anime-pets/main/assets/contact-sheets/ayaka.png) |

---

## 📐 8×9 Atlas Specifications

The sprite sheets follow the standard Codex 8×9 layout:

- **Dimensions**: `1536 × 2070` pixels (or `1536 × 1872` WebP).
- **Grid Layout**: `8 columns × 9 rows`.
- **Cell Size**: `192 × 230` pixels per frame.
- **Row Mappings**:
  - **Row 0**: `idle` (6 active frames) — *Gentle breathing and blinking*
  - **Row 1**: `running-right` (8 active frames) — *Moving right*
  - **Row 2**: `running-left` (8 active frames) — *Moving left*
  - **Row 3**: `waving` (4 active frames) — *Head pat & greeting reaction*
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

## 👥 Contributors & Project Credits

Nuzzle is built on the shoulders of brilliant open-source creators:

<table>
  <tr>
    <td align="center" width="25%">
      <a href="https://github.com/ChanceYu">
        <img src="https://github.com/ChanceYu.png" width="100" style="border-radius: 50%;" alt="ChanceYu" /><br />
        <sub><b>ChanceYu</b></sub>
      </a><br />
      <small>Creator & Maintainer of <a href="https://github.com/ChanceYu/CoPet">CoPet</a></small>
    </td>
    <td align="center" width="25%">
      <a href="https://github.com/chenxin-dlut">
        <img src="https://github.com/chenxin-dlut.png" width="100" style="border-radius: 50%;" alt="chenxin-dlut" /><br />
        <sub><b>Xin Chen (chenxin-dlut)</b></sub>
      </a><br />
      <small>Creator of <a href="https://github.com/chenxin-dlut/codex-anime-pets">codex-anime-pets</a></small>
    </td>
    <td align="center" width="25%">
      <a href="https://github.com/webbrain-one">
        <img src="https://github.com/webbrain-one.png" width="100" style="border-radius: 50%;" alt="webbrain-one" /><br />
        <sub><b>webbrain-one</b></sub>
      </a><br />
      <small>Contributor to <a href="https://github.com/chenxin-dlut/codex-anime-pets">codex-anime-pets</a></small>
    </td>
    <td align="center" width="25%">
      <a href="https://github.com/satiricalguru">
        <img src="https://github.com/satiricalguru.png" width="100" style="border-radius: 50%;" alt="satiricalguru" /><br />
        <sub><b>Jatin Pandey (satiricalguru)</b></sub>
      </a><br />
      <small>Maintainer of <a href="https://github.com/satiricalguru/Nuzzle-Codex-pets">Nuzzle Studio</a></small>
    </td>
  </tr>
</table>

---

## 📄 License & Disclaimers

- **Code & Documentation**: Licensed under the [MIT License](LICENSE) © 2026 Nuzzle Contributors, ChanceYu, and Xin Chen.
- **Pet Sprite Sheet Assets**: The character sprite sheet images in `public/pets/` are fan-made generated art interpretations inspired by anime and game characters. No license is granted to any underlying third-party character, trademark, or franchise. All copyrights and trademarks remain with their respective rights holders. This project is unofficial, non-commercial, and not affiliated with or endorsed by any rights holder.
