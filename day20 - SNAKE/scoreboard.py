from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

with open("data.txt") as file:
    contents = file.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        self.high_score = int(contents)
        self.score()

    def score(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(0, 260)
        self.clear()
        self.write(f"Score: {self.count} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.count > int(self.high_score):
            self.high_score = self.count
            with open("data.txt", mode="w") as file2:
                file2.write(str(self.count))
        self.count = 0
        self.score()
