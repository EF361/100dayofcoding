# TODO draw a random walk

import random
import turtle as t

tim = t.Turtle()
t.colormode(255)


def random_color():
    color = ()
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]
tim.width(30)
tim.speed("fastest")

for i in range(500):
    tim.color(random_color())
    tim.forward(50)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
