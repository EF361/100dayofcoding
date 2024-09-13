from turtle import Screen
from paddle import Paddle

# setup the screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")

paddle = Paddle()

screen.listen()
screen.onkeypress("Up", )
screen.exitonclick()
