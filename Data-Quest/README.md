# Data Quest
> Mastering Python Collections & Game Data Engineering

## 🎯 Objective

This project dives into the heart of data engineering by exploring Python's core data structures within a game analytics context. The goal is to process massive amounts of game data efficiently by choosing the exact right tool for the job—transforming linear time operations into optimized, memory-safe processes.

## 🧠 Technical Concepts Applied

* **Lists & CLI Parsing:** Safely ingesting and cleaning command-line arguments (`sys.argv`), utilizing error handling to discard corrupted inputs and perform statistical math (`sum`, `max`, `min`).
* **N-Tuples (Immutable Data):** Storing fixed 3D spatial coordinates (X, Y, Z) and applying the Euclidean distance formula (`math.sqrt`) to track player movement.
* **Sets (Unique Elements):** Utilizing mathematical set operations (`union`, `intersection`, `difference`) to analyze, compare, and filter unique player achievements without duplicates.
* **Associative Arrays (Dictionaries):** Building a dynamic game inventory system using key-value pairs, updating quantities, and calculating percentage distributions.
* **Lazy Iterators (Generators):** Using the `yield` keyword to create infinite data streams for game events, bypassing massive memory overhead by generating values strictly on-demand.
* **Comprehensions (Data Alchemy):** Writing highly optimized, single-line list and dictionary comprehensions to filter and transform data elegantly without verbose loop constructs.

### 📐 Visualizing Memory Efficiency (Generators vs. Lists)

In `ex5` (Stream Wizard), generators are used to handle 1000+ events safely. Here is exactly what happens in the system memory (RAM) under the hood:

```text
[ Standard List: Loads entirely into memory ]

RAM: [ Event 1 | Event 2 | ... | Event 1000000 ]
                              ↓
                    High memory usage


[ Generator (yield): Computes on-demand ]

RAM: [ Event 1 ] ➔ process & discard
          ↓
     [ Event 2 ] ➔ process & discard
          ↓
     [ Event 3 ] ➔ ...
```

## 🛠️ Usage

The project is divided into standalone Python scripts. Run them via the terminal, passing the required arguments where applicable:

```bash
# Ex0 & Ex1: Command-line parsing and List statistics
python3 ex0/ft_command_quest.py arg1 arg2
python3 ex1/ft_score_analytics.py 1500 2300 1800 2100

# Ex2: Tuple operations
python3 ex2/ft_coordinate_system.py

# Ex3: Set mathematics
python3 ex3/ft_achievement_tracker.py

# Ex4: Dictionary parsing (item:quantity)
python3 ex4/ft_inventory_system.py sword:1 potion:5 shield:2

# Ex5: Lazy Iteration (Generators)
python3 ex5/ft_data_stream.py

# Ex6: Comprehensions (List & Dict transformations)
python3 ex6/ft_data_alchemist.py
```