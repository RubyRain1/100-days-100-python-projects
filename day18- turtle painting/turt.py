import turtle as t #this assigns turtle to t to save time 
from turtle import Turtle, Screen
import random


timmy = Turtle()

color_table = ['red','blue','green','orange','pink','white','cyan','chartreuse']


timmy.shape("turtle")
timmy.color("chartreuse")

def square():
    count = 0
    random_color = random.randint(0,7)
    timmy.pencolor(color_table[random_color])
    while count <= 3:
        timmy.forward(100)
        timmy.right(90)
        timmy.forward(100)
        count += 1


def triangle():
    count = 0
    random_color = random.randint(0,7)
    timmy.pencolor(color_table[random_color])
    while count <= 2:
        timmy.forward(100)
        timmy.right(120)
        timmy.forward(100)
        count += 1

def dotline():
    count = 0
    random_color = random.randint(0,7)
    timmy.pencolor(color_table[random_color]) 
    while count<= 50:
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()
        count+=1

def pentagon():
    count = 0 
    random_color = random.randint(0,7)
    timmy.pencolor(color_table[random_color])
    while count<= 4:
        timmy.forward(100)
        timmy.right(72)
        timmy.forward(100)
        count += 1

def hexagon():
    count = 0 
    random_color = random.randint(0,7)
    timmy.pencolor(color_table[random_color])
    while count <= 5:
        timmy.forward(100)
        timmy.right(60)
        timmy.forward(100)
        count+=1

def heptagon():
    random_color = random.randint(0,7)
    timmy.pencolor(color_table[random_color])
    for i in range(7):
        timmy.forward(100)
        timmy.right(51.43)
        timmy.forward(100)


def octagon(): 
    random_color = random.randint(0,7)
    timmy.pencolor(color_table[random_color])
    for i in range(8):
        timmy.forward(100)
        timmy.right(45)
        timmy.forward(100)

def nonagon():
    random_color = random.randint(0,7)
    timmy.pencolor(color_table[random_color])
    for i in range(9):
        timmy.forward(100)
        timmy.right(40)
        timmy.forward(100)

def decagon():
    random_color = random.randint(0,7)
    timmy.pencolor(color_table[random_color])
    for i in range(10):
        timmy.forward(100)
        timmy.right(36)
        timmy.forward(100)

myScreen = Screen()
myScreen.bgcolor("black")
timmy.penup()
timmy.setpos(0,200)
timmy.pendown()
square()
triangle()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()
myScreen.exitonclick()