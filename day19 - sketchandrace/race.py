import turtle
import turtle as t
from turtle import Turtle, Screen
import random
cont = True
y = 125
racing = False
colors = ['blue', 'green', 'yellow', 'purple', 'red', 'orange']
turtle_list = []

screen = Screen()
screen.setup(500,400)
userI = screen.textinput("bet", "which turtle will win the race")

for i in range(0,6):
    timmy = t.Turtle(shape="turtle")
    timmy.color(colors[i])
    timmy.penup()
    timmy.setpos(-230, y)
    y -= 50
    turtle_list.append(timmy)


if userI:
    racing = True


while racing:
    for i in turtle_list: #random distance will be assigned to each turtle to race

        if i.xcor() > 230:
            if userI == i.pencolor():
                racing = False
                print(f"{i.pencolor()} wins the race, YOU WON")
            else:
                print(f"{i.pencolor()} wins the race, YOU LOSE")
        distance = random.randint(0, 10)
        i.forward(distance)



screen.exitonclick()
