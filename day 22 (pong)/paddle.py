from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        self.paddle = Turtle(shape="square")
        self.paddle.penup()
        self.paddle.speed("fastest")
        self.paddle.goto(x=350, y=0)
        self.paddle.shapesize(5, 1, 1)
        self.paddle.color("white")
