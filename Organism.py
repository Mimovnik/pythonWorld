import pygame


class Organism:
    counter = 0

    def __init__(self, world, strength, initiative, name, specie):
        Organism.counter += 1
        self.world = world
        self.strength = strength
        self.initiative = initiative
        self.stunned = False
        self.dead = False
        self.skin = (255, 0, 0)
        self.name = name
        self.specie = specie
        self.position = world.get_random_empty_pos()
        posX, posY = self.position["x"], self.position["y"]
        world.terrain[posX + world.terrainWidth * posY].organism = self
        self.lastPosition = self.position
        self.birthDate = Organism.counter


    def action(self):
        raise NotImplementedError("Implement Organism action") 
