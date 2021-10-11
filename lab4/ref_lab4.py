import pygame
from pygame.draw import *
import random as rd

pygame.init()

screen_x = 600
screen_y = 1000

FPS = 30
screen = pygame.display.set_mode((screen_x, screen_y))

sky_color = (0, 255, 255)
land_color = (0, 255, 0)
sun_color = (255, 255, 0)
horizon_level = 500
trees_number = 7
apple_color = (255, 99, 71)
leaf_color = (0, 128, 0)
up_leaf_color = (152, 251, 152)
tree_color = (222, 184, 135)
forest_size = 0.9
body_color = (255, 255, 255)
corn_color = (250, 128, 114)
unicorn_size = 0.11


def land_sky(c_sky, c_land, horizon):
    rect(screen, c_land, (0, horizon, 600, screen_y - horizon))
    rect(screen, c_sky, (0, 0, 600, horizon))


'''
Функция рисует небо и землю
c_sky - цвет неба, заданный в формате (RGB)
c_land - цвет земли, заданный в формате (RGB)
horizon - уровень горизонта
'''


def sun(c_sky, x, y, r_sun):
    r = c_sky[0]
    g = c_sky[1]
    b = c_sky[2]
    for i in range(255):
        circle(screen, (r, g, b), (x, y), r_sun)  # градиент
        if b > 0:
            b -= 1
        if r < 255:
            r += 1
        r_sun -= 0.5


'''
Функция рисует солнце
c_sky - цвет неба, заданный в формате (RGB)
x, y  - координаты центра солнца
r_sun - радиус солнца
'''


def forest(c_apple, c_leaf, up_c_leaf, c_tree, trees_num, tree_size):
    sr1 = pygame.Surface((200, 360))
    sr1.fill((0, 0, 0))

    rect(sr1, c_tree, (85, 210, 30, 150))
    ellipse(sr1, c_leaf, (35, 0, 130, 145))
    ellipse(sr1, up_c_leaf, (35, 0, 130, 145), 2)
    ellipse(sr1, c_leaf, (0, 60, 200, 85))
    ellipse(sr1, up_c_leaf, (0, 60, 200, 85), 2)
    ellipse(sr1, c_leaf, (40, 127, 120, 85))
    ellipse(sr1, up_c_leaf, (40, 127, 120, 85), 2)
    circle(sr1, c_apple, (20, 105), 13)
    circle(sr1, c_apple, (170, 107), 13)
    circle(sr1, c_apple, (140, 170), 13)
    circle(sr1, c_apple, (80, 70), 13)

    sr1.set_colorkey((0, 0, 0))  # обесцвечивает фон деревье

    for i in range(1, trees_num + 1):
        sr = pygame.transform.rotozoom(sr1, 0, rd.randint(70, 120) / 100 * tree_size)
        sr.set_colorkey((0, 0, 0))
        screen.blit(sr, (screen_x / 6 + rd.randint(int(-screen_x / 3), 0),
                         (horizon_level / 2) + i * (screen_y - horizon_level / 2) / trees_num / 2))


'''
Функция рисует яблоневый сад
c_apple - цвет яблок, заданный в формате (RGB)
c_leaf - цвет листвы, заданный в формате (RGB)
c_tree - цвет ствол, заданный в формате (RGB)
trees_num - количество яблонь
tree_size - размер яблонь (порядка 0,1 - 2)
'''


def unicorn(c_body, c_corn, uni_size):
    sre = pygame.Surface((400, 400))  # поверхностьь для единорога
    sre.fill((0, 0, 0))

    ellipse(sre, c_body, (70, 200, 200, 100))
    rect(sre, c_body, (90, 280, 20, 90))
    rect(sre, c_body, (125, 280, 20, 80))
    rect(sre, c_body, (200, 280, 20, 90))
    rect(sre, c_body, (230, 280, 20, 80))  # тело и ноги

    ellipse(sre, c_body, (200, 110, 70, 165))
    ellipse(sre, c_body, (230, 105, 85, 43))  # морда
    circle(sre, (c_corn), (260, 120), 9)  # глаз
    circle(sre, (0, 0, 1), (258, 118), 4)  # зрачок
    polygon(sre, (c_corn), ([225, 113], [235, 5], [245, 113]))  # рог

    ellipse(sre, (222, 177, 234), (185, 110, 65, 20))
    ellipse(sre, (222, 177, 234), (183, 112, 65, 20))
    ellipse(sre, (255, 239, 171), (182, 125, 60, 18))
    ellipse(sre, (255, 239, 171), (162, 165, 55, 23))
    ellipse(sre, (244, 216, 228), (172, 145, 52, 23))
    ellipse(sre, (176, 234, 222), (150, 175, 52, 23))
    ellipse(sre, (234, 177, 176), (150, 185, 55, 20))
    ellipse(sre, (234, 177, 176), (180, 135, 60, 23))  # грива

    ellipse(sre, (234, 177, 176), (55, 215, 60, 23))
    ellipse(sre, (214, 177, 176), (45, 220, 55, 20))
    ellipse(sre, (255, 239, 171), (0, 270, 63, 30))
    ellipse(sre, (222, 177, 234), (35, 250, 65, 20))
    ellipse(sre, (255, 239, 171), (40, 260, 60, 18))
    ellipse(sre, (255, 239, 171), (35, 227, 55, 23))
    ellipse(sre, (244, 216, 228), (10, 240, 62, 33))
    ellipse(sre, (176, 234, 222), (35, 270, 32, 23))
    ellipse(sre, (200, 177, 176), (40, 280, 60, 23))
    ellipse(sre, (176, 234, 222), (45, 270, 55, 23))  # хвост
    sre.set_colorkey((0, 0, 0))
    sre1 = pygame.transform.rotozoom(sre, 0, uni_size * 5)
    sre1.set_colorkey((0, 0, 0))
    sre1 = pygame.transform.flip(sre1, 150, 0)
    screen.blit(sre1, (screen_x / 4, horizon_level * 0.9))
    sre1 = pygame.transform.rotozoom(sre, 0, uni_size * 4.5)
    sre1 = pygame.transform.flip(sre1, 150, 0)
    sre1.set_colorkey((0, 0, 0))
    screen.blit(sre1, (screen_x * 4 / 7, horizon_level * 1.1))
    sre1 = pygame.transform.rotozoom(sre, 0, uni_size * 6)
    sre1.set_colorkey((0, 0, 0))
    screen.blit(sre1, (screen_x / 2, horizon_level * 1.3))


'''
Функция рисует единорогов
c_ode - цвет тела единорогов, заданный в формате (RGB)
c_corn - цвет рога, заданный в формате (RGB)
uni_size - размер единорогов (порядка 0,1 - 2)
'''

land_sky(sky_color, land_color, horizon_level)
sun(sky_color, 400, 200, 150)
unicorn(body_color, corn_color, unicorn_size)
forest(apple_color, leaf_color, up_leaf_color, tree_color, trees_number, forest_size)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
