class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown Plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if (plant_name != str.capitalize(plant_name)):
        raise PlantError("Invalid plant name to water: "
                         f"’{plant_name}’")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print("Caught PlantError: ", e)
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print("Caught PlantError: ", e)
        print(".. ending tests and returning to main")
        return

    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("Cleanup always happens, even with errors!")
