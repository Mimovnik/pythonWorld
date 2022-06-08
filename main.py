import pygame

WHITE = (255,255,255)

WIDTH, HEIGHT = 900, 900

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python World")


def drawWindow():
    WIN.fill(WHITE)
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        drawWindow()


if __name__ == "__main__":
    main()