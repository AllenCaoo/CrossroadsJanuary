import random

import pygame

from main import WIDTH, HEIGHT, AVATAR_WIDTH, AVATAR_HEIGHT

from avatars import NICOLE, ALLEN

from random import *


class Enemy:
    def __init__(self, difficulty):
        self.space = pygame.Rect(WIDTH - AVATAR_WIDTH, HEIGHT / 2 - AVATAR_HEIGHT / 2,
                                 AVATAR_WIDTH, AVATAR_HEIGHT)
        self.avatar = pygame.transform.scale(ALLEN, (40, 40))
        self.velocity = difficulty
        self.xMove = randint(-10, 0)
        self.yMove = randint(-20, 20)
        self.crossedBorder = False
