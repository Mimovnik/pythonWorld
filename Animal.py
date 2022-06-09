from copy import copy
import random
import Organism


class Animal(Organism.Organism):

    def __init__(self, world, strength, initiative, name, specie):
        self.moveRange = 1
        self.attackedThisTurn = False
        super(Animal, self).__init__(world, strength, initiative, name, specie)

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
                    # self.breed(defender)
                    return
                self.attackedThisTurn = True
                self.collide(defender)

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
