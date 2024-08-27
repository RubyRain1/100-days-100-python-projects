from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        self.score()

    def score(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(0, 260)
        self.write(f"Score: {self.count}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color("white")
        self.setpos(0,0)
        self.write("GAME OVER.", False, align=ALIGNMENT, font=FONT)
