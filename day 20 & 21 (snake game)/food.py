from turtle import Turtle
import random as r


class Food(Turtle):
    def refresh(self):
        random_x = r.randint(-250, 250)
        random_y = r.randint(-250, 250)
        self.goto(random_x, random_y)

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()
