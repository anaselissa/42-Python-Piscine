# Code Nexus
> Polymorphic Data Streams in the Digital Matrix

## 🎯 Objective
This project demonstrates the power of Object-Oriented Programming (OOP) in architectural design. The goal is to build an adaptive, real-time data processing pipeline that dynamically routes, ingests, and exports multiple data types using Abstract Base Classes (ABC), Method Overriding, and Subtype Polymorphism.

## 🧠 Technical Concepts Applied
* **Abstract Base Classes (ABC):** Defining a strict blueprint (`DataProcessor`) using the `@abstractmethod` decorator to enforce a standardized interface across all child classes.
* **Method Overriding:** Customizing the inherited `validate()` and `ingest()` methods within specialized classes (`NumericProcessor`, `TextProcessor`, `LogProcessor`) to handle type-specific logic.
* **Subtype Polymorphism:** Allowing the `DataStream` controller to iterate over a generic list of processors and execute `.validate()` and `.ingest()` without needing to know the concrete type of the object it is interacting with.
* **Structural Subtyping (Duck Typing):** Utilizing `typing.Protocol` to define an `ExportPlugin` interface. The `CSVPlugin` and `JSONPlugin` fulfill this contract based on their behavior (methods) rather than explicit inheritance, making the output pipeline highly extensible.

### 📐 Visualizing Polymorphism (Data Routing Architecture)
To understand how Subtype Polymorphism and Protocols eliminate the need for massive `if/else` chains, here is the architectural flow of the `DataStream` pipeline:

```text
[ Incoming Stream: Mixed Integers, Strings, and Dictionaries ]
                             │
                             ▼
              (DataStream Router Controller)
         Iterates registered processors and calls .validate(data)
                             │
           ┌─────────────────┼─────────────────┐
       Matches           Matches           Matches
           ▼                 ▼                 ▼
  [NumericProcessor]  [TextProcessor]   [LogProcessor]  (Inherits from ABC)
           │                 │                 │
           ▼                 ▼                 ▼
      [CSVPlugin]       [JSONPlugin]      [CSVPlugin]   (Complies with Protocol)
```

## 🛠️ Usage

The repository is structured incrementally, from basic processor creation to a fully integrated pipeline.

Run the modules via the terminal:

```bash
# Ex0: Data Processor (Testing ABC and Method Overriding)
python3 ex0/data_processor.py

# Ex1: Data Stream (Polymorphic routing of mixed data types)
python3 ex1/data_stream.py

# Ex2: Data Pipeline (Exporting processed data using Duck Typing plugins)
python3 ex2/data_pipeline.py
```

## 👤 Author

- **Anas Alissa**

- **Campus:** 42 Irbid (Common Core Track)