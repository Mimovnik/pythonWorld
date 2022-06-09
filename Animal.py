from copy import copy
from Event import Event
import random
import Organism


class Animal(Organism.Organism):

    def __init__(self, world, strength, initiative, specie, skin):
        super(Animal, self).__init__(
            world, strength, initiative, specie, skin)
        self.moveRange = 1
        self.attackedThisTurn = False

    def action(self):
        self.attackedThisTurn = False
        if(self.stunned):
            self.stunned = False
            return

        direction = self.get_direction()

        for i in range(self.moveRange):
            if self.dead:
                return

            self.lastPosition = copy(self.position)
            self.move(direction)
            defender = self.world.get_collider_with(self)
            if defender != 0:
                if defender.specie == self.specie:
                    self.breed(defender)
                    return
                self.attackedThisTurn = True
                self.world.write_event(
                    self.name() + " attacks " + defender.name() + ".", (255, 120, 0))
                self.collide(defender)

    def breed(self, partner):
        self.move_back()
        if random.randint(0, 1) == 1:
            return

        for x in range(3):
            for y in range(3):
                birthPos = {"x": min(self.position["x"] + x - 1, self.world.terrainWidth - 1),
                            "y": min(self.position["y"] + y - 1, self.world.terrainHeight - 1)}
                if self.world.get_cell(birthPos["x"], birthPos["y"]).organism == 0:
                    self.world.write_event(
                        self.name() + " has a baby with " + partner.name() + ".", (249, 93, 204))
                    self.world.add_organism(self.give_birth(), birthPos)
                    return

    def give_birth(self):
        raise NotImplementedError("Implement give_birth method")

    def take_hit(self, attacker):
        self.world.write_event(
            self.name() + " took a hit from " + attacker.name() + " and died.", (255, 0, 0))
        self.dead = True

    def move(self, direction):
        if direction == "NOWHERE":
            return
        elif direction == "LEFT":
            if self.position["x"] > 0:
                self.position["x"] -= 1
        elif direction == "RIGHT":
            if self.position["x"] + 1 < self.world.terrainWidth:
                self.position["x"] += 1
        elif direction == "UP":
            if self.position["y"] > 0:
                self.position["y"] -= 1
        else:
            if self.position["y"] + 1 < self.world.terrainHeight:
                self.position["y"] += 1

    def get_direction(self):
        rnd = random.randint(1, 4)
        if rnd == 1:
            return "LEFT"
        elif rnd == 2:
            return "UP"
        elif rnd == 3:
            return "RIGHT"
        else:
            return "DOWN"


class Antelope(Animal):

    def __init__(self, world):
        super(Antelope, self).__init__(world, 4, 4, "Antelope", (238, 182, 95))
        self.moveRange = 2

    def give_birth(self):
        return Antelope(self.world)


class Fox(Animal):

    def __init__(self, world):
        super(Fox, self).__init__(world, 3, 7, "Fox", (247, 150, 0))

    def give_birth(self):
        return Fox(self.world)


class Human(Animal):

    def __init__(self, world):
        super(Human, self).__init__(world, 5, 4, "Human", (255, 195, 170))

    def give_birth(self):
        return Human(self.world)


class Sheep(Animal):

    def __init__(self, world):
        super(Sheep, self).__init__(world, 4, 4, "Sheep", (231, 232, 168))

    def give_birth(self):
        return Sheep(self.world)


class Turtle(Animal):

    def __init__(self, world):
        super(Turtle, self).__init__(world, 2, 1, "Turtle", (28, 138, 7))

    def give_birth(self):
        return Turtle(self.world)


class Wolf(Animal):

    def __init__(self, world):
        super(Wolf, self).__init__(world, 9, 5, "Wolf", (144, 144, 144))

    def give_birth(self):
        return Wolf(self.world)
