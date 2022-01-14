import sys

from Roles import *

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("If you're ready this, happy birthday!")

BLACK = (0, 0, 0)

RED = (255, 0, 0)

GREEN = (0, 255, 0)

BLUE = (0, 0, 255)

DARK_GREEN = (0, 120, 0)

YELLOW = (255, 200, 0)

WHITE = (255, 255, 255)

TURQUOISE = (0, 120, 120)

PINK = (255, 192, 203)

WEIRD_COLOR = (120, 93, 23)

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
    run = True
    menu_avatar_width = 70
    menu_avatar_height = 70
    clock = pygame.time.Clock()
    while run:
        clicked = False
        clock.tick(FPS)
        WIN.fill(BLACK)
        font = pygame.font.SysFont('Comic Sans MS', 40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True

        welcome_text = font.render('©Crossroads January Resistance', False, (0, 255, 255))
        welcome_rect = welcome_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))
        font = pygame.font.SysFont('Comic Sans MS', 20)
        choice_text = font.render('Choose yoooooooooooooo fighter!!!', False, WHITE)
        choice_rect = choice_text.get_rect(center=(WIDTH / 2, welcome_rect.centery + 100))
        WIN.blit(welcome_text, welcome_rect)
        WIN.blit(choice_text, choice_rect)
        tutorial_text = font.render('CLICK HERE FOR RULES', False, WHITE)
        tutorial_rect = tutorial_text.get_rect(topright=(WIDTH - 50, 0))
        if tutorial_rect.collidepoint(pygame.mouse.get_pos()):
            tutorial_text = font.render('CLICK HERE FOR RULES', False, BLUE)
            if clicked:
                tutorial()
        WIN.blit(tutorial_text, tutorial_rect)

        font = pygame.font.SysFont('Comic Sans MS', 40)

        nicole = pygame.transform.scale(NICOLE, (70, 70))
        nicole_space = pygame.Rect(WIDTH / 5 - AVATAR_WIDTH / 2, 2 * HEIGHT / 3,
                                   menu_avatar_width, menu_avatar_height)
        nicole_text = font.render('Nicole', False, WHITE)
        nicole_text_rect = nicole_text.get_rect(
            center=(nicole_space.centerx, nicole_space.centery - 60))

        park = pygame.transform.scale(PARK, (70, 70))
        park_space = pygame.Rect(2 * WIDTH / 5 - AVATAR_WIDTH / 2, 2 * HEIGHT / 3,
                                 menu_avatar_width, menu_avatar_height)
        park_text = font.render('Park', False, WHITE)
        park_text_rect = park_text.get_rect(
            center=(park_space.centerx, park_space.centery - 60))

        zoe = pygame.transform.scale(ZOE, (70, 70))
        zoe_space = pygame.Rect(3 * WIDTH / 5 - AVATAR_WIDTH / 2, 2 * HEIGHT / 3,
                                menu_avatar_width, menu_avatar_height)
        zoe_text = font.render('Zoë', False, WHITE)
        zoe_text_rect = zoe_text.get_rect(
            center=(zoe_space.centerx, zoe_space.centery - 60))

        elaine = pygame.transform.scale(ELAINE, (70, 70))
        elaine_space = pygame.Rect(4 * WIDTH / 5 - AVATAR_WIDTH / 2, 2 * HEIGHT / 3,
                                   menu_avatar_width, menu_avatar_height)
        elaine_text = font.render('Elaine', False, WHITE)
        elaine_text_rect = elaine_text.get_rect(
            center=(elaine_space.centerx, elaine_space.centery - 60))

        WIN.blit(nicole, (nicole_space.x, nicole_space.y))
        WIN.blit(park, (park_space.x, park_space.y))
        WIN.blit(zoe, (zoe_space.x, zoe_space.y))
        WIN.blit(elaine, (elaine_space.x, elaine_space.y))

        descriptionx = 20
        descriptiony = nicole_space.centery + 50

        if nicole_space.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, WEIRD_COLOR, nicole_space, 1)
            nicole_text = font.render('Nicole', False, WEIRD_COLOR)
            display_description_nicole(descriptionx, descriptiony)
            if clicked:
                return 0
        if park_space.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, PINK, park_space, 1)
            park_text = font.render('Park', False, PINK)
            display_description_park(descriptionx, descriptiony)
            if clicked:
                return 1
        if zoe_space.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, TURQUOISE, zoe_space, 1)
            zoe_text = font.render('Zoë', False, TURQUOISE)
            display_description_zoe(descriptionx, descriptiony)
            if clicked:
                return 2
        if elaine_space.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, DARK_GREEN, elaine_space, 1)
            elaine_text = font.render('Elaine', False, DARK_GREEN)
            display_description_elaine(descriptionx, descriptiony)
            if clicked:
                return 3

        WIN.blit(nicole_text, nicole_text_rect)
        WIN.blit(park_text, park_text_rect)
        WIN.blit(zoe_text, zoe_text_rect)
        WIN.blit(elaine_text, elaine_text_rect)

        pygame.display.update()


