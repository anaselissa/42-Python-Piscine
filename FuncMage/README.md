# 🧙‍♂️ FuncMage

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Topic](https://img.shields.io/badge/Topic-Functional_Programming-orange.svg)
![Topic](https://img.shields.io/badge/Topic-Decorators-brightgreen.svg)

> **Advanced Functional Programming & Decorator Architecture**

## 🎯 Objective
This project marks a fundamental paradigm shift from imperative and object-oriented programming to pure **Functional Programming (FP)**. The objective is to treat functions as "first-class citizens"—passing them as arguments, returning them from other functions, and managing persistent state without relying on global variables.

---

## 🧠 Core Concepts
* **Anonymous Functions (`lambda`):** Utilizing inline, unnamed functions alongside iterators (`map`, `filter`, `sorted`) for rapid data transformation.
* **Higher-Order Functions:** Architecting functions that accept or return other functions (e.g., `spell_combiner`) to build composable logic.
* **Lexical Scoping & Closures:** Encapsulating state within nested functions using the `nonlocal` keyword (e.g., `memory_vault`), ensuring data persistence while avoiding global scope pollution.
* **Advanced `functools`:** 
  * `reduce`: Aggregating data streams.
  * `partial`: Pre-filling arguments for specialized templates.
  * `lru_cache`: Implementing memoization to optimize recursive algorithms.
  * `singledispatch`: Enabling function overloading based on argument types.
* **Decorator Engineering (`@wraps`):** Building custom function wrappers that dynamically alter execution behavior (timing, retrying, validating) via runtime metadata inspection (`inspect.signature`).

---

## 📐 Architecture: Decorator Execution
To understand how a Decorator alters execution flow without modifying the underlying function, here is the architectural pipeline of `@power_validator`:

```text
[ Function Call: mage.cast_spell("sleep", power=9) ]
                             │
                             ▼
  ┌─────────────────────────────────────────────────────┐
  │ @power_validator(min_power=10) (The Outer Wrapper)  │
  │   │                                                 │
  │   ├── 1. Intercepts *args and **kwargs              │
  │   ├── 2. Binds signature to find 'power' value (9)  │
  │   ├── 3. Condition: Is 9 >= 10?                     │
  │   │      ├── [NO] ➔ Abort! Return Error String      │ ◄─ Execution Stops
  │   │      └── [YES]➔ Proceed to Step 4               │
  │   │                                                 │
  │   └── 4. return func(*args, **kwargs)               │
  └──────────────────────────┬──────────────────────────┘
                             ▼
             [ Original cast_spell() Logic ]



## 🛠️ Usage

Execute the following scripts to test the functional paradigms isolated in each realm:

```bash
# Ex0: Lambda Sanctum (Anonymous functions and iterators)
python3 ex0/lambda_spells.py

# Ex1: Higher Realm (Combining and amplifying functions)
python3 ex1/higher_magic.py

# Ex2: Memory Depths (State retention using Closures and nonlocal)
python3 ex2/scope_mysteries.py

# Ex3: Ancient Library (Functools: reduce, partial, lru_cache, singledispatch)
python3 ex3/functools_artifacts.py

# Ex4: Master's Tower (Custom Decorators and Introspection)
python3 ex4/decorator_mastery.py
```

## 👤 Author

- **Anas Alissa**

- **Campus:** 42 Irbid (Common Core Track)