from collections.abc import Callable


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def f(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return f


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:
    def multibale(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return multibale


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def cond(name: str, power: int) -> str:
        if condition(name, power):
            return spell(name, power)
        return "Spell fizzled"

    return cond


def spell_sequence(
    spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:

    def sequence(target: str, power: int) -> list[str]:
        spell_result: list[str] = []

        for i in spells:
            spell_result.append(i(target, power))

        return spell_result

    return sequence


def fire(target: str, power: int) -> str:
    return f"hit {target} with {power} of fire"


def ice(target: str, power: int) -> str:
    return f"hit {target} with {power} of ice"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def condition(target: str, power: int) -> bool:
    return len(target) > 4 and power > 5


if __name__ == "__main__":

    test_targets: list[str] = [
        "Dragon",
        "Goblin",
        "Wizard",
        "Knight",
    ]
    print("Testing spell combiner...")
    combined = spell_combiner(fire, ice)
    result1, result2 = combined(test_targets[1], 44)
    print(f"Combined spell result: {result1}, {result2}")

    mega_fireball = power_amplifier(fire, 3)
    print(mega_fireball(test_targets[0], 4))

    spell_castrer = conditional_caster(condition, fire)
    print(spell_castrer("lion", 88))

    lst_spells = [fire, mega_fireball, ice, heal]
    spell_result = spell_sequence(lst_spells)
    print(spell_result("lion", 44))
