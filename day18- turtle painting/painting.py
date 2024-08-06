import colorgram
import turtle as t
import random
import colorgram as cg

# colors = cg.extract("paint.jpg", 30)
# color_palette = []
#
# for count in colors:
#     r = count.rgb.r
#     g = count.rgb.g
#     b = count.rgb.b
#     new_tuple = (r, g, b)
#     color_palette.append(new_tuple)

color_list = [(238, 244, 250), (236, 224, 81), (197, 7, 70), (195, 164, 14), (110, 179, 215), (200, 76, 16),
              (231, 54, 132), (218, 162, 101), (28, 105, 168), (13, 23, 64), (35, 186, 110), (19, 29, 168),
              (211, 136, 177), (232, 223, 7), (199, 33, 132), (13, 183, 212), (230, 167, 199), (126, 189, 161),
              (9, 49, 28), (40, 132, 76), (128, 219, 232), (61, 12, 25), (67, 22, 7), (112, 90, 210), (147, 215, 199),
              (178, 17, 8), (234, 66, 34)]
print(len(color_list))
count = 0
cont = True
rows = 0
y = 0
t.colormode(255)  #allows the use of 0,255 rgb

numberofdots = 100

def dotrow():
    global turn_logic, turn_check
    timmy.speed("fastest")
    timmy.penup()
    timmy.setheading(225)
    timmy.forward(300)
    timmy.setheading(0)

    for i in range(1,numberofdots + 1):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
        if i % 10 == 0:
            timmy.setheading(90)
            timmy.forward(50)
            timmy.setheading(180)
            timmy.forward(500)
            timmy.setheading(0)


def turnleft():
    timmy.speed("fastest")


def turnright():
    timmy.setheading(0)

timmy = t.Turtle()
timmy.color("white")
timmy.shape("turtle")
my_screen = t.Screen()
my_screen.bgcolor(113,98,122)

dotrow()
timmy.hideturtle()
my_screen.exitonclick()
