from snake import Snake
import turtle as t
from turtle import Turtle
import random



class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #coming from inherited super class of turtle
        self.spawn()

    def spawn(self):
        self.color("white")
        self.speed("fastest")
        self.goto(random.randint(-280, 280), random.randint(-280, 280))


