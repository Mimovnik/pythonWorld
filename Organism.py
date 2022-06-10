from copy import copy
import pygame


class Organism:
    counter = 0

    def __init__(self, world, strength, initiative, specie, skin):
        Organism.counter += 1
        self.world = world
        self.strength = strength
        self.initiative = initiative
        self.stunned = False
        self.dead = False
        self.skin = skin
        self.specie = specie
        self.position = world.get_random_empty_pos()
        posX, posY = self.position["x"], self.position["y"]
        world.get_cell(posX, posY).organism = self
        self.lastPosition = self.position
        self.birthDate = Organism.counter

    def to_string(self):
        return self.specie + "," + \
            str(self.position["x"]) + "," + str(self.position["y"]) + "," + \
            str(self.lastPosition["x"]) + "," + str(self.lastPosition["y"]) + "," + \
            str(self.birthDate) + "," + str(self.strength)

    def load(self, position, lastPosition, birthDate, strength):
        posX, posY = self.position["x"], self.position["y"]
        self.world.get_cell(posX, posY).organism = 0 
        self.position = position
        self.lastPosition = lastPosition
        self.birthDate = birthDate
        self.strength = strength
        posX, posY = self.position["x"], self.position["y"]
        self.world.get_cell(posX, posY).organism = self 

    def name(self):
        return self.specie + "(" + str(self.birthDate) + ")"

    def action(self):
        raise NotImplementedError("Implement Organism action")

    def update_position(self):
        self.world.get_cell(self.lastPosition["x"],
                            self.lastPosition["y"]).organism = 0
        self.world.get_cell(self.position["x"],
                            self.position["y"]).organism = self

    def take_hit(self, attacker):
        raise NotImplementedError("Implement Organism take_hit")

    def die(self):
        self.dead = True
        self.world.get_cell(
            self.position["x"], self.position["y"]).organism = 0

    def buff(self, additionalStrength):
        self.strength += additionalStrength
        self.world.write_event(
            self.name() + " got +" + str(additionalStrength) + " strength.", (0, 255, 0))
        self.world.write_event(
            "Total(" + str(self.strength) + ").", (0, 255, 0))

    def is_stronger(self, other):
        return self.strength >= other.strength

    def collide(self, defender):
        if defender.is_stronger(self):
            self.take_hit(defender)
        else:
            defender.take_hit(self)

    def move_back(self):
        self.position = copy(self.lastPosition)
