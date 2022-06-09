import pygame
from BattleLog import BattleLog
from World import World

pygame.init()

WHITE = (255,255,255)

WIN_WIDTH, WIN_HEIGHT = 900, 900
TERRAIN_WIDTH, TERRAIN_HEIGHT = 20, 20
WORLD_WIDTH, WORLD_HEIGHT = 500, 500

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Python World")

world = World(WORLD_WIDTH, WORLD_HEIGHT, TERRAIN_WIDTH, TERRAIN_HEIGHT, WIN)

battleLog = BattleLog()

def draw_window():
    WIN.fill(WHITE)
    world.draw()
    battleLog.draw(world.events, WIN)
    pygame.display.update()

def make_turn():
    world.events.clear()
    world.make_actions()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    make_turn()

        draw_window()


if __name__ == "__main__":
    main()