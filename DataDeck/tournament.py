from ex0 import AquaFactory, FlameFactory, CreatureFactory
from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex2.file31 import (
    AggressiveStrategy,
    NormalStrategy,
    InvaledInput,
    DefensiveStrategy,
    BattleStrategy
)


def main() -> None:

    o_aqua = AquaFactory()
    o_flame = FlameFactory()
    o_transform = TransformCreatureFactory()
    o_heal = HealingCreatureFactory()
    o_norm_strat = NormalStrategy()
    o_aggres_strat = AggressiveStrategy()
    o_defens_strat = DefensiveStrategy()

    def fight(fighter: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
        print("*** Tournament ***")
        print(f"{len(fighter)} opponents involved")
        creatures_list = []
        for factory, strategy in fighter:
            creatures_list.append((factory.create_base(), strategy))

        for i, (creator, strategy) in enumerate(creatures_list):
            for creator2, strategy2 in creatures_list[i + 1:]:
                print()
                print("* Battle *")
                print(creator.describe())
                print("VS.")
                print(creator2.describe())
                print("now fight!")
                strategy.act(creator)
                strategy2.act(creator2)

    try:
        print("Tournament 0 (basic)")
        lst_creature1 = [(o_flame, o_norm_strat), (o_heal, o_defens_strat)]
        print("[ (Flameling+Normal), (Healing+Defensive) ]")
        fight(lst_creature1)

        print("Tournament 1 (error)")
        lst_creature2 = [(o_flame, o_aggres_strat), (o_heal, o_defens_strat)]
        print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
        fight(lst_creature2)

    except InvaledInput as e:
        print(e)

    try:
        print("Tournament 2 (multiple)")
        lst_creature3 = [
            (o_aqua, o_norm_strat),
            (o_heal, o_defens_strat),
            (o_transform, o_aggres_strat)
        ]
        print("[ (Aquabub+Normal),"
              " (Healing+Defensive), (Transform+Aggressive) ]")
        fight(lst_creature3)
    except InvaledInput as e:
        print(e)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
