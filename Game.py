import pygame
from BattleLog import BattleLog
from World import World


class Game:
    def __init__(self, window, fromFile=False, terrainWidth=20, terrainHeight=20):
        self.window = window
        if fromFile:
            self.world = World.load_from_file(window)
        else:
            self.world = World(
                               terrainWidth, terrainHeight, self.window)
        self.battleLog = BattleLog(
            self.world.terrain[-1].rect.x + self.world.terrain[-1].rect.width + 10)

    def draw_window(self):
        self.window.fill((255, 255, 255))
        self.world.draw()
        self.battleLog.draw(self.world.events, self.window)
        self.draw_hints()
        pygame.display.update()

    def draw_hints(self):
        belowTerrainY = self.world.terrain[-1].rect.y + self.world.terrain[-1].rect.height
        FONT = pygame.font.SysFont("Noto Sans", 12)
        entry = FONT.render(
            "Press 'space' to start the next turn", True, (0, 0, 0))
        self.window.blit(entry, (10, belowTerrainY + 10))
        entry = FONT.render(
            "or 's' to save a game or 'q' to quit.", True, (0, 0, 0))
        self.window.blit(entry, (10, belowTerrainY + 30))

    def make_turn(self):
        self.world.events.clear()
        self.world.make_actions()

    def game(self):
        self.draw_window()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        return False
                    elif event.key == pygame.K_SPACE:
                        self.make_turn()
                    elif event.key == pygame.K_s:
                        self.world.save_to_file()
            
            self.draw_window()
