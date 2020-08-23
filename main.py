import pygame
from player import *
from ground import *


def main(*args, **kwargs):
    win = pygame.display.set_mode((800, 600), 0, 32)
    clock = pygame.time.Clock()
    player = Player()
    surf = pygame.Surface((400, 300))
    platforms.add(Platform())
    sprites.add(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        sprites.update()
        platforms.update()

        win.fill((220, 220, 100))

        platforms.draw(win)

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    pygame.init()
    main()
