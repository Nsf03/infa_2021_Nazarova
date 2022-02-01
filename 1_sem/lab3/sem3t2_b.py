# семинар 3
# t2
import turtle as tr

tr.shape('turtle')
tr.speed()
tr.color('blue')
tr.width(3)

tr.penup()
tr.goto(-300, 50)
tr.pendown()

c0, c1, c2, c3, c4, c5, c6, c7, c8, c9 = [], [], [], [], [], [], [], [], [], []
c = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]
cn = ('c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9')
i = 0

numbers = open('numbers.txt', 'r')
while True:
    line = numbers.readline()[:-1]
    if line in cn:
        c_num = line
        i = cn.index(c_num)
    if line not in cn:
        c[i].append(line)
    if not line:
        numbers.close()
        break

for sp in c:
    ind = 0
    for i in sp:
        i = tuple(map(float, i.split()))
        sp[ind] = i
        ind += 1


def let(c):
    tr.setheading(90)
    for i in c:
        if i[0] == 3:
            tr.penup()
            tr.left(i[1])
            tr.forward(i[2])
        else:
            tr.pendown()
            tr.left(i[0])
            tr.forward(i[1])


def write(x):
    x = str(x)
    l = list(x)
    l = [int(i) for i in l]
    for i in l:
        let(c[i])


write(123456)
