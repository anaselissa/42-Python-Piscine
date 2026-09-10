from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if spells:
        if operation == "add":
            return reduce(add, spells)
        elif operation == "multiply":
            return reduce(mul, spells)
        elif operation == "max":
            return reduce(max, spells)
        elif operation == "min":
            return reduce(min, spells)
        else:
            raise ValueError("the operation is unknown")
    else:
        return 0


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"power is {power} , element is {element}, target is : {target}"


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:
    version1 = partial(base_enchantment, 50, "ice")
    version2 = partial(base_enchantment, 50, "fire")
    version3 = partial(base_enchantment, 50, "Lightning")
    return {"ice": version1, "fire": version2, "lightning": version3}


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    else:
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(data: Any) -> str:
        if data:
            pass
        return "Unknown spell type"

    @dispatcher.register
    def _(data: int) -> str:
        return f"Damage spell: {data} damage"

    @dispatcher.register
    def _(data: str) -> str:
        return f"Enchantment: {data}"

    @dispatcher.register(list)
    def _(data: list[Any]) -> str:
        return f"Multi-cast: {len(data)} spells"

    return dispatcher


if __name__ == "__main__":
    print("Testing spell reducer...")
    try:
        print(spell_reducer([1, 3, 10, 4], "add"))
    except Exception as e:
        print(e)

    print("\nTesting partial enchanter...")
    spell_50_power = partial_enchanter(base_enchantment)

    ice = spell_50_power["ice"]
    fire = spell_50_power["fire"]
    lightning = spell_50_power["lightning"]

    print(ice("lion"))
    print(fire("tiger"))
    print(lightning("fish"))

    print("\nTesting memoized fibonacci...")
    print("Fib(0): ", memoized_fibonacci(0))
    print("Fib(1): ", memoized_fibonacci(1))
    print("Fib(10): ", memoized_fibonacci(10))
    print("Fib(15): ", memoized_fibonacci(15))
    # print(memoized_fibonacci.cache_info())

    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    lst: list[Callable[[str], str]] = [ice, fire, lightning]
    print(dispatcher(lst))
    print(dispatcher({"power": 88}))
