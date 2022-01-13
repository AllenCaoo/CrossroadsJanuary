import sys

import pygame
from characters import NICOLE
from Roles import *

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("HEHEHEHEHEHEHEHEHEHEHEHEHEHEHE")

BLACK = (0, 0, 0)

RED = (255, 0, 0)

GREEN = (0, 255, 0)

YELLOW = (255, 200, 0)

FPS = 60

avatar = None

enemies = []

AVATAR_WIDTH, AVATAR_HEIGHT = 40, 40

BORDER = pygame.Rect(WIDTH - AVATAR_WIDTH - 50, 0, 10, HEIGHT)

VELOCITY = 5

ENEMY_SPAWN = pygame.Rect(WIDTH - AVATAR_WIDTH, HEIGHT / 2 - AVATAR_HEIGHT / 2,
                          AVATAR_WIDTH, AVATAR_HEIGHT)

SPAWN_CD = 1000

ATTACK_CD = 2000


def menu():
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 30)
    run = True
    menu_avatar_width = 70
    menu_avatar_height = 70
    while run:
        WIN.fill(BLACK)
        clock = pygame.time.Clock()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        nicole = pygame.transform.scale(NICOLE, (70, 70))
        nicole_space = pygame.Rect(WIDTH / 5, 2 * HEIGHT / 3,
                                   menu_avatar_width, menu_avatar_height)
        nicole_text = font.render('Nicole', False, (255, 255, 255))
        nicole_text_rect = nicole_text.get_rect(
            center=(nicole_space.centerx, nicole_space.centery - 60))

        park = pygame.transform.scale(PARK, (70, 70))
        park_space = pygame.Rect(2 * WIDTH / 5, 2 * HEIGHT / 3,
                                 menu_avatar_width, menu_avatar_height)
        park_text = font.render('Park', False, (255, 255, 255))
        park_text_rect = park_text.get_rect(
            center=(park_space.centerx, park_space.centery - 60))

        zoe = pygame.transform.scale(ZOE, (70, 70))
        zoe_space = pygame.Rect(3 * WIDTH / 5, 2 * HEIGHT / 3,
                                menu_avatar_width, menu_avatar_height)
        zoe_text = font.render('Zoe', False, (255, 255, 255))
        zoe_text_rect = zoe_text.get_rect(
            center=(zoe_space.centerx, zoe_space.centery - 60))

        elaine = pygame.transform.scale(ELAINE, (70, 70))
        elaine_space = pygame.Rect(4 * WIDTH / 5, 2 * HEIGHT / 3,
                                   menu_avatar_width, menu_avatar_height)
        elaine_text = font.render('Elaine', False, (255, 255, 255))
        elaine_text_rect = elaine_text.get_rect(
            center=(elaine_space.centerx, elaine_space.centery - 60))

        WIN.blit(nicole, (nicole_space.x, nicole_space.y))
        WIN.blit(park, (park_space.x, park_space.y))
        WIN.blit(zoe, (zoe_space.x, zoe_space.y))
        WIN.blit(elaine, (elaine_space.x, elaine_space.y))

        welcome_text = font.render('Welcome to Crossroads January!', False, (255, 255, 255))
        welcome_rect = welcome_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))

        WIN.blit(welcome_text, welcome_rect)
        WIN.blit(nicole_text, nicole_text_rect)
        WIN.blit(park_text, park_text_rect)
        WIN.blit(zoe_text, zoe_text_rect)
        WIN.blit(elaine_text, elaine_text_rect)

        if nicole_space.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GREEN, nicole_space, 1)
        if park_space.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GREEN, park_space, 1)
        if zoe_space.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GREEN, zoe_space, 1)
        if elaine_space.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GREEN, elaine_space, 1)

        pygame.display.update()


def draw_window(av, enemies):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, (255, 255, 255), ENEMY_SPAWN)
    pygame.draw.rect(WIN, (255, 255, 255), BORDER)
    WIN.blit(av.avatar, (av.space.x, av.space.y))
    if av.can_attack():
        pygame.draw.circle(WIN, GREEN,
                           (av.space.x + AVATAR_WIDTH / 2, av.space.y + AVATAR_HEIGHT / 2),
                           100, width=2)
    elif av.can_almost_attack():
        pygame.draw.circle(WIN, YELLOW,
                           (av.space.x + AVATAR_WIDTH / 2, av.space.y + AVATAR_HEIGHT / 2),
                           100, width=2)
    else:
        pygame.draw.circle(WIN, RED,
                           (av.space.x + AVATAR_WIDTH / 2, av.space.y + AVATAR_HEIGHT / 2),
                           100, width=2)
    for e in enemies:
        WIN.blit(e.avatar, (e.space.x, e.space.y))
    pygame.display.update()


def handle_avatar_action(keys_pressed, av):
    av.handle_action(keys_pressed)


def handle_enemy_action(enemies, av):
    for e in enemies:
        e.action(av)


def main():
    global avatar, enemies
    menu()
    avatar = Avatar(0, enemies)
    clock = pygame.time.Clock()
    run = True
    difficulty = 1
    last = pygame.time.get_ticks()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        now = pygame.time.get_ticks()
        if now - last >= SPAWN_CD:
            enemies.append(Enemy(0, 3))
            last = now
        keys_pressed = pygame.key.get_pressed()
        handle_avatar_action(keys_pressed, avatar)
        handle_enemy_action(enemies, avatar)
        draw_window(avatar, enemies)
    pygame.quit()


if __name__ == "__main__":
    main()
