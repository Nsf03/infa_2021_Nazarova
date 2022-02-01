import math
from random import choice
from random import randint as rnd

import pygame

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

g = 3
down = 590
move_counter = 0
x_0 = 40
y_0 = 450
padej = ''


class Ball:
    def __init__(self, screen: pygame.Surface, type, x=x_0, y=y_0):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        vx - скорость мяча по оси x
        xy - скорость мяча по оси y
        color - цвет мяча
        live - время жизни шарика
        """
        self.screen = screen
        self.type = type
        self.x = x
        self.y = y
        if self.type == 0:
            self.r = 10
            self.limit = 1
            self.live = 30
        else:
            self.r = 30
            self.limit = 0.5
            self.live = 60
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.live == 0:
            balls.pop(balls.index(self))
        else:
            if min(self.x, abs(self.x - WIDTH)) <= self.r:  # отталкивание от границ экрана
                self.vx = -self.vx
                self.x += 2 * self.vx
            if min(self.y, abs(self.y - HEIGHT)) <= self.r:
                self.vy = -self.vy
                self.y -= 2 * self.vy
            self.x += self.vx
            self.vy -= g
            self.y -= self.vy

    def draw(self):
        if self.type == 0:
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        if self.type == 1:
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
            pygame.draw.ellipse(self.screen, BLACK, ((self.x, self.y), (2, 15)))

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        rad = max(obj.r, self.r)
        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= rad ** 2:
            balls.pop(balls.index(self))
            return True
        else:
            return False


class Gun:
    def __init__(self):
        """
        screen - экран где рисуется пушка
        f2_power - сила выстрела
        f2_on - 1 если пушка заряжена, 0 - если нет
        an - угол поворота пушки
        color - цвет пушки
        """
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = x_0
        self.y = y_0

    def fire2_start(self, event):
        """
        Заряжает пушку
        """
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, ball_type)
        new_ball.r += 5
        new_ball.x = self.x
        new_ball.y = self.y
        self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an) * new_ball.limit  # если мяч большой то медленнее в два раза
        new_ball.vy = - self.f2_power * math.sin(self.an) * new_ball.limit
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targeting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if (event.pos[0] - self.x) != 0:
                self.an = math.atan2((event.pos[1] - self.y), (event.pos[0] - self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        width = 10
        coords = [
            (self.x, self.y),
            (self.x + (self.f2_power + 20) * math.cos(self.an),
             self.y + (self.f2_power + 20) * math.sin(self.an)),
            (self.x + (self.f2_power + 20) * math.cos(self.an) + width * math.sin(self.an),
             self.y + (self.f2_power + 20) * math.sin(self.an) - width * math.cos(self.an)),
            (self.x + width * math.sin(self.an), self.y - width * math.cos(self.an))
        ]
        pygame.draw.polygon(self.screen, self.color, (coords))
        pygame.draw.rect(self.screen, self.color, ((self.x - 20, self.y - 10), (60, 20)))
        pygame.draw.circle(self.screen, BLACK, (self.x-15, self.y +10), 10)
        pygame.draw.circle(self.screen, BLACK, (self.x , self.y + 10), 10)
        pygame.draw.circle(self.screen, BLACK, (self.x + 15, self.y + 10), 10)
        pygame.draw.circle(self.screen, BLACK, (self.x + 30, self.y + 10), 10)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:

    def __init__(self, type):
        """ Инициализация новой цели. """
        self.type = type
        self.screen = screen
        if self.type == 0:
            self.x = rnd(600, 750)
            self.y = rnd(300, 550)
            self.vx = rnd(-7, 7) + 1
            self.vy = rnd(-7, 7) + 1
        elif self.type == 1:
            self.x = 300
            self.y = 300
            self.alpha = 0.1
            self.omega = rnd(5, 10)
        self.color = RED
        self.r = rnd(30, 50)
        self.live = 1
        self.points = 1

    def hit(self):
        """Попадание шарика в цель."""
        self.live -= 1
        global points
        points += self.points

    def draw(self):
        if self.live == 1:
            if self.type == 0:
                pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
                pygame.draw.circle(screen, BLACK, (self.x, self.y), self.r, width=1)
                pygame.draw.circle(screen, WHITE, (self.x, self.y), self.r * 0.75)
                pygame.draw.circle(screen, self.color, (self.x, self.y), self.r * 0.5)
                pygame.draw.circle(screen, WHITE, (self.x, self.y), self.r * 0.25)
            elif self.type == 1:
                pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
                pygame.draw.circle(screen, BLACK, (self.x, self.y), self.r, width=1)
                pygame.draw.circle(screen, BLACK, (self.x, self.y), self.r * 0.75)
                pygame.draw.circle(screen, self.color, (self.x, self.y), self.r * 0.5)
                pygame.draw.circle(screen, BLACK, (self.x, self.y), self.r * 0.25)

    def move(self):
        """перемещает себя согласно значениям скорости"""
        global move_counter
        if self.type == 0:
            if min(self.x, abs(self.x - WIDTH)) <= self.r + 5:  # отталкивание от границ экрана
                self.vx = -self.vx
                self.x += 3 * self.vx
            if min(self.y, abs(self.y - HEIGHT)) <= self.r + 5:
                self.vy = -self.vy
                self.y += 3 * self.vy
            self.x += self.vx
            self.y += self.vy
        if self.type == 1:
            self.x += self.omega * math.sin(self.alpha * move_counter)
            self.y += self.omega * math.cos(self.alpha * move_counter)
            move_counter += 1


def show_score():
    f1 = pygame.font.Font(None, 36)
    note1 = str(points)
    text1 = f1.render(note1, True, BLACK)
    screen.blit(text1, (10, 15))


def show_hit():
    global padej, bullet
    f1 = pygame.font.Font(None, 36)
    if (bullet_show % 10) == 1 and (bullet_show % 100) != 11:
        padej = ' выстрела'
    elif bullet_show % 10 == 2 or bullet_show % 10 == 3 or bullet_show % 10 == 4:
        padej = ' выстрела'
    else:
        padej = ' выстрелов'
    note2 = ('Вы уничтожили цели за ' + str(bullet_show) + padej)
    text2 = f1.render(note2, True,
                      BLACK)
    screen.blit(text2, (200, 260))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
points = 0
ball_type = 0

clock = pygame.time.Clock()
gun = Gun()
target = Target(0)
target1 = Target(1)
show = 0
show_live = 30
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    target1.draw()
    show_score()
    if show == 1:
        show_hit()
        show_live -= 1
        if show_live < 1:
            show = 0
            show_live = 30
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targeting(event)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                ball_type = 0
            elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                ball_type = 1
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        if gun.x >= x_0:
            gun.x -= 10
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        if gun.x <= x_0 + 640:
            gun.x += 10

    for b in balls:
        b.move()
        b.live -= 1
        if b.hittest(target) and target.live == 1:
            target.live = 0
            target.hit()
        if b.hittest(target1) and target1.live == 1:
            target1.live = 0
            target1.hit()
        if target1.live < 1 and target.live < 1:
            target = Target(0)
            target1 = Target(1)
            show = 1
            bullet_show = bullet
            bullet = 0
    gun.power_up()
    target.move()
    target1.move()
pygame.quit()
