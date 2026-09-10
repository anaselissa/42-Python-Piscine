from sys import prefix, base_prefix, executable
import os
import site

if prefix == base_prefix:
    print("MATRIX STATUS: You’re still plugged in\n")
    print(f"Current Python: {executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You’re in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:\n"
          "python -m venv matrix_env\n"
          "source matrix_env/bin/activate # On Unix\n"
          "matrix_env\\Scripts\\activate # On Windows\n\n"
          "Then run this program again.")


else:
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {executable}")
    print(f"Virtual Environment: {os.path.basename(prefix)}")
    print(f"Environment Path: {prefix}\n")
    print("SUCCESS: You’re in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")
    print("Package installation path:")
    print(site.getsitepackages()[1])
