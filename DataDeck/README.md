# 🃏 DataDeck

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Topic](https://img.shields.io/badge/Topic-Design_Patterns-orange.svg)
![Topic](https://img.shields.io/badge/Topic-Abstract_Factory-brightgreen.svg)

> **Abstract Card Architecture & Design Patterns**

## 🎯 Objective
This project explores advanced Object-Oriented Design Patterns in Python by building a dynamic, modular card game system. The goal is to architect a highly scalable system capable of handling thousands of creature variations, capabilities, and battle strategies without duplicating code or creating rigid class hierarchies.

---

## 🧠 Core Concepts
* **Abstract Factory Pattern (`ex0`):** Enforcing a structured creation process for related objects. The `CreatureFactory` ensures that every family (e.g., `FlameFactory`, `AquaFactory`) correctly implements methods to generate both base and evolved creature forms.
* **Interfaces & Mixins (`ex1`):** Utilizing multiple inheritance to decouple specific abilities (`HealCapability`, `TransformCapability`) from the base `Creature` class. This ensures that capabilities can be applied modularly to any entity.
* **Strategy Pattern (`ex2`):** Decoupling battle logic from the creatures themselves. By defining a `BattleStrategy` interface, behaviors (`NormalStrategy`, `AggressiveStrategy`, `DefensiveStrategy`) are injected dynamically at runtime, allowing the tournament engine to execute different tactical flows without altering the creature objects.
* **Static Typing & Casting (`typing.cast`):** Ensuring type safety when invoking specialized interface methods on abstract base objects, satisfying strict `mypy` requirements.

---

## 📐 Architecture: The Strategy Pattern
In `ex2` (Tournament), the battle logic is entirely decoupled from the creatures. Here is how the Strategy Pattern handles the execution dynamically at runtime:

```text
[ Tournament Engine (Context) ]
               │
               ▼
   [ BattleStrategy (ABC Interface) ] ◄── (Behavior injected into the fight)
               │
     ┌─────────┼──────────────┐
     ▼         ▼              ▼
  Normal   Aggressive     Defensive
     │         │              │
     ▼         ▼              ▼
  Attack   Transform      Attack
           Attack         Heal
           Revert
```

## 🛠️ Usage

The repository is structured to incrementally test the implementation of each Design Pattern. Run the simulation scripts from the root directory:

```bash
# Ex0: Abstract Factory (Testing base and evolved creature generation)
python3 battle.py

# Ex1: Capabilities / Interfaces (Testing modular abilities and state changes)
python3 capacitor.py

# Ex2: Strategy Pattern (Running the tournament with injected battle behaviors)
python3 tournament.py
```

## 👤 Author

- **Anas Alissa**

- **Campus:** 42 Irbid (Common Core Track)