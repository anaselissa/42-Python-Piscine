import typing
from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex1.file21 import HealCapability, TransformCapability


def test_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    try:
        print("base:")
        o_hb = factory.create_base()
        print(o_hb.describe())
        print(o_hb.attack())
        print(typing.cast(HealCapability, o_hb).heal())

        print("evolved:")
        o_he = factory.create_evolved()
        print(o_he.describe())
        print(o_he.attack())
        print(typing.cast(HealCapability, o_he).heal())

    except AttributeError as e:
        print("Erorr : " + e.__str__())


def test_transform(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    try:
        print("base:")
        o_tb = factory.create_base()
        print(o_tb.describe())
        print(o_tb.attack())
        print(typing.cast(TransformCapability, o_tb).transform())
        print(o_tb.attack())
        print(typing.cast(TransformCapability, o_tb).revert())

        print("evolved:")
        o_te = factory.create_evolved()
        print(o_te.describe())
        print(o_te.attack())
        print(typing.cast(TransformCapability, o_te).transform())
        print(o_te.attack())
        print(typing.cast(TransformCapability, o_te).revert())

    except AttributeError as e:
        print("Erorr : " + e.__str__())


if __name__ == "__main__":
    o_heal = HealingCreatureFactory()
    test_healing(o_heal)

    o_transform = TransformCreatureFactory()
    test_transform(o_transform)
