import pygame

from main import WIDTH, HEIGHT, AVATAR_WIDTH, AVATAR_HEIGHT, BORDER, enemies, ATTACK_CD

from characters import NICOLE, ALLEN

from random import *


class Enemy:
    def __init__(self, difficulty):
        self.velocity = difficulty
        self.health = 2
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
    def __init__(self, enemies_lst):
        self.width = AVATAR_WIDTH
        self.height = AVATAR_HEIGHT
        self.avatar = pygame.transform.scale(NICOLE, (40, 40))
        self.space = pygame.Rect(100, 250, self.width, self.height)
        self.attack_cd = ATTACK_CD
        self.last_attacked = -self.attack_cd
        self.velocity = 5
        self.enemies = enemies_lst

    def handle_movement(self, keys_pressed):
        if keys_pressed[pygame.K_a] and self.space.x - self.velocity > 0:  # left key
            self.space.x -= self.velocity
        if keys_pressed[pygame.K_d] and self.space.x + self.velocity < BORDER.x - AVATAR_WIDTH:  # right key
            self.space.x += self.velocity
        if keys_pressed[pygame.K_w] and self.space.y - self.velocity > 0:  # up key
            self.space.y -= self.velocity
        if keys_pressed[pygame.K_s] and self.space.y + self.velocity < HEIGHT - AVATAR_HEIGHT:  # down key
            self.space.y += self.velocity
        if keys_pressed[pygame.K_SPACE]:
            self.attack()

    def attack(self):
        now = pygame.time.get_ticks()
        if now - self.last_attacked >= self.attack_cd:
            self.last_attacked = now
            dead = []
            for i in range(len(self.enemies)):
                if abs(self.enemies[i].space.x - self.space.x) < 100 and \
                        abs(self.enemies[i].space.y - self.space.y) < 100:
                    dead.append(i)
            for i in range(len(dead)):
                self.enemies.pop(dead[i] - i)

    def can_attack(self):
        now = pygame.time.get_ticks()
        if now - self.last_attacked >= self.attack_cd:
            return True
        return False
