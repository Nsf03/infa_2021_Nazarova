# семинар 3
# t5
#реальный газ
from random import randint
import turtle as tr
from math import sqrt


n = 25
dt=0.5
dist=10
xt=[]
yt=[]
vxt=[]
vyt=[]
flag=[0 for i in range(n)]
flag0=flag

pool = [tr.Turtle(shape='circle') for i in range(n)]
for unit in pool:
    unit.shapesize(0.5)
    unit.penup()
    unit.speed(50)
    x=randint(-300, 300)
    y=randint(-300, 300)
    unit.goto(x, y)
    xt.append(x)
    yt.append(y)

for i in range(n):
    vxt.append(randint(1, 15)*randint(-1, 1)+0.1)
    vyt.append(randint(1, 15)*randint(-1, 1)+0.1)

for _ in range (100):
    i=0
    for unit in pool:
        vx=vxt[i]
        vy=vyt[i]
        x=vx*dt+xt[i]
        y=vy*dt+yt[i]
        unit.goto(x, y)
        xt[i]=x
        yt[i]=y
        i+=1
    for a in range(n):
        if abs(xt[a]-350)<=1 or abs(xt[a]+350)<=1 or abs(xt[a])>350:
            xt[a]=xt[a]-abs(xt[a])/xt[a]*dist/2
            vxt[a]=-vxt[a]
            pool[a].goto(xt[a], yt[a])
        if (abs(yt[a]-250)<=1 or abs(yt[a]+250)<=1) or abs(yt[a])>250:
            yt[a]=yt[a]-abs(yt[a])/yt[a]*dist/2
            pool[a].goto(xt[a], yt[a])
            vyt[a]=-vyt[a]
        for b in range(n):
            if sqrt((xt[a]-xt[b])**2+(yt[a]-yt[b])**2)<=dist and a != b and flag[b]!=1:
                flag[a]=1
                vxt[a], vxt[b] = vxt[b], vxt[a]
                vyt[a], vyt[b] = vyt[b], vyt[a]
                xt[a] = xt[a]+(abs(vxt[a])/vxt[a])*dist/2
                yt[a] = yt[a] + (abs(vyt[a]) / vyt[a]) * dist/2
                xt[b] = xt[b] + (abs(vxt[b]) / vxt[b]) * dist/2
                yt[b] = yt[b] + (abs(vyt[b]) / vyt[b]) * dist/2
                pool[a].goto(xt[a], yt[a])
                pool[b].goto(xt[b], yt[b])







