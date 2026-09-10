if __name__ == "__main__":
    import importlib

    print("LOADING STATUS: Loading programs...\n")

    packages = ["numpy", "pandas", "matplotlib"]
    missing = False

    for package in packages:
        try:
            module = importlib.import_module(package)
            print(f"[OK] {package} ({module.__version__})", end="")
            if package == "numpy":
                print(" - Numerical computation ready")
            if package == "pandas":
                print(" - Data manipulation ready")
            if package == "matplotlib":
                print(" - Visualization ready")
        except ModuleNotFoundError:
            print(f"[MISSING] {package}")
            missing = True

    if missing:
        print("\nMissing dependencies detected!")
        print("To install with pip:")
        print("pip install -r requirements.txt")
        print("To install with Poetry:")
        print("pip install poetry")
        print("poetry install")
    else:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        print("\nAnalyzing Matrix data...")
        data = np.random.rand(1000)
        df = pd.DataFrame(data, columns=["value"])

        print("Processing 1000 data points...")
        plt.hist(df["value"])
        print("Generating visualization...")

        plt.savefig("matrix_analysis.png")
        plt.close()
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
