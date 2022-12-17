import pygame
from pygame.locals import (
    QUIT,
    KEYDOWN,
    K_ESCAPE
)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((132, 252, 3))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH, SCREEN_HEIGHT))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == QUIT:
            running = False

    pygame.display.flip()

    clock.tick(60)