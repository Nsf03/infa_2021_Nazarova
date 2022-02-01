import pygame as pg

pg.init()

FPS = 30
screen = pg.display.set_mode((400, 400))

xr=200
yr=200
yel = (240, 230, 140)
red = (255, 99, 71)
bl = (0, 0, 0)
gray = (211, 211, 211)
color = (255, 255, 255)

screen.fill(gray)


pg.draw.circle(screen, bl, (xr, yr), 101, 5)
pg.draw.circle(screen, yel, (xr, yr), 100)
pg.draw.rect(screen, bl, (xr-50, yr+40, 100, 20))
pg.draw.circle(screen, red, (xr+50, yr-30), 20)
pg.draw.circle(screen, red, (xr-50, yr-30), 25)
pg.draw.circle(screen, bl, (xr+50, yr-30), 10)
pg.draw.circle(screen, bl, (xr-50, yr-30), 10)
pg.draw.circle(screen, bl, (xr+50, yr-30), 20, 1)
pg.draw.circle(screen, bl, (xr-50, yr-30), 25, 1)
pg.draw.line(screen, bl, (xr+20, yr-40), (xr+80, yr-80), 10)
pg.draw.line(screen, bl, (xr-20, yr-40), (xr-80, yr-80), 10)
pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()

pg.quit()
