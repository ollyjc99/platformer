import pygame
from random import randint

blocks = pygame.sprite.Group()
chunks = pygame.sprite.Group()


class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((50, 200, 75))
        self.rect = self.image.get_rect()
        self.rect.bottom = 600

    def __str__(self):
        return 'Platform'


class Chunk(object):
    def __init__(self):
        self.surface = pygame.Surface((400, 250))
        self.noise = [[randint(1, 3)] for i in range(8)]
