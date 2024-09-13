from turtle import Screen
from paddle import Paddle as p

# setup the screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")

paddle = p.Paddle()

screen.listen()

screen.onkeypress(p.go_up, "Up")

screen.exitonclick()
