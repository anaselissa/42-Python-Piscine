from abc import ABC, abstractmethod
from .file1 import Flameling, Pyrodon, Aquabub, Torragon, Creature


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        o_flameling = Flameling("Flameling", "Fire")
        return o_flameling

    def create_evolved(self) -> Creature:
        o_pyrdon = Pyrodon("Pyrodon", "Fire/Flying")
        return o_pyrdon


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        o_aquabub = Aquabub("Aquabub", "Water")
        return o_aquabub

    def create_evolved(self) -> Creature:
        o_torrago = Torragon("Torragon", "Water")
        return o_torrago
