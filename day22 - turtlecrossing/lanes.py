import turtle
from turtle import Turtle

y_start = -250
y_end = 250
x_start_positions = [-290, -283, -250, -243, -210, -203, -170, -163, -130, -123,
                     -90, -83, -50, -43, -10, -3, 30, 37, 70, 77, 100, 107,
                     140, 147, 180, 187, 220, 227, 260, 267, 290, 297]


class Lanes(Turtle):  # this is incase I want to make lanes and improve the game.

    def __init__(self):
        super().__init__()
        self.lane_list = []
        self.lanes()
        self.hideturtle()

    def lanes(self):
        for y in range(y_start, y_end + 1, 70):
            for x in x_start_positions:
                self.make_lanes((x, y))

    def make_lanes(self, start_lane):
        lane = turtle.Turtle("square")
        lane.color("white")
        lane.penup()
        lane.shapesize(stretch_wid=.4, stretch_len=.3)
        lane.goto(start_lane)
        self.lane_list.append(lane)
