# Cosmic Data
> Pydantic Models, Data Validation & Nested Structures

## 🎯 Objective
This project explores the implementation of robust data validation pipelines using `Pydantic v2`. Set within a cosmic theme, the goal is to enforce strict data integrity rules, handle type coercion, and manage complex hierarchical data structures (nested models) safely and predictably.

## 🧠 Technical Concepts Applied
* **Schema Definition (`BaseModel` & `Field`):** Establishing strict data contracts with built-in constraints such as `min_length`, `max_length`, `ge` (greater than or equal), and `le` (less than or equal).
* **Enumerations (`Enum`):** Restricting variable states to predefined sets (e.g., `ContactType`, `Rank`) to eliminate typos and invalid categorizations.
* **Cross-Field Business Logic (`@model_validator`):** Utilizing `mode="after"` validators to enforce complex rules that depend on the relationship between multiple fields (e.g., rejecting telepathic alien contacts if there are fewer than 3 witnesses).
* **Nested Object Validation:** Embedding models within models (e.g., a `list[CrewMember]` inside a `SpaceMission`). The validation engine aggregates child data to enforce parent-level constraints (e.g., ensuring a mission has at least one Commander, or verifying experience ratios across the crew).

### 📐 Visualizing the Pydantic Validation Lifecycle
To understand how Pydantic processes raw incoming data (e.g., from a JSON payload or API request) into safe Python objects, here is the architectural pipeline:

```text
[ Raw Input Dictionary / Keyword Args ]
                 │
                 ▼
 ┌───────────────────────────────┐
 │ 1. Type Coercion & Casting    │ ──(Fails)──> [ ValidationError ]
 │ (e.g., "42" -> int(42))       │
 └───────────────┬───────────────┘
                 ▼
 ┌───────────────────────────────┐
 │ 2. Field-Level Constraints    │ ──(Fails)──> [ ValidationError ]
 │ (e.g., ge=0, max_length=15)   │
 └───────────────┬───────────────┘
                 ▼
 ┌───────────────────────────────┐
 │ 3. @model_validator (after)   │ ──(Fails)──> [ ValueError -> ValidationError ]
 │ (Custom Business Rules)       │
 └───────────────┬───────────────┘
                 ▼
 [ Validated & Safe Python Object ]
```

## 🛠️ Usage

The project contains progressively complex validation schemas. Execute the scripts to see valid object instantiation alongside intercepted `ValidationErrors`.

```bash
# Ex0: Basic Validation (Testing Field constraints and type safety)
python3 ex0/space_station.py

# Ex1: Cross-Field Validation (Testing Enums and custom @model_validator logic)
python3 ex1/alien_contact.py

# Ex2: Nested Models (Testing parent-child relationship constraints)
python3 ex2/space_crew.py
```

## 👤 Author

- **Anas Alissa**

- **Campus:** 42 Irbid (Common Core Track)