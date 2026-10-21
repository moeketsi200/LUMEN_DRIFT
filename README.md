# Lumen Drift

[![Platform](https://img.shields.io/badge/Platform-Decentraland-red.svg)](https://decentraland.org)
[![Engine](https://img.shields.io/badge/SDK-Decentraland%20SDK%207-blue.svg)](https://docs.decentraland.org)
[![Language](https://img.shields.io/badge/Language-TypeScript-blue.svg)](https://www.typescriptlang.org)
[![Status](https://img.shields.io/badge/Status-V0%20Development-green.svg)](#)

> **Lumen Drift** is a fast-paced, bioluminescent arcade precision runner built on Decentraland. Players guide a luminous, organic deep-sea creature through a hazardous winding tunnel—evading glowing tendrils, collecting energy nodes, and competing against the clock.

---

## 🎮 Gameplay Overview

- **Genre:** Arcade Precision Runner / Time Trial
- **Controls:** Keyboard (`A`/`D` or `Left`/`Right` arrow keys to steer, `Space`/`Enter` to restart)
- **Target Run Duration:** 30–60 seconds per run
- **Visual Aesthetic:** Deep-sea bioluminescence—cyan/turquoise player elements set against deep navy environments and hazardous magenta tendrils.

---

## 📖 Game Design Document (GDD)

The full specification, mechanics breakdown, mathematical tuning, and architecture are documented in:
👉 **[Game Design Document (`design/gdd.md`)](design/gdd.md)**

---

## 🚀 Getting Started

### Prerequisites
- [Node.js](https://nodejs.org/) (version 18+ or 20+ recommended)
- [Decentraland CLI](https://docs.decentraland.org/creator/development-guide/sdk7/dev-environment/) installed globally:
  ```bash
  npm install -g decentraland
  ```

### Local Development Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/LUMEN_DRIFT.git
   cd LUMEN_DRIFT
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Launch the local development preview:**
   ```bash
   npm start
   # or
   dcl start
   ```
   A browser window will open automatically with the local Decentraland scene running.

---

## 🏗️ Project Architecture

```text
LUMEN_DRIFT/
├── README.md               # Project overview and setup instructions
├── package.json            # Node & Decentraland SDK dependencies
├── scene.json              # Decentraland scene manifest & coordinates
├── design/
│   └── gdd.md              # Complete Game Design Document
└── src/
    ├── index.ts            # Scene entry point & lifecycle
    ├── game/               # Core systems
    │   ├── GameManager.ts       # Master game state machine
    │   ├── PlayerController.ts  # Steering and forward velocity
    │   ├── TailAnimator.ts      # Undulating procedural tail
    │   ├── CollisionSystem.ts   # Boundary & hazard collision logic
    │   ├── CollectibleSystem.ts # Luminous node pickup handler
    │   └── CourseManager.ts     # Tunnel layout & hazard generator
    ├── entities/           # Scene object factories
    │   ├── Player.ts
    │   ├── Hazard.ts
    │   └── Collectible.ts
    ├── ui/                 # In-scene HUD and modal interfaces
    │   ├── StartScreen.ts
    │   ├── GameHUD.ts
    │   └── ResultsScreen.ts
    └── levels/
        └── Level01.ts       # V0 single-course layout
```

---

## 🗓️ Roadmap (Decentraland Creator Success V0)

- [x] **Week 1:** Project blueprint, repository setup, and Game Design Document.
- [ ] **Week 2:** Core creature movement, lateral steering, camera tracking, and boundary collisions.
- [ ] **Week 3:** Complete loop—hazards, collectible nodes, timer, score, and restart flow.
- [ ] **Week 4:** Visual polish—emissive bioluminescent materials, tail undulation, and particles.
- [ ] **Week 5:** Deployment to a public Decentraland World and playtesting.
- [ ] **Week 6:** Creator Success submission and review onboarding.

---

## 👥 Creator Success Reviewers

As required by the Decentraland Creator Success application, the following reviewer accounts are granted repository access:
- `pravusjif`
- `popuz`
- `baybackner`
- `nearnshaw`

---

## 📄 License
This project is developed for the Decentraland Creator Success Programme. All rights reserved.
