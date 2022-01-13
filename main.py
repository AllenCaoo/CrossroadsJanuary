from Roles import *

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("HEHEHEHEHEHEHEHEHEHEHEHEHEHEHE")

BLACK = (0, 0, 0)

RED = (255, 0, 0)

GREEN = (0, 255, 0)

YELLOW = (255, 200, 0)

WHITE = (255, 255, 255)

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
    clock = pygame.time.Clock()
    while run:
        WIN.fill(BLACK)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        nicole = pygame.transform.scale(NICOLE, (70, 70))
        nicole_space = pygame.Rect(WIDTH / 5, 2 * HEIGHT / 3,
                                   menu_avatar_width, menu_avatar_height)
        nicole_text = font.render('Nicole', False, WHITE)
        nicole_text_rect = nicole_text.get_rect(
            center=(nicole_space.centerx, nicole_space.centery - 60))

        park = pygame.transform.scale(PARK, (70, 70))
        park_space = pygame.Rect(2 * WIDTH / 5, 2 * HEIGHT / 3,
                                 menu_avatar_width, menu_avatar_height)
        park_text = font.render('Park', False, WHITE)
        park_text_rect = park_text.get_rect(
            center=(park_space.centerx, park_space.centery - 60))

        zoe = pygame.transform.scale(ZOE, (70, 70))
        zoe_space = pygame.Rect(3 * WIDTH / 5, 2 * HEIGHT / 3,
                                menu_avatar_width, menu_avatar_height)
        zoe_text = font.render('Zoe', False, WHITE)
        zoe_text_rect = zoe_text.get_rect(
            center=(zoe_space.centerx, zoe_space.centery - 60))

        elaine = pygame.transform.scale(ELAINE, (70, 70))
        elaine_space = pygame.Rect(4 * WIDTH / 5, 2 * HEIGHT / 3,
                                   menu_avatar_width, menu_avatar_height)
        elaine_text = font.render('Elaine', False, WHITE)
        elaine_text_rect = elaine_text.get_rect(
            center=(elaine_space.centerx, elaine_space.centery - 60))

        WIN.blit(nicole, (nicole_space.x, nicole_space.y))
        WIN.blit(park, (park_space.x, park_space.y))
        WIN.blit(zoe, (zoe_space.x, zoe_space.y))
        WIN.blit(elaine, (elaine_space.x, elaine_space.y))

        welcome_text = font.render('Welcome to Crossroads January!', False, WHITE)
        welcome_rect = welcome_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))

        WIN.blit(welcome_text, welcome_rect)
        WIN.blit(nicole_text, nicole_text_rect)
        WIN.blit(park_text, park_text_rect)
        WIN.blit(zoe_text, zoe_text_rect)
        WIN.blit(elaine_text, elaine_text_rect)

        if nicole_space.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GREEN, nicole_space, 1)
            if pygame.mouse.get_pressed()[0]:
                return 0
        if park_space.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GREEN, park_space, 1)
            if pygame.mouse.get_pressed()[0]:
                return 1
        if zoe_space.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GREEN, zoe_space, 1)
            if pygame.mouse.get_pressed()[0]:
                return 2
        if elaine_space.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GREEN, elaine_space, 1)
            if pygame.mouse.get_pressed()[0]:
                return 3

        pygame.display.update()


def end(score):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        score_text = font.render('you died! your score: ' + str(score),
                                 False, WHITE)
        score_text_rect = score_text.get_rect(center=(WIDTH / 2, HEIGHT / 3))

        play_text = font.render('play again',
                                False, WHITE)
        play_text_rect = play_text.get_rect(center=(WIDTH / 3, 2 * HEIGHT / 3))

        quit_text = font.render('quit',
                                False, WHITE)
        quit_text_rect = quit_text.get_rect(center=(2 * WIDTH / 3, 2 * HEIGHT / 3))

        if play_text_rect.collidepoint(pygame.mouse.get_pos()):
            play_text = font.render('play again',
                                    False, GREEN)
            if pygame.mouse.get_pressed()[0]:
                main()
        if quit_text_rect.collidepoint(pygame.mouse.get_pos()):
            quit_text = font.render('quit',
                                    False, RED)
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
        WIN.blit(score_text, score_text_rect)
        WIN.blit(play_text, play_text_rect)
        WIN.blit(quit_text, quit_text_rect)
        pygame.display.update()


def draw_window(av, enemies, score):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, ENEMY_SPAWN)
    pygame.draw.rect(WIN, WHITE, BORDER)

    font = pygame.font.SysFont('Helvetica', 30)

    score_text = font.render('Score: ' + str(score), False, WHITE)
    score_rect = score_text.get_rect(topleft=(5, 0))
    WIN.blit(score_text, score_rect)

    hp_text = font.render('HP: ' + str(av.health), False, WHITE)
    hp_rect = score_text.get_rect(topleft=(BORDER.x + BORDER.width + 5, 0))
    WIN.blit(hp_text, hp_rect)

    WIN.blit(av.avatar, (av.space.x, av.space.y))
    av.draw_range(WIN)

    for e in enemies:
        WIN.blit(e.avatar, (e.space.x, e.space.y))
    pygame.display.update()


def handle_avatar_action(keys_pressed, av):  # Returns number of points scored in action
    return av.handle_action(keys_pressed)


def handle_enemy_action(enemies, av):
    for e in enemies:
        e.action(av)


def main():
    global avatar, enemies
    enemies.clear()
    avatar_id = menu()
    if avatar_id == 0:
        avatar = Speedrunner(avatar_id, enemies)
    if avatar_id == 1:
        avatar = Sniper(avatar_id, enemies)  # Perceptive
    if avatar_id == 2:
        avatar = Tank(avatar_id, enemies)
    if avatar_id == 3:
        avatar = Gunner(avatar_id, enemies)
    clock = pygame.time.Clock()
    run = True
    difficulty = 1
    last = pygame.time.get_ticks()
    score = 0
    while run:
        clock.tick(FPS)
        if avatar.is_dead():
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        now = pygame.time.get_ticks()
        if now - last >= SPAWN_CD:
            enemies.append(Enemy(avatar_id, 3))
            last = now
        keys_pressed = pygame.key.get_pressed()
        score += handle_avatar_action(keys_pressed, avatar)
        handle_enemy_action(enemies, avatar)
        draw_window(avatar, enemies, score)
    end(score)


if __name__ == "__main__":
    main()
