from array import array
import random

import pygame
import Organism


class World:
    def __init__(self, width, height, terrainWidth, terrainHeight, window):
        self.width = width
        self.height = height
        self.window = window

        self.terrain = []
        posX, posY = 0, 0
        cellWidth = int(width / terrainWidth)
        cellHeight = int(height / terrainHeight)

        gap = 1
        for c in range(terrainWidth * terrainHeight):
            self.terrain.append(pygame.Rect(posX, posY, cellWidth, cellHeight))
            posX += cellWidth + gap
            if c % terrainWidth == terrainWidth - 1:
                posY += cellHeight + gap
                posX = 0

        organismsDensity = 10
        organismsNumber = organismsDensity * width * height / 100

        self.organisms = []

        # self.organisms.append(Human(self))

        # for organism in organismsNumber:
        #     whichOne = random.randint(1, 10)
        #     if whichOne == 1:
        #         self.organisms.append(1)
        #     elif whichOne == 2:
        #         self.organisms.append(1)
        #     elif whichOne == 3:
        #         self.organisms.append(1)
        #     elif whichOne == 4:
        #         self.organisms.append(1)
        #     elif whichOne == 5:
        #         self.organisms.append(1)
        #     elif whichOne == 6:
        #         self.organisms.append(1)
        #     elif whichOne == 7:
        #         self.organisms.append(1)
        #     elif whichOne == 8:
        #         self.organisms.append(1)
        #     elif whichOne == 9:
        #         self.organisms.append(1)
        #     elif whichOne == 10:
        #         self.organisms.append(1)

    def draw(self):
        for cell in self.terrain:
            pygame.draw.rect(self.window, (155, 253, 233), cell)
