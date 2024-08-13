import turtle as t
from turtle import Turtle, Screen
import random
cont = True
timmy = t.Turtle()
jimmy = t.Turtle()
zimmy = t.Turtle()
emmy = t.Turtle()
demmy = t.Turtle()
fizzy = t.Turtle()
timmy.color("purple"), timmy.shape("turtle"), timmy.penup()
jimmy.color("blue"), jimmy.shape("turtle"), jimmy.penup()
zimmy.color("green"), zimmy.shape("turtle"), zimmy.penup()
emmy.color("yellow"), emmy.shape("turtle"), emmy.penup()
demmy.color("orange"), demmy.shape("turtle"), demmy.penup()
fizzy.color("red"), fizzy.shape("turtle"), fizzy.penup()


def start():
    timmy.setpos(-400, 100)
    jimmy.setpos(-400, 50)
    zimmy.setpos(-400, 0)
    emmy.setpos(-400, -50)
    demmy.setpos(-400, -100)
    fizzy.setpos(-400, -150)


def movement(turt):
   turt.forward(random.randint(0, 20))


start()


movement(timmy)
movement(jimmy)
movement(zimmy)
movement(emmy)
movement(demmy)
movement(fizzy)

screen = Screen()
screen.exitonclick()
