from array import array
import random
import Organism


class World:
    def __init__(self, width, height, window):
        self.width = width
        self.height = height
        self.window = window
        self.terrain = array()

        organismsDensity = 10
        organismsNumber = organismsDensity * width * height / 100

        self.organisms = list(Organism.Organism)
        # self.organisms.append(Human(self))

        for organism in self.organisms:
            whichOne = random.randint(1, 10)
            if whichOne == 1:
                self.organisms.append(1)
            elif whichOne == 2:
                self.organisms.append(1)
            elif whichOne == 3:
                self.organisms.append(1)
            elif whichOne == 4:
                self.organisms.append(1)
            elif whichOne == 5:
                self.organisms.append(1)
            elif whichOne == 6:
                self.organisms.append(1)
            elif whichOne == 7:
                self.organisms.append(1)
            elif whichOne == 8:
                self.organisms.append(1)
            elif whichOne == 9:
                self.organisms.append(1)
            elif whichOne == 10:
                self.organisms.append(1)