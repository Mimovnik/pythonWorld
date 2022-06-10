import os
import pygame
from Game import Game


def main():
    pygame.init()
    WIN_WIDTH, WIN_HEIGHT = 900, 900
    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Python World")
    WIN.fill((255, 255, 255))

    FONT = pygame.font.SysFont("Noto Sans", 32)

    entry = FONT.render(
        "Press 's' to load from save or 'n' to create a new world", True, (0, 0, 0))
    WIN.blit(entry, (int(WIN_WIDTH / 2 - entry.get_width() / 2),
             int(WIN_HEIGHT / 2 - entry.get_height() / 2)))

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                elif event.key == pygame.K_n:
                    run = Game(WIN).game()
                elif event.key == pygame.K_s:
                    if savefile_exists():
                        run = Game(WIN, True).game()
                    else:
                        entry = FONT.render(
                            "There are no saves yet.", True, (0, 0, 0))
                        WIN.blit(entry, (int(WIN_WIDTH / 2 - entry.get_width() / 2),
                                 int(WIN_HEIGHT / 2 - entry.get_height() / 2) + 100))
                        pygame.display.update()

    pygame.quit()


def savefile_exists():
    os.path.isfile("save.txt")


if __name__ == "__main__":
    main()
