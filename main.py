import pygame
import World

WHITE = (255,255,255)

WIN_WIDTH, WIN_HEIGHT = 900, 900
TERRAIN_WIDTH, TERRAIN_HEIGHT = 20, 20
WORLD_WIDTH, WORLD_HEIGHT = 500, 500

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Python World")

world = World.World(WORLD_WIDTH, WORLD_HEIGHT, TERRAIN_WIDTH, TERRAIN_HEIGHT, WIN)

def drawWindow():
    WIN.fill(WHITE)
    world.draw()
    pygame.display.update()


def main():
    pygame.init()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    world.make_actions()

        drawWindow()


if __name__ == "__main__":
    main()