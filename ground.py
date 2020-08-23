import pygame

platforms = pygame.sprite.Group()


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((400, 40))
        self.rect = self.image.get_rect()
        self.rect.bottom = 600

    def __str__(self):
        return 'Platform'

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.image.scroll(1, 1)

        if keys[pygame.K_RIGHT]:
            self.image.scroll(dx=1)

