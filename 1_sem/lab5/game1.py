import pygame.draw
from random import randint

pygame.init()

FPS = 60
screen_size = (screen_x, screen_y) = (1200, 900)
screen = pygame.display.set_mode(screen_size)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

balls = []  # список под характеристики шара


def generate_ball():
    '''генерирует новый шарик '''
    r = randint(10, 100)
    x = randint(100, 1100)
    y = randint(100, 800)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    color_number = randint(0, 5)
    balls.append([x, y, r, vx, vy, color_number])


pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0

for _ in range(15):  # создаем на экране 15 шаров
    generate_ball()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            event.x, event.y = event.pos
            for ball in balls:
                if (ball[0] - event.x) ** 2 + (ball[1] - event.y) ** 2 < ball[2] ** 2:
                    score += 1
                    balls.remove(ball)
                    generate_ball()

    for ball in balls:
        ball[0] += ball[3]  # адаем скорость шаров
        ball[1] += ball[4]
        pygame.draw.circle(screen, COLORS[ball[5]], (ball[0], ball[1]), ball[2])
        if min(ball[0], abs(ball[0] - screen_x)) <= ball[2]:  # отталкивание от границ экрана
            ball[3] = -ball[3]
            ball[0] += 2 * ball[3]
        if min(ball[1], abs(ball[1] - screen_y)) <= ball[2]:
            ball[4] = -ball[4]
            ball[1] += 2 * ball[4]
    pygame.display.update()
    screen.fill(BLACK)
print('УРА, ВАШ СЧЕТ', score)
pygame.quit()
