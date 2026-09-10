from abc import ABC, abstractmethod
from ex0 import Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.persistent_state = True

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        TransformCapability.__init__(self)
        super().__init__(name, type)

    def attack(self) -> str:
        if self.persistent_state:
            return "Shiftling attacks normally"
        else:
            return "Shiftling performs a boosted strike!"

    def transform(self) -> str:
        self.persistent_state = False
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self.persistent_state = True
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        Creature.__init__(self, name, type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.persistent_state:
            return "Morphagon attacks normally"
        else:
            return "Morphagon unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.persistent_state = False
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.persistent_state = True
        return "Morphagon stabilizes its form."
