import pygame
from avatars import NICOLE

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("HEHEHEHEHEHEHEHEHEHEHEHEHEHEHE")
BORDER = pygame.Rect(0, 0, WIDTH, HEIGHT)

BLACK = (0, 0, 0)

FPS = 60

avatar = None

AVATAR_WIDTH, AVATAR_HEIGHT = 40, 40

VELOCITY = 5

def draw_window(avatar_space):
    WIN.fill(BLACK)
    WIN.blit(avatar, (avatar_space.x, avatar_space.y))
    pygame.display.update()

def handle_avatar_movement(keys_pressed, avatar_space):
    if keys_pressed[pygame.K_LEFT] and avatar_space.x - VELOCITY > 0:  # left key
        avatar_space.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and avatar_space.x + VELOCITY < WIDTH - AVATAR_WIDTH:  # right key
        avatar_space.x += VELOCITY
    if keys_pressed[pygame.K_UP] and avatar_space.y - VELOCITY > 0:  # up key
        avatar_space.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and avatar_space.y + VELOCITY < HEIGHT - AVATAR_HEIGHT:  # down key
        avatar_space.y += VELOCITY


def main():
    global avatar
    avatar = pygame.transform.scale(NICOLE, (40, 40))
    avatar_space = pygame.Rect(100, 250, AVATAR_WIDTH, AVATAR_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        handle_avatar_movement(keys_pressed, avatar_space)
        draw_window(avatar_space)
    pygame.quit()


if __name__ == "__main__":
    main()
