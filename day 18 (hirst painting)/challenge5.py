# TODO draw a spirograph

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def radius():
    r = random.randint(50, 100)
    return r


r = radius()
for _ in range(36):
    tim.circle(r)
    tim.color(random_color())
    tim.setheading(tim.heading() + 10)

screen = t.Screen()
screen.exitonclick()
