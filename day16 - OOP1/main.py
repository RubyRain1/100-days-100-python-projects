from turtle import Turtle, Screen

timmy = Turtle()
jimmy = Turtle()


def timmy_turtle():
    timmy.shape("turtle")
    timmy.color("chartreuse")


def jimmy_turtle():
    jimmy.shape("turtle")
    jimmy.color("white")


def square():
    count = 0
    while count <= 3:
        timmy.forward(105)
        timmy.left(90)
        timmy.forward(105)
        count += 1


def triangle():
    count = 0
    jimmy.penup()
    jimmy.setposition(-5, 210)
    jimmy.pendown()
    while count <= 2:
        jimmy.forward(120)
        jimmy.left(120)
        jimmy.forward(110)
        count += 1


def window():
    count = 0
    while count <= 3:
        jimmy.forward(20)
        jimmy.left(90)
        jimmy.forward(15)
        count += 1
    count = 0
    #inner frame vertical
    timmy.left(90)
    timmy.forward(20)
    #inner frame horizontal

    timmy.left(90)
    timmy.forward(10)
    timmy.left(90)
    timmy.pendown()
    timmy.forward(10)

myScreen = Screen()
myScreen.bgcolor("black")

timmy_turtle()
jimmy_turtle()

square()
triangle()
jimmy.penup()
jimmy.setposition(0, 230)
jimmy.pendown()
timmy.penup()
timmy.setposition(0, 230)
window()

myScreen.exitonclick()

# from prettytable import PrettyTable
#
# table = PrettyTable()
#
#
# table.add_column("Idol Name", ["ruby", "grave", "abyss"], "l")
# table.add_column("Fav Color", ["white", "teal", "purple"])
#
# print(table)
