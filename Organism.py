import pygame


class Organism:
    counter = 0

    def __init__(self, world, strength, initiative, name, specie):
        Organism.counter += 1
        self.world = world
        self.strength = strength
        self.initiative = initiative
        self.skin = (255, 0, 0)
        self.name = name
        self.specie = specie
        self.position = world.get_random_empty_pos()
        self.lastPosition = self.position
        self.birthDate = Organism.counter
        # raise NotImplementedError("Implement this method")
