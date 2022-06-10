from copy import copy
import random
from Cell import Cell
from Event import Event
import Animal
import Plant


class World:

    def __init__(self, width, height, terrainWidth, terrainHeight, window):
        self.width = width
        self.height = height
        self.window = window

        self.events = []

        self.terrainWidth, self.terrainHeight = terrainWidth, terrainHeight

        self.terrain = []
        posX, posY = 0, 0
        cellWidth = int(width / terrainWidth)
        cellHeight = int(height / terrainHeight)

        gap = 1
        for c in range(terrainWidth * terrainHeight):
            self.terrain.append(Cell(posX, posY, cellWidth, cellHeight))
            posX += cellWidth + gap
            if c % terrainWidth == terrainWidth - 1:
                posY += cellHeight + gap
                posX = 0

        organismsDensity = 10
        organismsNumber = int(
            organismsDensity * terrainWidth * terrainHeight / 100)

        self.organisms = []

        self.organisms.append(Animal.Human(self))

        for o in range(organismsNumber):
            whichOne = random.randint(1, 11)
            if whichOne == 1:
                self.organisms.append(Animal.Antelope(self))
            elif whichOne == 2:
                self.organisms.append(Animal.Fox(self))
            elif whichOne == 3:
                self.organisms.append(Animal.Sheep(self))
            elif whichOne == 4:
                self.organisms.append(Animal.CyberSheep(self))
            elif whichOne == 5:
                self.organisms.append(Animal.Turtle(self))
            elif whichOne == 6:
                self.organisms.append(Animal.Wolf(self))
            elif whichOne == 7:
                self.organisms.append(Plant.Dandelion(self))
            elif whichOne == 8:
                self.organisms.append(Plant.Grass(self))
            elif whichOne == 9:
                self.organisms.append(Plant.Guarana(self))
            elif whichOne == 10:
                self.organisms.append(Plant.Hogweed(self))
            else:
                self.organisms.append(Plant.Wolfberry(self))

    def get_cell(self, x, y):
        if x < 0 or x >= self.terrainWidth or y < 0 or y >= self.terrainHeight:
            return "OUT_OF_BOUND"
        return self.terrain[x + self.terrainWidth * y]

    def stamp_organisms_on_cells(self):
        for organism in self.organisms:
            posX, posY = organism.position["x"], organism.position["y"]
            if self.get_cell(posX, posY).organism != 0:
                 raise RuntimeError(
                    "stamp_organisms_on_cells: Two organisms on the same cell")
            self.get_cell(posX, posY).organism = organism


    def remove_dead_organisms(self):
        toRemove = []
        for organism in self.organisms:
            if organism.dead:
                toRemove.append(organism)
        for organism in toRemove:
            self.organisms.remove(organism)

    def write_event(self, text, color=(255, 255, 255)):
        self.events.append(Event(text, color))

    def add_organism(self, newborn, birthPos):
        self.get_cell(newborn.position["x"],
                      newborn.position["y"]).organism = 0
        self.get_cell(birthPos["x"], birthPos["y"]).organism = newborn
        newborn.position = copy(birthPos)
        newborn.lastPosition = copy(birthPos)
        newborn.stunned = True
        self.organisms.append(newborn)

    def draw(self):
        for cell in self.terrain:
            cell.draw(self.window)

    def make_actions(self):
        self.organisms.sort(
            key=lambda organism: organism.initiative, reverse=True)
        for organism in self.organisms:
            organism.action()
            self.remove_dead_organisms()

    def get_random_empty_pos(self):
        emptyPositions = []
        for cell in self.terrain:
            if cell.organism == 0:
                newPosition = {"x": int(
                    cell.rect.x / cell.rect.width), "y": int(cell.rect.y / cell.rect.height)}
                emptyPositions.append(newPosition)

        return emptyPositions[random.randint(0, len(emptyPositions) - 1)]

    def get_collider_with(self, attacker):
        posX, posY = attacker.position["x"], attacker.position["y"]
        if self.get_cell(posX, posY).organism == attacker:
            return 0
        return self.get_cell(posX, posY).organism
