import random
import turtle
import time
from turtle import Turtle

MOVE_DISTANCE = 20
BALL_STARTING = [(0, 0)]


class Ball:

    def __init__(self):
        self.ball_list = []
        self.create_ball()
        self.ball_start = self.ball_list[0]
        self.ball_angle()

    def create_ball(self):
        for start_ball in BALL_STARTING:
            self.add_ball(start_ball)

    def add_ball(self,start_ball):
        ball = turtle.Turtle("square")
        ball.color("chartreuse")
        ball.penup()
        ball.goto(start_ball)
        self.ball_list.append(ball)

    def ball_move(self):
        self.ball_start.forward(MOVE_DISTANCE)

    def ball_angle(self):
        self.ball_start.setheading(random.randint(0, 360))

    def bounce_x(self):
        bounceangle = 180 - self.ball_start.heading()
        self.ball_start.setheading(bounceangle)

    def bounce_y(self):
        bounceangle = -self.ball_start.heading()
        self.ball_start.setheading(bounceangle)

    def ball_reset(self):
        self.ball_start.goto(0,0)

