# Garden Guardian
> Data Engineering for Smart Agriculture

## 🎯 Objective

This project focuses on building resilient data pipelines for smart agriculture by mastering Python's exception handling capabilities. The goal is to gracefully handle sensor failures, validate agricultural data streams, and ensure that the monitoring system continues to run robustly even when unexpected errors occur.

## 🧠 Technical Concepts Applied

* **Exception Catching (`try/except`):** Safely intercepting specific built-in errors such as `ValueError`, `ZeroDivisionError`, `FileNotFoundError`, and `TypeError` to prevent abrupt program crashes.
* **Manual Error Triggering (`raise`):** Validating data bounds (e.g., ensuring temperature readings remain between 0°C and 40°C) and raising explicit exceptions when the data is corrupted or unsafe for plants.
* **Custom Exception Hierarchies (OOP):** Engineering domain-specific error classes (`GardenError`, `PlantError`, `WaterError`) by utilizing class inheritance from Python's base `Exception` object. This enables structured, polymorphic error catching.
* **Guaranteed Resource Cleanup (`finally`):** Implementing strict cleanup procedures (such as closing a watering system) that are guaranteed to execute regardless of whether an exception was raised, caught, or if the function returned early.

### 📐 Visualizing Exception Lifecycle (`ex4` Architecture)

To understand how the pipeline secures resources using the `finally` block, here is a visual representation of the execution flow:

```text
[ Data Pipeline: water_plant() ]
       │
       ▼
 ┌───────────┐
 │   try:    │ ──(Valid Plant)──> [ OK: Plant Watered ] ──────────┐
 └───────────┘                                                    │
       │                                                          │
 (Invalid Plant)                                                  │
       ▼                                                          │
 ┌───────────┐                                                    │
 │  except:  │ ──(Catch PlantError)──> [ Log Error & Return ] ────┤
 └───────────┘                                                    │
                                                                  ▼
                                                          ┌──────────────┐
                                                          │   finally:   │
                                                          │ Close System │
                                                          └──────────────┘
                                                          (ALWAYS EXECUTES)
```

## 🛠️ Usage

Each exercise demonstrates a different aspect of error handling and runs independently.

To test the fault-tolerance of the pipelines, run the scripts directly:

```bash
# Ex0: Basic string-to-integer exception catching
python3 ex0/ft_first_exception.py

# Ex1: Raising bounded exceptions for temperature data
python3 ex1/ft_raise_exception.py

# Ex2: Catching discrete, specific built-in errors
python3 ex2/ft_different_errors.py

# Ex3: Working with custom OOP exception inheritance
python3 ex3/ft_custom_errors.py

# Ex4: Forcing execution of cleanup protocols
python3 ex4/ft_finally_block.py
```