import pygame
from random import randint
from player import *
from ground import *


def main(*args, **kwargs):
    win = pygame.display.set_mode((800, 600), 0, 32)
    clock = pygame.time.Clock()
    player = Player()
    chunk = Chunk()
    blocks.add(Block())
    sprites.add(player)

    grid = [[randint(2, 3)] for i in range(8)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        sprites.update()
        blocks.update()

        win.fill((220, 220, 100))

        blocks.draw(win)
        sprites.draw(win)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    pygame.init()
    main()
