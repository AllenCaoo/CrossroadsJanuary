import pygame
from characters import NICOLE

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("HEHEHEHEHEHEHEHEHEHEHEHEHEHEHE")

WHITE = (255, 255, 255)

FPS = 60

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(NICOLE, )
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
