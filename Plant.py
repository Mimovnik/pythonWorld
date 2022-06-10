from copy import copy
import random
import Animal
from Organism import Organism


class Plant(Organism):

    def __init__(self, world, strength, initiative, specie, skin):
        super(Plant, self).__init__(
            world, strength, initiative, specie, skin)
        self.spreadTries = 1

    def action(self):
        if self.dead:
            raise RuntimeError(self + " should be removed before it's action.")
        if self.stunned:
            self.stunned = False
            return
        for i in range(self.spreadTries):
            if random.randint(0, 10) == 1:
                self.spread()

    def spread(self):
        for x in range(3):
            for y in range(3):
                sowPos = {"x": max(min(self.position["x"] + x - 1, self.world.terrainWidth - 1), 0),
                          "y": max(min(self.position["y"] + y - 1, self.world.terrainHeight - 1), 0)}
                if self.world.get_cell(sowPos["x"], sowPos["y"]).organism == 0:
                    self.world.write_event(
                        self.name() + " spreads.", (52, 173, 79))
                    self.world.add_organism(self.get_sapling(), sowPos)
                    return

    def take_hit(self, attacker):
        self.world.write_event(
            self.name() + " got eaten by " + attacker.name() + ".", (255, 0, 0))
        self.die()

    def get_sapling(self):
        raise NotImplementedError("Implement get_sapling method")


class Dandelion(Plant):

    def __init__(self, world):
        super(Dandelion, self).__init__(
            world, 0, 0, "Dandelion", (248, 255, 48))
        self.spreadTries = 3

    def get_sapling(self):
        return Dandelion(self.world)


class Grass(Plant):

    def __init__(self, world):
        super(Grass, self).__init__(
            world, 0, 0, "Grass", (145, 247, 131))

    def get_sapling(self):
        return Grass(self.world)


class Guarana(Plant):

    def __init__(self, world):
        super(Guarana, self).__init__(
            world, 0, 0, "Guarana", (245, 59, 59))

    def get_sapling(self):
        return Guarana(self.world)

    def take_hit(self, attacker):
        self.world.write_event(
            self.name() + " got eaten by " + attacker.name() + ".", (255, 0, 0))
        self.die()
        attacker.buff(3)


class Hogweed(Plant):

    def __init__(self, world):
        super(Hogweed, self).__init__(
            world, 10, 0, "Hogweed", (255, 255, 220))

    def get_sapling(self):
        return Hogweed(self.world)

    def is_stronger(self, other):
        if isinstance(other, Animal.CyberSheep):
            return False
        return True

    def action(self):
        if self.dead:
            raise RuntimeError(self + " should be removed before it's action.")
        if self.stunned:
            self.stunned = False
            return

        self.burn()
        for i in range(self.spreadTries):
            if random.randint(0, 10) == 1:
                self.spread()

    def burn(self):
        for x in range(3):
            for y in range(3):
                burnPos = {"x": max(min(self.position["x"] + x - 1, self.world.terrainWidth - 1), 0),
                           "y": max(min(self.position["y"] + y - 1, self.world.terrainHeight - 1), 0)}
                toBurnOrganism = self.world.get_cell(
                    burnPos["x"], burnPos["y"]).organism
                if toBurnOrganism != 0 and issubclass(type(toBurnOrganism), Animal.Animal) and isinstance(toBurnOrganism, Animal.CyberSheep) == False:
                    self.world.write_event(
                        self.name() + " burns " + toBurnOrganism.name() + ".", (245, 50, 50))
                    toBurnOrganism.take_hit(self)


class Wolfberry(Plant):

    def __init__(self, world):
        super(Wolfberry, self).__init__(
            world, 99, 0, "Wolfberry", (52, 173, 79))

    def get_sapling(self):
        return Wolfberry(self.world)

    def is_stronger(self, other):
        return True
