from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# screen settings
screen = Screen()
screen.bgcolor("black")
screen.title("snake game")
screen.setup(width=600, height=600)
screen.tracer(0)


snake = Snake()
food = Food()
display = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

game_on = True
score = 0
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        display.increase_score()
        snake.extend()

    # detect collision with wall
    if (
        snake.head.xcor() < -295
        or snake.head.xcor() > 295
        or snake.head.ycor() < -295
        or snake.head.ycor() > 295
    ):
        game_on = False
        display.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            display.game_over()

screen.exitonclick()
