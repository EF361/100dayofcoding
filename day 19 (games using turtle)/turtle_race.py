from turtle import Turtle, Screen
import random

# screen
screen = Screen()  # declare an object for the screen
screen.setup(width=500, height=400)  # set the size of the screen
screen.title("Turtle Race")  # set the title of the screen
user_bet = screen.textinput(  # get the input from the user
    title="Enter your bet",
    prompt="Which turtle will win the race? Enter a color: \n",
)

# declare variables
color_list = ["red", "orange", "yellow", "green", "blue", "purple", "indigo"]
turtles = []
game_on = False
y = -130

for turtle_index in range(0, 7):
    y += 30
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color_list[turtle_index])
    new_turtle.goto(x=-230, y=y)
    turtles.append(new_turtle)

if user_bet:
    game_on = True

while game_on:
    for each_turtle in turtles:
        rand_steps = random.randint(0, 10)
        each_turtle.forward(rand_steps)
        if each_turtle.xcor() > 220:
            game_on = False
            win_turtle = each_turtle.pencolor()
            if user_bet == each_turtle.pencolor():
                print(f"You win! the {win_turtle} turtle is the winner!")
            else:
                print(f"You lost! the {win_turtle} turtle is the winner!")

screen.exitonclick()
