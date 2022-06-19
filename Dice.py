import pygame
import random
import time

pygame.font.init()

WIDTH, HEIGHT = 900, 500

FPS = 10

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND = (230,230,230)
BLACK = (0,0,0)
MAROON = (128, 0, 0)
WHITE = (255,255,255)

DICE = pygame.Rect(WIDTH/2 - 160, 100, 300, 300)
DICE_2 = pygame.Rect(WIDTH/2 - 155, 105, 290, 290)

LABEL = pygame.font.SysFont("Ubuntu", 50, True)

def draw_dice(val):
    if val == 1:
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 - 10, HEIGHT / 2), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 - 10, HEIGHT / 2), 30)
    elif val == 2:
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 - 100, 170), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 - 100, 170), 30)
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 + 80, HEIGHT - 170), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 + 80, HEIGHT - 170), 30)
    elif val == 3:
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 - 100, 170), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 - 100, 170), 30)
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 + 80, HEIGHT - 170), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 + 80, HEIGHT - 170), 30)
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 - 10, HEIGHT / 2), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 - 10, HEIGHT / 2), 30)
    elif val == 4:
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 - 100, 170), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 - 100, 170), 30)
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 + 80, HEIGHT - 170), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 + 80, HEIGHT - 170), 30)
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 + 80, 170), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 + 80, 170), 30)
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 - 100, HEIGHT - 170), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 - 100, HEIGHT - 170), 30)
    elif val == 5:
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 - 100, 170), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 - 100, 170), 30)
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 + 80, HEIGHT - 170), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 + 80, HEIGHT - 170), 30)
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 + 80, 170), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 + 80, 170), 30)
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 - 100, HEIGHT - 170), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 - 100, HEIGHT - 170), 30)
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 - 10, HEIGHT / 2), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 - 10, HEIGHT / 2), 30)
    elif val == 6:
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 - 10, HEIGHT / 2 - 50), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 - 10, HEIGHT / 2 - 50), 30)
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 - 100, HEIGHT / 2 - 50), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 - 100, HEIGHT / 2 - 50), 30)
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 + 80, HEIGHT / 2 - 50), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 + 80, HEIGHT / 2 - 50), 30)

        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 - 10, HEIGHT / 2 + 50), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 - 10, HEIGHT / 2 + 50), 30)
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 - 100, HEIGHT / 2 + 50), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 - 100, HEIGHT / 2 + 50), 30)
        pygame.draw.circle(WIN, BLACK, (WIDTH / 2 + 80, HEIGHT / 2 + 50), 35)
        pygame.draw.circle(WIN, WHITE, (WIDTH / 2 + 80, HEIGHT / 2 + 50), 30)


def draw_window(val):
    WIN.fill(BACKGROUND)
    pygame.draw.rect(WIN, BLACK, DICE)
    pygame.draw.rect(WIN, MAROON, DICE_2)
    txt = LABEL.render("Press Space for dice", 1, BLACK)
    WIN.blit(txt, (WIDTH//2 - txt.get_width()/2, 15))
    draw_dice(val)
    pygame.display.update()


def main():
    run = True
    dice_val = 0
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                run = False

        key_press = pygame.key.get_pressed()

        if key_press[pygame.K_SPACE]:
            dice_val = random.randint(1,6)

        draw_window(dice_val)


    pygame.quit()

if __name__ == "__main__":
    main()