from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "left"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.turt_score()

    def turt_score(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(-280, 260)
        self.write(f"Level: {self.level}", False, align=ALIGN, font=FONT)


    def game_over(self):
        self.color("white")
        self.setpos(0,0)
        self.write("GAME OVER.", False, align="center", font=FONT)


