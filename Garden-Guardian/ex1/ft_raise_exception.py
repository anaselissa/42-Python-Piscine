def input_temperature(temp_str: str) -> int:
    print(f"Input data is ’{temp_str}’")
    temperature_value = int(temp_str)

    if temperature_value > 40:
        raise Exception(f"{temperature_value}°C is"
                        " too hot for plants (max 40°C)")
    if temperature_value < 0:
        raise Exception(f"{temperature_value}°C is"
                        " too cold for plants (min 0°C)")
    print(f"Temperature is now {temperature_value}°C\n")

    return (temperature_value)


def test_temperature() -> None:
    try:
        input_temperature("25")
    except Exception as e:
        print("Caught input_temperature error: "
              f"{e}\n")
    try:
        input_temperature("abc")
    except Exception as e:
        print("Caught input_temperature error: "
              f"{e}\n")
    try:
        input_temperature("100")
    except Exception as e:
        print("Caught input_temperature error: "
              f"{e}\n")
    try:
        input_temperature("-50")
    except Exception as e:
        print("Caught input_temperature error: "
              f"{e}\n")
    print("All tests completed - program didn’t crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
