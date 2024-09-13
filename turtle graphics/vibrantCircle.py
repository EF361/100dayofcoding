# TODO draw a vibrant circle

import turtle as t

screen = t.Screen()
screen.bgcolor("black")
t.pencolor("white")
t.hideturtle()
t.speed(0)
a = 0
b = 0
t.pu()
t.goto(0, 200)
t.pd()

while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 210:
        break
screen.exitonclick()
