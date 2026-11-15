# Quark Confinement Simulation (Prototype v0.2)

Interactive 2D physics simulation of strong interaction (confinement) inside a proton (`uud` quarks) built with Python and Pyglet.

## Features (v0.2)
* **Chaotic Motion:** Random thermal-like movement of quarks within the hadron.
* **Gluon Attraction:** Continuous pull toward the dynamic center of mass, simulating the strong nuclear force.
* **Interactive Control:** Drag individual quarks with the left mouse button to stretch gluon links.

## Roadmap (v0.3)
The project will be migrated to **Unity (C#)** to implement advanced physics:
* **Hadronization (String Breaking):** Spawning quark-antiquark pairs (`u/anti-u`, `d/anti-d`) when gluon tension exceeds the energy threshold.
* **High-Energy Collisions:** Pair production upon high-velocity quark impacts.

## Installation & Run
1. Clone the repository:
   ```bash
   git clone https://github.com
   cd quark-simulation
   ```
2. Install dependencies:
   ```bash
   pip install pyglet
   ```
3. Run the simulation:
   ```bash
   python main.py
   ```
