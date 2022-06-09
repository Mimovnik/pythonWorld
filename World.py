import random
import Cell
import Antelope
import Animal


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

        gap = 0
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
                self.organisms.append(Antelope.Antelope(self))
            elif whichOne == 2:
                self.organisms.append(Animal.Animal(
                    self, 0, 0, "name", "specie", (255, 0, 0)))
            elif whichOne == 3:
                self.organisms.append(Animal.Animal(
                    self, 0, 0, "name", "specie", (255, 0, 0)))
            elif whichOne == 4:
                self.organisms.append(Animal.Animal(
                    self, 0, 0, "name", "specie", (255, 0, 0)))
            elif whichOne == 5:
                self.organisms.append(Animal.Animal(
                    self, 0, 0, "name", "specie", (255, 0, 0)))
            elif whichOne == 6:
                self.organisms.append(Animal.Animal(
                    self, 0, 0, "name", "specie", (255, 0, 0)))
            elif whichOne == 7:
                self.organisms.append(Animal.Animal(
                    self, 0, 0, "name", "specie", (255, 0, 0)))
            elif whichOne == 8:
                self.organisms.append(Animal.Animal(
                    self, 0, 0, "name", "specie", (255, 0, 0)))
            elif whichOne == 9:
                self.organisms.append(Animal.Animal(
                    self, 0, 0, "name", "specie", (255, 0, 0)))
            elif whichOne == 10:
                self.organisms.append(Animal.Animal(
                    self, 0, 0, "name", "specie", (255, 0, 0)))

    def render_organisms(self):
        for o in self.organisms:
            posX, posY = o.position["x"], o.position["y"]
            self.terrain[posX + self.terrainWidth * posY].organism = o

    def remove_dead_organisms(self):
        for organism in self.organisms:
            if organism.dead:
                self.organisms.remove(organism)

    def wipe_cells(self):
        for cell in self.terrain:
            cell.organism = 0

    def draw(self):
        self.wipe_cells()
        self.render_organisms()
        for cell in self.terrain:
            cell.draw(self.window)

    def make_actions(self):
        for organism in self.organisms:
            organism.action()
            self.remove_dead_organisms()
            self.draw()

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
        if self.terrain[posX + self.terrainWidth * posY].organism == attacker:
            return 0
        return self.terrain[posX + self.terrainWidth * posY].organism
