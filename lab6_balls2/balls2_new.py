import pygame.draw
from random import randint
import pygame.time

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
WHITE = (255, 220, 220)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


# список под характеристики шара

class Ball:

    def __init__(self):
        self.r = randint(20, 100)
        self.x = randint(100, 1100)
        self.y = randint(100, 800)
        self.vx = randint(-5, 5)
        self.vy = randint(-5, 5)
        self.color_number = randint(1, 5)

    def make_ball(self):
        pygame.draw.circle(screen, COLORS[self.color_number], (self.x, self.y), self.r)

    def move_ball(self):
        self.x += self.vx  # задаем скорость шаров
        self.y += self.vy
        if min(self.x, abs(self.x - screen_x)) <= self.r:  # отталкивание от границ экрана
            self.vx = -self.vx
            self.x += 2 * self.vx
        if min(self.y, abs(self.y - screen_y)) <= self.r:
            self.vy = -self.vy
            self.y += 2 * self.vy

class Bomb:

    def __init__(self):
        self.r = 10
        self.x = randint(100, 1100)
        self.y = randint(100, 800)
        self.vx = randint(-2, 2)
        self.vy = randint(-2, 2)
        self.left = FPS * 4
        self.color_number = 0
        self.bills = 3

    def make_bomb(self):
            pygame.draw.circle(screen, COLORS[self.color_number], (self.x, self.y), self.r)
            pygame.draw.circle(screen, WHITE, (self.x, self.y), self.r*0.75)
            pygame.draw.circle(screen, COLORS[self.color_number], (self.x, self.y), self.r*0.5)
            pygame.draw.circle(screen, WHITE, (self.x, self.y), self.r*0.25)


    def move_bomb(self):
        self.x += self.vx  # задаем скорость бомб
        self.y += self.vy
        if min(self.x, abs(self.x - screen_x)) <= self.r:  # отталкивание от границ экрана
            self.vx = -self.vx
            self.x += 2 * self.vx
        if min(self.y, abs(self.y - screen_y)) <= self.r:
            self.vy = -self.vy
            self.y += 2 * self.vy
        self.r += 0.2
        if self.r >= FPS * 0.2 * 3 + 10:
            self.bills = -3
        elif self.r >= FPS * 0.2 * 2 + 10:
            self.bills = 1
        elif self.r >= FPS * 0.2 * 1 + 10:
            self.bills = 2

def table:
    names = open(scor)

    print(a, b, c, file=output)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0
counter = 0
balls = [Ball() for _ in range(10)]
for i in range(len(balls)):
    balls[i].make_ball()
bombs = [Bomb() for _ in range(1)]
for i in range(len(bombs)):
    bombs[i].make_bomb()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            for i in range(len(balls)):
                if (mouse[0] - balls[i].x) ** 2 + (mouse[1] - balls[i].y) ** 2 <= balls[i].r ** 2:
                    score += 1
                    balls.remove(balls[i])
                    balls.append(Ball())
                    balls[-1].make_ball()
            for i in range(len(bombs)):
                if (mouse[0] - bombs[i].x) ** 2 + (mouse[1] - bombs[i].y) ** 2 <= bombs[i].r ** 2:
                    score += bombs[i].bills
                    bombs.remove(bombs[i])
                    counter = pygame.time.get_ticks()
    for i in range(len(balls)):
        balls[i].move_ball()
        balls[i].make_ball()
    if len(bombs) != 0:
        for i in range(len(bombs)):
            bombs[i].move_bomb()
            bombs[i].make_bomb()
            if bombs[i].bills == -3:
                bombs.remove(bombs[i])
                score += -3
                counter = pygame.time.get_ticks()
    elif pygame.time.get_ticks() - counter >= 1500:
        bombs.append(Bomb())
        bombs[-1].make_bomb()
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
print('КАК ВАС ЗОВУТ?')
name = input()
if score >=1:
    print(name, ',ВАШ СЧЕТ', score)
else:
    print(name, ',УВЫ, ВАШ СЧЕТ ВСЕГО', score)

