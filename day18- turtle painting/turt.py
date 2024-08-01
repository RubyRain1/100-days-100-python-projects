import turtle
import turtle as t  # this assigns turtle to t to save time
from turtle import Turtle, Screen
import random

timmy = Turtle()

# color_table = ['red', 'blue', 'green', 'orange', 'pink', 'white', 'cyan', 'chartreuse']

direction = [0, 90, 180, 270]
timmy.shape("turtle")
timmy.color("chartreuse")
t.colormode(255)

# def drawshape(num_sides):
#     angle = 360 / num_sides
#     color_random = random.randint(0, 7)
#     timmy.pencolor(color_table[color_random])
#     for i in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)

def randcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color_tuple = (r,g,b)
    return color_tuple
# def randwalk():
#     timmy.speed("fastest")
#     pensize = 1
#     for i in range(50):
#         timmy.pencolor(randcolor())
#         steps = int(random.randint(0, 50))
#         angle = int(random.choice(direction))
#         timmy.pensize(pensize)
#         timmy.right(angle)
#         timmy.forward(steps)
#         pensize += 1

def spirograph(size):
    timmy.speed("fastest")
    for i in range(int(360 / size)):
        timmy.pencolor(randcolor())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size)
        timmy.tilt(50)

myScreen = Screen()
myScreen.bgcolor("black")
timmy.penup()
# timmy.setpos(0, 200)
timmy.pendown()
# for sides in range(3, 11):
#     drawshape(sides)
# randwalk()
spirograph(5)
myScreen.exitonclick()
