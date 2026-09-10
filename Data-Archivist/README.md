# 🗃️ Data Archivist

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Topic](https://img.shields.io/badge/Topic-File_Systems-orange.svg)
![Topic](https://img.shields.io/badge/Topic-Context_Managers-brightgreen.svg)

> **Digital Preservation in the Cyber Archives**

## 🎯 Objective
This project explores the critical domain of file operations and stream management in Python. The goal is to build robust systems capable of reading, creating, and securing data archives while gracefully handling missing files, permission errors, and resource leaks.

---

## 🧠 Core Concepts
* **Standard File I/O (`open`, `read`, `write`, `close`):** Accessing and modifying file contents dynamically while intercepting OS-level errors (`FileNotFoundError`, `PermissionError`).
* **Advanced Stream Management (`sys` module):** Bypassing standard `print()` and `input()` by directly manipulating `sys.stdout`, `sys.stdin`, and `sys.stderr` for precise control over where data and errors flow.
* **Buffer Flushing (`flush`):** Enforcing immediate data output to terminal or files to ensure absolute data integrity, preventing asynchronous write delays during critical operations.
* **Context Managers (`with` statement):** Architecting secure data vaults. The `with` keyword acts as a fail-safe, guaranteeing that file descriptors are safely closed and resources are released, even if a fatal exception occurs during the read/write process.

---

## 📐 Architecture: Vault Security (`with` Statement)
In `ex3` (Vault Security), we transition from manual `.close()` calls to Python's Context Managers. Here is how memory and file descriptors are protected under the hood:

```text
[ Traditional I/O: High Risk of Resource Leaks ]
open() ➔ read() ➔ [ ERROR CRASH ] ➔ .close() is NEVER executed! (File locked in memory)

[ Context Manager (with): Absolute Security ]
with open() 
   ├── read() / write()
   └── [ ERROR CRASH ] ➔ Context Manager Intercepts ➔ Auto-closes file ➔ Raises Exception
```

## 🛠️ Usage

The project includes several data recovery and preservation scripts. Execute them via the terminal:

```bash
# Ex0: Ancient Text Recovery (Basic File Reading & Error Handling)
python3 ex0/ft_ancient_text.py <file_name>

# Ex1: Archive Creation (Reading, Transforming, and Writing Data)
python3 ex1/ft_archive_creation.py <file_name>

# Ex2: Stream Management (Using sys.stdin, sys.stdout, sys.stderr)
python3 ex2/ft_stream_management.py <file_name>

# Ex3: Vault Security (Testing secure_archive via Context Managers)
python3 ex3/ft_vault_security.py
```

## 👤 Author

- **Anas Alissa**
- **Campus:** 42 Irbid (Common Core Track)

