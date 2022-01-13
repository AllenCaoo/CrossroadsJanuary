import pygame
from avatars import NICOLE
from Roles import *

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("HEHEHEHEHEHEHEHEHEHEHEHEHEHEHE")

BLACK = (0, 0, 0)

RED = (255, 0, 0)

GREEN = (0, 255, 0)

FPS = 60

avatar = None

enemies = []

AVATAR_WIDTH, AVATAR_HEIGHT = 40, 40

BORDER = pygame.Rect(WIDTH - AVATAR_WIDTH - 50, 0, 10, HEIGHT)

VELOCITY = 5

ENEMY_SPAWN = pygame.Rect(WIDTH - AVATAR_WIDTH, HEIGHT / 2 - AVATAR_HEIGHT / 2,
                          AVATAR_WIDTH, AVATAR_HEIGHT)

SPAWN_CD = 500

ATTACK_CD = 2000


def draw_window(av, enemies):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, (255, 255, 255), ENEMY_SPAWN)
    pygame.draw.rect(WIN, (255, 255, 255), BORDER)
    WIN.blit(av.avatar, (av.space.x, av.space.y))
    if av.can_attack():
        pygame.draw.circle(WIN, GREEN,
                           (av.space.x + AVATAR_WIDTH / 2, av.space.y + AVATAR_HEIGHT / 2),
                           100, width=2)
    else:
        pygame.draw.circle(WIN, RED,
                           (av.space.x + AVATAR_WIDTH / 2, av.space.y + AVATAR_HEIGHT / 2),
                           100, width=2)
    for e in enemies:
        WIN.blit(e.avatar, (e.space.x, e.space.y))
    pygame.display.update()


def handle_avatar_movement(keys_pressed, av):
    av.handle_movement(keys_pressed)


def handle_enemy_movement(enemies):
    for e in enemies:
        e.move()


def main():
    global avatar, enemies
    avatar = Avatar(enemies)
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
            enemies.append(Enemy(3))
            last = now
        keys_pressed = pygame.key.get_pressed()
        handle_avatar_movement(keys_pressed, avatar)
        handle_enemy_movement(enemies)
        draw_window(avatar, enemies)
    pygame.quit()


if __name__ == "__main__":
    main()
