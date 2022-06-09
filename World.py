from copy import copy
import random
from Cell import Cell
from Event import Event
import Animal


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
            whichOne = random.randint(1, 10)
            if whichOne == 1:
                self.organisms.append(Animal.Antelope(self))
            elif whichOne == 2:
                self.organisms.append(Animal.Fox(self))
            elif whichOne == 3:
                self.organisms.append(Animal.Sheep(self))
            elif whichOne == 4:
                self.organisms.append(Animal.Turtle(self))
            elif whichOne == 5:
                self.organisms.append(Animal.Wolf(self))
            # elif whichOne == 6:
            #     self.organisms.append(Plant.odgsa(self))
            # elif whichOne == 7:
            #     self.organisms.append(Plant.Animal())
            # elif whichOne == 8:
            #     self.organisms.append(Plant.Animal())
            # elif whichOne == 9:
            #     self.organisms.append(Plant.Animal())
            # elif whichOne == 10:
            #     self.organisms.append(Plant.Animal())

    def get_cell(self, x, y):
        return self.terrain[x + self.terrainWidth * y]

    def render_organisms(self):
        for o in self.organisms:
            posX, posY = o.position["x"], o.position["y"]
            self.get_cell(posX, posY).organism = o

    def remove_dead_organisms(self):
        for organism in self.organisms:
            if organism.dead:
                self.organisms.remove(organism)

    def wipe_cells(self):
        for cell in self.terrain:
            cell.organism = 0

    def write_event(self, text, color=(255, 255, 255)):
        self.events.append(Event(text, color))

    def add_organism(self, newborn, birthPos):
        newborn.position = birthPos
        newborn.lastPosition = copy(birthPos)
        newborn.stunned = True
        self.organisms.append(newborn)

    def draw(self):
        self.wipe_cells()
        self.render_organisms()
        for cell in self.terrain:
            cell.draw(self.window)

    def make_actions(self):
        self.organisms.sort(key=lambda o: o.initiative, reverse=True)
        for organism in self.organisms:
            self.events.append(
                Event("This is " + organism.name() + "'s turn.", (192, 192, 192)))
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
