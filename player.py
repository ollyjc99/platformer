import pygame

sprites = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255,50,255))
        self.rect = self.image.get_rect()
        self.velocity = 10

    def __str__(self):
        return 'Player Sprite'

    def draw(self):
        print('ye')

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.centery -= self.velocity

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.centery += self.velocity

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.centerx -= self.velocity

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.centerx += self.velocity
