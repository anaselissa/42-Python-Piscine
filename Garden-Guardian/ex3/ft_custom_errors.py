class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown Plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown Water error") -> None:
        super().__init__(message)


def plant_check() -> None:
    print("Testing PlantError...")
    raise PlantError("The tomato plant is wilting!")


def water_check() -> None:
    print("Testing WaterError...")
    raise WaterError("Not enough water in the tank!")


def test_error() -> None:
    try:
        plant_check()
    except PlantError as e:
        print("Caught PlantError:", e)
        print()
    try:
        water_check()
    except WaterError as e:
        print("Caught WaterError:", e)
        print()
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print("Caught GardenError:", e)
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print("Caught GardenError:", e)
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_error()
