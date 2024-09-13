from turtle import Turtle


class Paddle:
    def __init__(self, x_position, y_position):
        self.position = (x_position, y_position)
        self.create_paddle()

    def create_paddle(self):
        self.paddle = Turtle(shape="square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(self.position)

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)
