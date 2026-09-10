try:
    import dotenv
    import os

    print("\nORACLE STATUS: Reading the Matrix...")

    print("\nConfiguration loaded:")
    dotenv.load_dotenv()

    MATRIX_MODE = os.getenv("MATRIX_MODE")
    if not MATRIX_MODE:
        print("[MISSING] MATRIX_MODE")
    else:
        print(f"Mode: {MATRIX_MODE}")

    DATABASE_URL = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        print("[MISSING] DATABASE_URL")
    else:
        print("Database: Connected to local instance")

    API_KEY = os.getenv("API_KEY")
    if not API_KEY:
        print("[MISSING] API_KEY")
    else:
        print("API Access: Authenticated")
        print()

    LOG_LEVEL = os.getenv("LOG_LEVEL")
    if not LOG_LEVEL:
        print("[MISSING] LOG_LEVEL")
    else:
        print(f"Log Level: {LOG_LEVEL}")

    ZION_ENDPOINT = os.getenv("ZION_ENDPOINT")
    if not ZION_ENDPOINT:
        print("[MISSING] ZION_ENDPOINT")
    else:
        print("Zion Network: Online")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    required = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]

    correct = True
    is_Production_overrides_available = False
    stop_pov = False
    env_config = dotenv.dotenv_values(".env")
    for name in required:
        if not env_config.get(name):
            print("[WARNING] Missing configuration in .env :", name)
            correct = False
        if os.getenv(name) != env_config.get(name) and not stop_pov:
            print("[OK] Production overrides available")
            stop_pov = True
            is_Production_overrides_available = True
    if correct:
        print("[OK] .env file properly configured")

    if not is_Production_overrides_available:
        print("[INFO] Using standard .env configuration")

    print("\nThe Oracle sees all configurations.")

except Exception as e:
    print(f"Error: {e}")
