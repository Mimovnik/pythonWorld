from copy import copy
import random
from Organism import Organism


class Plant(Organism):

    def __init__(self, world, strength, initiative, specie, skin):
        super(Plant, self).__init__(
            world, strength, initiative, specie, skin)
        self.spreadTries = 1

    def action(self):
        if self.stunned:
            self.stunned = False
            return
        for i in range(self.spreadTries):
            if self.dead:
                return
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
            self.name() + " got eaten by " + attacker.name() + " and died.", (255, 0, 0))
        self.dead = True

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


class Hogweed(Plant):

    def __init__(self, world):
        super(Hogweed, self).__init__(
            world, 0, 0, "Hogweed", (255, 255, 220))

    def get_sapling(self):
        return Hogweed(self.world)


class Wolfberry(Plant):

    def __init__(self, world):
        super(Wolfberry, self).__init__(
            world, 0, 0, "Wolfberry", (52, 173, 79))

    def get_sapling(self):
        return Wolfberry(self.world)
