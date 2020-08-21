import pygame

platforms = pygame.sprite.Group()


class Platform(pygame.sprite.Sprite):
    def __init__(self, w):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, 40))
        self.rect = self.image.get_rect()

    def __str__(self):
        return 'Platform'

    def update(self):
        pass