def display_description_nicole(x, y):
    font = pygame.font.SysFont('Comic Sans MS', 16)
    color = WEIRD_COLOR
    text_1 = font.render("Nimble Nicole: she grew up balling with a bunch of baller bros (and that's the first "
                         "time I've used alliteration).", False, color)
    text_1_rect = text_1.get_rect(topleft=(x, y))
    text_2 = font.render("That's why she's so fast, fervent, and flexible (unlike her gym schedule). "
                         "She moves 2x faster and is 2x less likely", False, color)
    text_2_rect = text_1.get_rect(topleft=(text_1_rect.x, text_1_rect.y + 20))
    text_3 = font.render("to get hit by a Crossroader.", False, color)
    text_3_rect = text_1.get_rect(topleft=(text_1_rect.x, text_2_rect.y + 20))
    WIN.blit(text_1, text_1_rect)
    WIN.blit(text_2, text_2_rect)
    WIN.blit(text_3, text_3_rect)


def display_description_park(x, y):
    font = pygame.font.SysFont('Comic Sans MS', 16)
    color = PINK
    text_1 = font.render("Perceptive Park: even though he can't read this without glasses, Park is still somehow "
                         "better at reading you than "
                         "", False, color)
    text_1_rect = text_1.get_rect(topleft=(x, y))
    text_2 = font.render("anyone else can. He effortless senses your mood and sImpathizes with your circumstances. "
                         "That is why he laughs", False, color)
    text_2_rect = text_1.get_rect(topleft=(text_1_rect.x, text_1_rect.y + 20))
    text_3 = font.render("with you when you are happy and cries with you when you are sad. "
                         "His Ring of Hofung is wider.", False, color)
    text_3_rect = text_1.get_rect(topleft=(text_1_rect.x, text_2_rect.y + 20))
    WIN.blit(text_1, text_1_rect)
    WIN.blit(text_2, text_2_rect)
    WIN.blit(text_3, text_3_rect)


def display_description_zoe(x, y):
    font = pygame.font.SysFont('Comic Sans MS', 16)
    color = TURQUOISE
    text_1 = font.render("Zealous Zoë: there's like no other adjective that starts with 'z', but luckily 'zealous' "
                         "perfectly fits her. Zoë is ", False, color)
    text_1_rect = text_1.get_rect(topleft=(x, y))
    text_2 = font.render("zealous for two things: God and academics (in that order hopefully). Motivated by the power "
                         "of God and his grand ", False, color)
    text_2_rect = text_1.get_rect(topleft=(text_1_rect.x, text_1_rect.y + 20))
    text_3 = font.render("plans for her career, Zoë will toughen out all injuries. "
                         "She gains +2 health.", False, color)
    text_3_rect = text_1.get_rect(topleft=(text_1_rect.x, text_2_rect.y + 20))
    WIN.blit(text_1, text_1_rect)
    WIN.blit(text_2, text_2_rect)
    WIN.blit(text_3, text_3_rect)


def display_description_elaine(x, y):
    font = pygame.font.SysFont('Comic Sans MS', 16)
    color = DARK_GREEN
    text_1 = font.render("Enduring Elaine: she is the most sincere person you will ever meet. "
                         "In JFung's words, \"she ain't sus.\" That's why", False, color)
    text_1_rect = text_1.get_rect(topleft=(x, y))
    text_2 = font.render("Michael Zheng's dying wish was to give Elaine his Ring as " 
                         "a final repayment of kindness. Too bad he actually did die", False, color)
    text_2_rect = text_1.get_rect(topleft=(text_1_rect.x, text_1_rect.y + 20))
    text_3 = font.render("fighting the ragers. After combining her two Rings, "
                         "Elaine's new upgraded Ring now has half the attack cooldown.", False, color)
    text_3_rect = text_1.get_rect(topleft=(text_1_rect.x, text_2_rect.y + 20))
    WIN.blit(text_1, text_1_rect)
    WIN.blit(text_2, text_2_rect)
    WIN.blit(text_3, text_3_rect)


