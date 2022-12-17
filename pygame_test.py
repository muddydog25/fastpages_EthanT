import pygame
import random
from pygame.locals import (
    QUIT,
    KEYDOWN,
    K_ESCAPE,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((132, 252, 3))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH, SCREEN_HEIGHT))

    def move(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)    

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((132, 252, 3))
        self.rect = self.surf.get_rect(center = (random.randint(5, SCREEN_WIDTH -5), random.randint(5, SCREEN_HEIGHT - 5)))


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Player()

running = True

while running:

    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.move(pressed_keys)

    screen.fill((173, 216, 230))

    screen.blit(player.surf, player.rect)

    pygame.display.flip()

    clock.tick(60)