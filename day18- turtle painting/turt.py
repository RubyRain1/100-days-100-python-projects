import turtle as t  # this assigns turtle to t to save time
from turtle import Turtle, Screen
import random

timmy = Turtle()

color_table = ['red', 'blue', 'green', 'orange', 'pink', 'white', 'cyan', 'chartreuse']

timmy.shape("turtle")
timmy.color("chartreuse")


def drawshape(num_sides):
    angle = 360 / num_sides
    color_random = random.randint(0, 7)
    timmy.pencolor(color_table[color_random])
    for i in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


myScreen = Screen()
myScreen.bgcolor("black")
timmy.penup()
timmy.setpos(0, 200)
timmy.pendown()
for sides in range(3, 11):
    drawshape(sides)

myScreen.exitonclick()