def tutorial():
    run = True
    clock = pygame.time.Clock()
    while run:
        font = pygame.font.SysFont('Comic Sans MS', 20)
        clock.tick(FPS)
        WIN.fill(BLACK)
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
        text_1 = font.render('The rules are simple.', False, RED)
        text_1_rect = text_1.get_rect(center=(WIDTH / 2, 50))
        text_2 = font.render("Crossroaders have gone sicko mode. Your job is to eliminate them so you don't get "
                             "infected.",
                             False, WHITE)
        text_2_rect = text_2.get_rect(topleft=(20, text_1_rect.centery + 20))
        text_3 = font.render('Once you have chosen a fighter, you will be teleported to the battlefield. ',
                             False, WHITE)
        text_3_rect = text_3.get_rect(topleft=(20, text_2_rect.centery + 20))
        text_4 = font.render("You have 2 health (4 for Zoë). If you get hit by a Crossroader," +
                             " you will lose 1 health.",
                             False, WHITE)
        text_4_rect = text_4.get_rect(topleft=(20, text_3_rect.centery + 20))
        text_5 = font.render('Better dodge then. On the battlefield, you can move: ',
                             False, WHITE)
        text_5_rect = text_5.get_rect(topleft=(20, text_4_rect.centery + 20))
        text_6 = font.render('UP (W or up arrow), DOWN (S or down arrow)',
                             False, GREEN)
        text_6_rect = text_6.get_rect(center=(WIDTH / 2, text_5_rect.centery + 30))
        text_7 = font.render('LEFT (A or left arrow), RIGHT (D or right arrow)',
                             False, GREEN)
        text_7_rect = text_7.get_rect(center=(WIDTH / 2, text_6_rect.centery + 20))
        text_8 = font.render('To defeat Crossroaders, you must use the Ring of Hofung.',
                             False, WHITE)
        text_8_rect = text_8.get_rect(topleft=(20, text_7_rect.centery + 20))
        text_9 = font.render('When Crossroaders step within the ring, you can eliminate them by: ',
                             False, WHITE)
        text_9_rect = text_9.get_rect(topleft=(20, text_8_rect.centery + 20))
        text_10 = font.render('pressing SPACE',
                              False, GREEN)
        text_10_rect = text_10.get_rect(center=(WIDTH / 2, text_9_rect.centery + 30))
        text_11 = font.render('Beware that this ring has a three second cooldown (half for Elaine).',
                              False, WHITE)
        text_11_rect = text_11.get_rect(topleft=(20, text_10_rect.centery + 20))
        text_12 = font.render("And if you haven't realized by now, each fighter has unique attributes.",
                              False, WHITE)
        text_12_rect = text_12.get_rect(topleft=(20, text_11_rect.centery + 20))
        text_13 = font.render("Good luck, and I hope you don't become a rager.",
                              False, WHITE)
        text_13_rect = text_13.get_rect(topleft=(20, text_12_rect.centery + 20))
        text_14 = font.render("+1 pts/second",
                              False, GREEN)
        text_14_rect = text_14.get_rect(center=(WIDTH / 3, text_13_rect.centery + 35))
        text_15 = font.render("+3 pts/XRoader",
                              False, GREEN)
        text_15_rect = text_14.get_rect(center=(2 * WIDTH / 3, text_13_rect.centery + 35))
        back = font.render('RETURN TO MENU', False, WHITE)
        back_rect = text_1.get_rect(center=(WIDTH - 130, 15))
        if back_rect.collidepoint(pygame.mouse.get_pos()):
            back = font.render('RETURN TO MENU', False, BLUE)
            if clicked:
                break
        WIN.blit(text_1, text_1_rect)
        WIN.blit(text_2, text_2_rect)
        WIN.blit(text_3, text_3_rect)
        WIN.blit(text_4, text_4_rect)
        WIN.blit(text_5, text_5_rect)
        WIN.blit(text_6, text_6_rect)
        WIN.blit(text_7, text_7_rect)
        WIN.blit(text_8, text_8_rect)
        WIN.blit(text_9, text_9_rect)
        WIN.blit(text_10, text_10_rect)
        WIN.blit(text_11, text_11_rect)
        WIN.blit(text_12, text_12_rect)
        WIN.blit(text_13, text_13_rect)
        WIN.blit(text_14, text_14_rect)
        WIN.blit(text_15, text_15_rect)
        WIN.blit(back, back_rect)
        pygame.display.update()


def end(score):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        score_text = font.render('you dead! your score: ' + str(score),
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
                sys.exit(0)
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
    last = pygame.time.get_ticks()
    score = 0
    while run:
        clock.tick(FPS)
        if avatar.is_dead():
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        now = pygame.time.get_ticks()
        if now - last >= SPAWN_CD:
            enemies.append(Enemy(avatar_id, 3))
            last = now
            score += 1
        keys_pressed = pygame.key.get_pressed()
        score += handle_avatar_action(keys_pressed, avatar)
        handle_enemy_action(enemies, avatar)
        draw_window(avatar, enemies, score)
    end(score)


if __name__ == "__main__":
    main()
