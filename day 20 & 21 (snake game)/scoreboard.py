from turtle import Turtle as T

FONT = ("courier", 12, "normal")
ALIGNMENT = "center"


class Scoreboard(T):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.goto(-10, 280)
        self.hideturtle()
        self.update_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()
