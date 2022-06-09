import pygame


class BattleLog:

    def __init__(self, x):
        self.x = x
        self.FONT = pygame.font.SysFont("Noto Sans", 12)

    def draw(self, events, WIN):
        row = 0
        for event in events:
            entry = self.FONT.render(event.text, True, (0, 0, 0))
            entry.fill(event.color)
            WIN.blit(entry, (self.x, row))
            entry = self.FONT.render(event.text, True, (0, 0, 0))
            WIN.blit(entry, (self.x, row))
            row += 15

