import pygame

from characters import *
from main import WIDTH, HEIGHT, AVATAR_WIDTH, AVATAR_HEIGHT, BORDER, enemies, ATTACK_CD

from characters import NICOLE

from random import *


class Enemy:
    def __init__(self, av_id, difficulty):
        self.velocity = difficulty
        # self.health = 2
        self.space = pygame.Rect(WIDTH - AVATAR_WIDTH, HEIGHT / 2 - AVATAR_HEIGHT / 2,
                                 AVATAR_WIDTH, AVATAR_HEIGHT)
        self.avatar = pygame.transform.scale(get_rand_img_not(av_id), (40, 40))
        self.velocity = difficulty
        self.xMove = randint(-3, -1)
        self.yMove = randint(-3, 3)
        self.crossed_border = False
        self.attack_cd = ATTACK_CD
        self.last_attacked = -self.attack_cd

    def action(self, av):
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
        self.attack(av)
        self.space.x += self.xMove
        self.space.y += self.yMove

    def attack(self, av):
        now = pygame.time.get_ticks()
        if self.can_attack() and self.in_range(av):
            av.injured()
            self.last_attacked = now

    def can_attack(self):
        now = pygame.time.get_ticks()
        if now - self.last_attacked >= self.attack_cd:
            return True
        return False

    def in_range(self, av):
        return abs(av.space.centerx - self.space.centerx) < 30 \
               and abs(av.space.centery - self.space.centery) < 30


class Avatar:
    def __init__(self, id, enemies_lst):
        self.id = id
        self.health = 2
        self.width = AVATAR_WIDTH
        self.height = AVATAR_HEIGHT
        self.avatar = pygame.transform.scale(characters[id], (40, 40))
        self.space = pygame.Rect(100, 250, self.width, self.height)
        self.attack_cd = ATTACK_CD
        self.last_attacked = -self.attack_cd
        self.velocity = 5
        self.enemies = enemies_lst

    def handle_action(self, keys_pressed):
        if keys_pressed[pygame.K_a] and self.space.x - self.velocity > 0:  # go left
            self.space.x -= self.velocity
        if keys_pressed[pygame.K_d] and self.space.x + self.velocity < BORDER.x - AVATAR_WIDTH:  # go right
            self.space.x += self.velocity
        if keys_pressed[pygame.K_w] and self.space.y - self.velocity > 0:  # go up
            self.space.y -= self.velocity
        if keys_pressed[pygame.K_s] and self.space.y + self.velocity < HEIGHT - AVATAR_HEIGHT:  # go down
            self.space.y += self.velocity
        if keys_pressed[pygame.K_SPACE]:
            self.attack()

    def attack(self):
        now = pygame.time.get_ticks()
        if now - self.last_attacked >= self.attack_cd:
            self.last_attacked = now
            dead = []
            for i in range(len(self.enemies)):
                if self.in_range(self.enemies[i]):
                    dead.append(i)
            for i in range(len(dead)):
                self.enemies.pop(dead[i] - i)

    def in_range(self, enemy):
        return abs(enemy.space.x - self.space.x) < 100 and abs(enemy.space.y - self.space.y) < 100

    def can_attack(self):
        now = pygame.time.get_ticks()
        if now - self.last_attacked >= self.attack_cd:
            return True
        return False

    def can_almost_attack(self):
        now = pygame.time.get_ticks()
        if now - self.last_attacked >= self.attack_cd / 2:
            return True
        return False

    def injured(self):
        self.health -= 1
        if self.health == 0:
            pygame.quit()  # Need better way to end the game
        self.avatar = pygame.transform.scale(characters_injured[self.id], (40, 40))
