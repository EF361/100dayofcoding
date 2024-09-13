from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        self = Turtle(shape="square")
        self.penup()
        self.speed("fastest")
        self.goto(x=350, y=0)
        self.shapesize(5, 1, 1)
        self.color("white")

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
