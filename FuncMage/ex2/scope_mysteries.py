from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count_return = 0

    def counter() -> int:
        nonlocal count_return
        count_return += 1
        return count_return

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    initial = initial_power

    def accumulate(amount: int) -> int:
        nonlocal initial
        initial += amount
        return initial

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} :  {item_name} "

    return enchant


def memory_vault() -> dict[str, Callable[..., Any]]:
    dic_memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> str:
        nonlocal dic_memory
        dic_memory[key] = value
        return f"Store ’{key}’ = {value}"

    def recall(key: str) -> Any:
        return dic_memory.get(key, "Memory not found")

    dic_ret_fun: dict[str, Callable[..., Any]] = {
        "store": store,
        "recall": recall
        }
    return dic_ret_fun


print("Testing mage counter...\n")
mage_count_a = mage_counter()
mage_count_b = mage_counter()

print("counter_a call 1: ", mage_count_a())
print("counter_a call 2: ", mage_count_a())
print("counter_b call 1: ", mage_count_b())

# # -------------------
print("\nTesting spell accumulator...")

spell_accumulat = spell_accumulator(100)

print("Base 100, add 20: ", spell_accumulat(20))
print("Base 100, add 30: ", spell_accumulat(30))


# -------------------------

print("\nTesting memory vault...")
mem_vault = memory_vault()
store = mem_vault["store"]
recall = mem_vault["recall"]

print(store("secret", 42))

print("Recall ’secret’: ", recall("secret"))
print("Recall ’unknown’ : ", recall("unknown"))

# # ----------


fire = enchantment_factory("Flaming")
ice = enchantment_factory("Frozen")
poison = enchantment_factory("Poison")

print(fire("Sword"))
print(ice("Bow"))
