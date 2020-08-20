import pygame

sprites = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.rect = self.image.get_rect()
        self.velocity = 10

    def __str__(self):
        return 'Player Sprite'

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.centery -= self.velocity

        if keys[pygame.K_s]:
            self.rect.centery += self.velocity

        if keys[pygame.K_a]:
            self.rect.centerx -= self.velocity

        if keys[pygame.K_d]:
            self.rect.centerx += self.velocity

