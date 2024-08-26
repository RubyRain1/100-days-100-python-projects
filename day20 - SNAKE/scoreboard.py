from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        self.score()


    def score(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(0,270)
        self.write(f"Score: {self.count}", False, align="center", font=("Arial", 13, "normal"))


