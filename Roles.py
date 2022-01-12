import pygame

from main import WIDTH, HEIGHT, AVATAR_WIDTH, AVATAR_HEIGHT, BORDER

from avatars import NICOLE, ALLEN

from random import *


class Enemy:
    def __init__(self, difficulty):
        self.velocity = difficulty
        self.space = pygame.Rect(WIDTH - AVATAR_WIDTH, HEIGHT / 2 - AVATAR_HEIGHT / 2,
                                 AVATAR_WIDTH, AVATAR_HEIGHT)
        self.avatar = pygame.transform.scale(ALLEN, (40, 40))
        self.velocity = difficulty
        self.xMove = randint(-3, -1)
        self.yMove = randint(-3, 3)
        self.crossed_border = False

    def move(self):
        if self.space.x + self.xMove < BORDER.x - AVATAR_WIDTH:
            self.crossed_border = True
        if self.space.x + self.xMove < 0:
            self.xMove = -self.xMove
        if self.space.y + self.yMove < 0:
            self.yMove = -self.yMove
        if self.space.x + self.xMove > BORDER.x - AVATAR_WIDTH - 1 and self.crossed_border:
            self.xMove = -self.xMove
        if self.space.y + self.yMove > HEIGHT - AVATAR_HEIGHT - 1 and self.crossed_border:
            self.yMove = -self.yMove
        self.space.x += self.xMove
        self.space.y += self.yMove


class Avatar:
    def __init__(self):
        self.width = AVATAR_WIDTH
        self.height = AVATAR_HEIGHT
        self.velocity = 5
        self.avatar = pygame.transform.scale(NICOLE, (40, 40))
        self.space = pygame.Rect(100, 250, self.width, self.height)

    def handle_movement(self, keys_pressed):
        if keys_pressed[pygame.K_a] and self.space.x - self.velocity > 0:  # left key
            self.space.x -= self.velocity
        if keys_pressed[pygame.K_d] and self.space.x + self.velocity < BORDER.x - AVATAR_WIDTH:  # right key
            self.space.x += self.velocity
        if keys_pressed[pygame.K_w] and self.space.y - self.velocity > 0:  # up key
            self.space.y -= self.velocity
        if keys_pressed[pygame.K_s] and self.space.y + self.velocity < HEIGHT - AVATAR_HEIGHT:  # down key
            self.space.y += self.velocity
