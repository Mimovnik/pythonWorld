import random
import pygame
import Cell
import Organism


class World:

    def __init__(self, width, height, terrainWidth, terrainHeight, window):
        self.width = width
        self.height = height
        self.window = window

        self.terrainWidth, self.terrainHeight = terrainWidth, terrainHeight

        self.terrain = []
        posX, posY = 0, 0
        cellWidth = int(width / terrainWidth)
        cellHeight = int(height / terrainHeight)

        gap = 1
        for c in range(terrainWidth * terrainHeight):
            self.terrain.append(Cell.Cell(posX, posY, cellWidth, cellHeight))
            posX += cellWidth + gap
            if c % terrainWidth == terrainWidth - 1:
                posY += cellHeight + gap
                posX = 0

        organismsDensity = 10
        organismsNumber = int(
            organismsDensity * terrainWidth * terrainHeight / 100)

        self.organisms = []

        # self.organisms.append(Human(self))

        for o in range(organismsNumber):
            whichOne = random.randint(1, 10)
            if whichOne == 1:
                self.organisms.append(Organism.Organism(
                    self, 0, 0, "name", "specie"))
            elif whichOne == 2:
                self.organisms.append(Organism.Organism(
                    self, 0, 0, "name", "specie"))
            elif whichOne == 3:
                self.organisms.append(Organism.Organism(
                    self, 0, 0, "name", "specie"))
            elif whichOne == 4:
                self.organisms.append(Organism.Organism(
                    self, 0, 0, "name", "specie"))
            elif whichOne == 5:
                self.organisms.append(Organism.Organism(
                    self, 0, 0, "name", "specie"))
            elif whichOne == 6:
                self.organisms.append(Organism.Organism(
                    self, 0, 0, "name", "specie"))
            elif whichOne == 7:
                self.organisms.append(Organism.Organism(
                    self, 0, 0, "name", "specie"))
            elif whichOne == 8:
                self.organisms.append(Organism.Organism(
                    self, 0, 0, "name", "specie"))
            elif whichOne == 9:
                self.organisms.append(Organism.Organism(
                    self, 0, 0, "name", "specie"))
            elif whichOne == 10:
                self.organisms.append(Organism.Organism(
                    self, 0, 0, "name", "specie"))

    def render_organisms(self):
        for o in self.organisms:
            posX, posY = o.position["x"], o.position["y"]
            self.terrain[posX + self.terrainWidth * posY].organism = o

    def draw(self):
        self.render_organisms()
        for cell in self.terrain:
            cell.draw(self.window)

    def get_random_empty_pos(self):
        emptyPositions = []
        for cell in self.terrain:
            if cell.organism == 0:
                emptyPositions.append(
                    {"x": int(cell.rect.x / cell.rect.width), "y": int(cell.rect.y / cell.rect.height)})

        return emptyPositions[random.randint(0, len(emptyPositions))]
