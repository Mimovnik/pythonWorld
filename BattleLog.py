import pygame


class BattleLog:

    def __init__(self):
        self.FONT = pygame.font.SysFont("Noto Sans", 12)

    def draw(self, events, WIN):
        row = 0
        for event in events:
            entry = self.FONT.render(event.text, True, (0, 0, 0))
            entry.fill(event.color)
            WIN.blit(entry, (500, row))
            entry = self.FONT.render(event.text, True, (0, 0, 0))
            WIN.blit(entry, (500, row))
            row += 15

