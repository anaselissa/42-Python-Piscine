from collections.abc import Callable
from functools import wraps
from inspect import signature
from time import perf_counter, sleep
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter()
        print(f"Casting {func.__name__}...")
        result = func(*args, **kwargs)
        end_time = perf_counter()
        print(f"Spell completed in {round(end_time - start_time, 3)} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            signature_func = signature(func)
            paramitar = signature_func.bind(*args, **kwargs)
            power = paramitar.arguments["power"]
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i < max_attempts - 1:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {i + 1}/{max_attempts})"
                        )
                    else:
                        return (
                            f"Spell casting failed after "
                            f"{max_attempts} attempts"
                        )
        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        for ch in name:
            if not (ch.isalpha() or ch.isspace()):
                return False
        if len(name) < 3:
            return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        sleep(0.1)
        return "Fireball cast!"

    print("Result: ", fireball())

    print("\nTesting retrying spell...")

    hour = 8

    @retry_spell(3)
    def spill_sleep() -> None:
        global hour
        hour += 1
        if hour <= 9:
            raise Exception("hour should be greater than 9")
        else:
            print(f"hour is {hour}, sleep now")

    @retry_spell(2)
    def print_waaa() -> str:
        return "Waaaaaaagh spelled !"

    print(spill_sleep())
    print(print_waaa())
    print("\nTesting MageGuild...")
    mage1 = MageGuild()

    print(mage1.validate_mage_name("sleep"))
    print(mage1.validate_mage_name("sleep#"))
    if mage1.validate_mage_name("sleep"):
        print(mage1.cast_spell("sleep", 30))
        print(mage1.cast_spell("sleep", 9))
