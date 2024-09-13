# TODO draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon

from turtle import Turtle, Screen
import random

tim = Turtle()
color = ["red", "orange", "yellow", "blue", "green", "purple", "pink", "brown"]

for i in range(3, 11):
    color_chose = random.choice(color)
    tim.color(color_chose)
    for j in range(i):
        tim.forward(100)
        tim.right(360 / i)
    color.remove(color_chose)


screen = Screen()
screen.exitonclick()
