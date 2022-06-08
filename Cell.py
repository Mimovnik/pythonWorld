import pygame


class Cell:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.organism = 0

    def draw(self, window):
        if self.organism == 0:
            pygame.draw.rect(window, (155, 253, 233), self.rect)
        else:
            pygame.draw.rect(window, self.organism.skin, self.rect)