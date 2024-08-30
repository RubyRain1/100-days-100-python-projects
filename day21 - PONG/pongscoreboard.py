import turtle
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 40, "normal")
DIVIDER_STARTING_POSITIONS = \
    {(0, 240), (0, 231), (0, 222),
     (0, 182), (0, 173), (0, 164),
     (0, 124), (0, 115), (0, 106),
     (0, 66), (0, 57), (0, 48),
     (0, 8), (0, -1), (0, -10),
     (0, -50), (0, -59), (0, -68),
     (0, -108), (0, -117), (0, -126),
     (0, -166), (0, -175), (0, -184),
     (0, -224), (0, -233), (0, -242) }


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.divider_list = []
        self.player_score = 0
        self.computer_score = 0
        self.divider()
        self.player_score_number()
        self.computer_score_number()

    def divider(self):
        for start_player_body in DIVIDER_STARTING_POSITIONS:
            self.add_divider(start_player_body)

    def add_divider(self, start_divider):
        divider = turtle.Turtle("square")
        divider.color("white")
        divider.penup()
        divider.shapesize(stretch_wid=.4, stretch_len=.3)
        divider.goto(start_divider)
        self.divider_list.append(divider)

    def player_score_number(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(-40, 220)
        self.write(f"{self.player_score}", False, align=ALIGNMENT, font=FONT)

    def computer_score_number(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(40, 220)
        self.write(f"{self.computer_score}", False, align=ALIGNMENT, font=FONT)
