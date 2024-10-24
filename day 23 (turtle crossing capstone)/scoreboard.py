from turtle import Turtle as t

FONT = ("Courier", 24, "normal")


class Scoreboard(t):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def end_game(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
