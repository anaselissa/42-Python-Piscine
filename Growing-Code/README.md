# Growing Code
> Python Fundamentals Through Garden Data

## 🎯 Objective

This project introduces Python's fundamental syntax and semantics using practical community garden scenarios. It focuses on expressions, variables, functions, and control flow to build a solid programming foundation.

## 🧠 Technical Concepts Applied

* **Standard I/O:** Handling user input and terminal output (`input()`, `print()`).
* **Control Flow:** Implementing conditional logic (`if`/`elif`/`else`) and iterative loops (`for` with `range()`).
* **Data Casting & Formatting:** Converting strings to integers (`int()`) and utilizing f-strings with string methods like `capitalize()` for dynamic outputs.
* **Type Annotations (Typing):** Enforcing strict data types (`str`, `int`) and return types (`-> None`) in function signatures, verified via tools like `mypy`.
* **Algorithmic Thinking (Iteration vs. Recursion):** Solving the same problem using two distinct paradigms, including the use of nested helper functions for recursion.

### 📐 Visualizing Execution: Iteration vs. Recursion (`ex5`)

To deeply understand how `ft_count_harvest_iterative` differs from `ft_count_harvest_recursive`, here is a visual representation of how the memory handles both approaches:

```text
[ Iteration: A single process running in a loop ]

Start ➔ (Day 1) ➔ (Day 2) ➔ (Day 3) ➔ Harvest!
        └── loop returns here ──┘


[ Recursion: A stack of function calls (Nested Helper) ]

count(1) calls ➔ count(2) calls ➔ count(3) calls ➔ Harvest!
     ↑                ↑                ↑
   (Day 1)          (Day 2)          (Day 3)
     └─ waits for ───┘                │
                      └─ waits for ───┘
```

## 🛠️ Usage

Each exercise is contained in its own file and consists strictly of a single function without a main execution block.

To test the functions using the provided helper script:

```bash
# Ensure main.py is in the working directory alongside your exercise files.
python3 main.py
```
