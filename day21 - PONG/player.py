import time
import turtle
from turtle import Turtle

PLAYER_STARTING_POSITIONS = [(-100, 0), (-100, -20), (-100, -40)]
COMPUTER_STARTING_POSITIONS = [(100, 0), (100, -20), (100, -40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
CPU_POSITIONS = [(100, 275), (100, -275)]


class Player:

    def __init__(self):
        self.player_list = []
        self.createbody_player()
        self.player_start = self.player_list[0]

    def createbody_player(self):
        for start_player_body in PLAYER_STARTING_POSITIONS:
            self.add_body_player(start_player_body)

    def player_move(self):
        for i in range(len(self.player_list) - 1, 0, -1):
            next_x = self.player_list[i - 1].xcor()
            next_y = self.player_list[i - 1].ycor()
            self.player_list[i].goto(next_x, next_y)
        self.player_start.forward(MOVE_DISTANCE)

        if self.player_start.ycor() < -275:
            self.player_start.setheading(90)
        elif self.player_start.ycor() > 275:
            self.player_start.setheading(270)

    def add_body_player(self, start_player_body):
        player = turtle.Turtle("square")
        player.color("white")
        player.penup()
        player.goto(-420,0)
        self.player_list.append(player)

    def up(self):
        self.player_start.setheading(UP)


    def down(self):
        self.player_start.setheading(DOWN)

