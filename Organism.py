from copy import copy
import pygame


class Organism:
    counter = 0

    def __init__(self, world, strength, initiative, name, specie, skin):
        Organism.counter += 1
        self.world = world
        self.strength = strength
        self.initiative = initiative
        self.stunned = False
        self.dead = False
        self.skin = skin
        self.name = name
        self.specie = specie
        self.position = world.get_random_empty_pos()
        posX, posY = self.position["x"], self.position["y"]
        world.terrain[posX + world.terrainWidth * posY].organism = self
        self.lastPosition = self.position
        self.birthDate = Organism.counter

    def action(self):
        raise NotImplementedError("Implement Organism action")

    def take_hit(self, attacker):
        raise NotImplementedError("Implement Organism take_hit")

    def is_stronger(self, other):
        return self.strength >= other.strength

    def collide(self, defender):
        if defender.is_stronger(self):
            self.take_hit(defender)
        else:
            defender.take_hit(self)

    def move_back(self):
        self.position = copy(self.lastPosition)
