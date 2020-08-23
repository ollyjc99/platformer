import pygame
import math


class Ball(object):
    def __init__(self, x, y, radius, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour

    def draw(self, win):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius-1)

    @staticmethod
    def ballpath(self, startx, starty, power, ang, time):
        pass


def redraw_win(win, golf):
    win.fill((64, 64, 64))
    golf.draw(win)
    pygame.display.update()


def main():
    win = pygame.display.set_mode((800, 600))
    golf = Ball(300, 300, 10, (255, 255, 255))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        redraw_win(win, golf)


if __name__ == '__main__':
    main()