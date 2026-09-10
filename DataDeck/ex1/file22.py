from ex0 import CreatureFactory, Creature
from .file21 import Bloomelle, Sproutling, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        o_sproutling = Sproutling("Sproutling", "Grass")
        return o_sproutling

    def create_evolved(self) -> Creature:
        o_bloomell = Bloomelle("Bloomelle", "Grass/Fairy")
        return o_bloomell


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> Creature:
        return Morphagon("Morphagon", "Normal/Dragon")
