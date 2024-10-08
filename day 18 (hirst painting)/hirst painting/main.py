# TODO hirst painting
import turtle as t
import random

color_list = [
    (199, 175, 117),
    (124, 36, 24),
    (210, 221, 213),
    (168, 106, 57),
    (222, 224, 227),
    (186, 158, 53),
    (6, 57, 83),
    (109, 67, 85),
    (113, 161, 175),
    (22, 122, 174),
    (64, 153, 138),
    (39, 36, 36),
    (76, 40, 48),
    (9, 67, 47),
    (90, 141, 53),
    (181, 96, 79),
    (132, 40, 42),
    (210, 200, 151),
    (141, 171, 155),
    (179, 201, 186),
    (172, 153, 159),
    (212, 183, 177),
    (176, 198, 203),
    (150, 115, 120),
    (202, 185, 190),
    (40, 72, 82),
    (46, 73, 62),
    (47, 66, 82),
]

tim = t.Turtle()
t.colormode(255)
tim.hideturtle()
tim.speed("fastest")

y = -250
tim.pu()

for i in range(10):
    tim.setx(-250)
    tim.sety(y)
    for i in range(10):
        color = random.choice(color_list)
        tim.pd()
        tim.dot(20, color)
        tim.fillcolor(color)
        tim.pu()
        tim.forward(50)

    y += 50

screen = t.Screen()
screen.exitonclick()
