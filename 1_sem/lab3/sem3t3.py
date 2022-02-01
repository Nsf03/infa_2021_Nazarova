# семинар 3
# t4
# поле тяжести
import turtle
import turtle as tr
import random as rd

tr.shape('circle')
tr.speed()
tr.shapesize(0.7)
tr.color('black')
tr.width(1)

tr.penup()
tr.goto(300, 0)
tr.pendown()
tr.goto(-300, 0)

vx = 5
vy = 30
x0 = -300
y0 = 0
t0 = 0
x = -300
y = 0
a = -2
dt = 1

for _ in range(0, 10000):
    x += vx * dt
    vy += a * dt
    y += vy * dt + a * dt ** 2 / 2
    if y <= 0:
        y = 0
        vy = -vy
    tr.goto(x, y)
