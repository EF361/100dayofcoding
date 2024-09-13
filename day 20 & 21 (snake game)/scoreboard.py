from turtle import Turtle as T

FONT = ("courier", 12, "normal")
ALIGNMENT = "center"


class Scoreboard(T):
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-10, 280)
        self.hideturtle()
        self.update_score()
