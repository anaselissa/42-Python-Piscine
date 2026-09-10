from ex0 import FlameFactory, AquaFactory, CreatureFactory
o_flamefactory = FlameFactory()
o_aquaFactory = AquaFactory()


def test(factory: CreatureFactory) -> bool:
    print("Testing factory")

    try:
        base_ob = factory.create_base()
        evolve_ob = factory.create_evolved()
        print(base_ob.describe())
        print(base_ob.attack())
        print(evolve_ob.describe())
        print(evolve_ob.attack())
        print()
        return True
    except AttributeError as e:
        print(e)
        return False


def fight(fisrt_fact: CreatureFactory, second_fact: CreatureFactory) -> None:

    print("Testing battle")
    base_ob1 = fisrt_fact .create_base()
    base_ob2 = second_fact.create_base()

    print(base_ob1.describe())
    print("vs.")
    print(base_ob2.describe())
    print("fight!")
    print(base_ob1.attack())
    print(base_ob2.attack())


if __name__ == "__main__":
    if (test(o_flamefactory) and test(o_aquaFactory)):
        fight(o_flamefactory, o_aquaFactory)
