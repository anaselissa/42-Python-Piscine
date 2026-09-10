# The Matrix
> Welcome to the Real World of Data Engineering

## 🎯 Objective
This project bridges the gap between writing scripts and engineering real-world data systems. The goal is to master the core infrastructure of Python data engineering: isolating workspaces via Virtual Environments, managing external dependencies with `pip` and `Poetry`, and securing sensitive configuration data using Environment Variables.

## 🧠 Technical Concepts Applied
* **Environment Isolation (`venv`):** Inspecting `sys.prefix` and `sys.base_prefix` to detect whether the code is running in the global OS environment (unsafe) or inside an isolated virtual construct (safe).
* **Dynamic Dependency Checking (`importlib`):** Programmatically verifying the presence of heavy data science libraries (`numpy`, `pandas`, `matplotlib`) before execution, and providing graceful fallback instructions instead of fatal crash tracebacks.
* **Package Management (`pip` vs `Poetry`):** Understanding the difference between simple requirements mapping (`requirements.txt`) and deterministic, modern dependency resolution (`pyproject.toml`).
* **Configuration Security (`python-dotenv`):** Completely decoupling configuration from code. Loading variables dynamically from a `.env` file and utilizing OS-level environment variable overrides to seamlessly switch between *Development* and *Production* modes without altering the source code.

### 📐 Visualizing Architecture (The Construct & Data Flow)
To understand why isolating environments and configurations is critical for data pipelines, here is a visual representation of how `oracle.py` handles configuration precedence securely:

```text
[ 🌍 The Matrix (Global OS Environment) ]
   ├── ⚠️ Highly susceptible to version conflicts
   └── ⚠️ Exposes globally installed packages

[ 🏗️ The Construct (Isolated Virtual Environment) ]
   │
   ├── [ Dependency Layer ] ➔ pandas, numpy, matplotlib (Isolated site-packages)
   │
   └── [ Security & Config Pipeline (oracle.py) ]
          │
          ├── 1. Default Fallbacks (Hardcoded / Missing)
          ├── 2. Local Configuration (.env file - ignored by Git)
          │      └─> Mode: Development | DB: Local
          │
          └── 3. OS Runtime Overrides (Top Priority!)
                 └─> MATRIX_MODE=production python3 oracle.py
                     (Overrides the .env securely at runtime)
```

## 🛠️ Usage

This project requires testing across different environment states to observe the behavioral changes.

```bash
# Ex0: Entering the Matrix (Environment Detection)
python3 ex0/construct.py                  # Outside venv (Warning)
python3 -m venv matrix_env                # Create the construct
source matrix_env/bin/activate            # Enter the construct
python3 ex0/construct.py                  # Inside venv (Success)

# Ex1: Loading Programs (Dependency Management)
python3 ex1/loading.py                    # Fails gracefully if packages are missing
pip install -r ex1/requirements.txt       # Install required data libraries
python3 ex1/loading.py                    # Generates matrix_analysis.png using numpy/pandas

# Ex2: Accessing the Mainframe (Secure Configuration)
python3 ex2/oracle.py                     # Warns about missing variables
cp ex2/.env.example ex2/.env              # Setup local configuration
python3 ex2/oracle.py                     # Loads settings from .env
MATRIX_MODE=production python3 ex2/oracle.py # Tests production overrides
```

## 👤 Author

- **Anas Alissa**

- **Campus:** 42 Irbid (Common Core Track)