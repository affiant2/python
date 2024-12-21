#导入库
import turtle
import random
import time
import _thread

turtle.shape("turtle")
turtle.speed(0)
turtle.tracer(0)

pp  =turtle.Turtle()
pp.up()
pp.goto(-300,220)
pp.down()
grade = 0
pp.write(f"点击w,a,s,d控制上下左右,总分{grade}",font=10)
#控制
def w():
    turtle.up()
    turtle.seth(90)
    turtle.fd(20)
    turtle.down()
    o()
    turtle.update()
def s():
    turtle.up()
    turtle.seth(-90)
    turtle.fd(20)
    turtle.down()
    o()
    turtle.update()
def a():
    turtle.up()
    turtle.seth(180)
    turtle.fd(20)
    turtle.down()
    o()
    turtle.update()
def d():
    turtle.up()
    turtle.seth(0)
    turtle.fd(20)
    turtle.down()
    o()
    turtle.update()
turtle.onkey(w,'w')
turtle.onkey(s,'s')
turtle.onkey(a,'a')
turtle.onkey(d,'d')
turtle.listen()
i = 0
#得失判断
a = turtle.Turtle()
a.hideturtle()
a.speed(0)
def o():
    global grade
    x1 = a.xcor()
    y1 = a.ycor()
    if turtle.distance(x1,y1) <=14:
        a.clear()
        print("分数+1")
        grade+=1
        pp.undo()
        pp.write(f"点击w,a,s,d控制上下左右,总分{grade}", font=10)
        k()
    if turtle.distance(0,0) >=252:
        turtle.up()
        turtle.home()
        turtle.down()
        print("你死了，分数-1")
        grade-=1
        pp.undo()
        pp.write(f"点击w,a,s,d控制上下左右,总分{grade}", font=10)
#圆
def k():
    x = random.randint(-195,195)
    y = random.randint(-195,195)
    a.up()
    a.goto(x,y)
    a.down()
    a.fillcolor("red")
    a.begin_fill()
    a.circle(7)
    a.end_fill()
k()

#边界
bj = turtle.Turtle()
bj.pensize(3)
bj.hideturtle()
bj.color("red")
bj.up()
bj.goto(0,-250)
bj.down()
bj.circle(250)
#背景
xhb = turtle.Turtle()
xhb.color("green")
turtle.tracer(0)
xhb.up()
xhb.goto(0,-250)
xhb.down()
xhb.hideturtle()
for i in range(100000):
    xhb.clear()
    xhb.up()
    xhb.goto(0,0)
    xhb.down()
    for j in range(500):
        xhb.fd(j)
        xhb.left(90)
    xhb.right(1)
    time.sleep(0.1)
    turtle.update()