import pygame
from player import *


def main(*args, **kwargs):
    win = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    player = Player()
    sprites.add(player)

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        sprites.update()

        win.fill((220, 220, 100))
        sprites.draw(win)

        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    main()
