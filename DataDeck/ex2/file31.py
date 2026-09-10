import typing
from abc import ABC, abstractmethod

from ex0 import Creature
from ex1.file21 import HealCapability, TransformCapability


class InvaledInput(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
        else:
            raise InvaledInput("invaled input : the input not creature ")


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        else:
            return False

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            capable_creature = typing.cast(TransformCapability, creature)
            print(capable_creature.transform())
            print(creature.attack())
            print(capable_creature.revert())
        else:
            raise InvaledInput(
                f"Battle error, aborting tournament: Invalid Creature "
                f"’{creature.name}’ for this aggressive strategy"
            )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        else:
            return False

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            capable_creature = typing.cast(HealCapability, creature)
            print(creature.attack())
            print(capable_creature.heal())
        else:
            raise InvaledInput(
                f"Battle error, aborting tournament: Invalid Creature "
                f"’{creature.name}’ for this defensive strategy"
            )
