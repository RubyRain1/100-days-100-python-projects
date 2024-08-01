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

def dotcolor():
    rColor = color_list[random.randint(0, 26)]
    return rColor

def dotrow():
    global turn_logic, turn_check
    timmy.speed("fastest")
    timmy.dot(40, dotcolor())
    for i in range(0,11):
        timmy.penup()
        timmy.forward(5)
        timmy.pendown()


def turnleft():
    timmy.speed("fastest")
    timmy.penup()
    timmy.left(90)
    timmy.forward(20)
    timmy.left(90)

def newrow():
    timmy.penup()
    timmy.setpos(0, y)
    timmy.pendown()

timmy = t.Turtle()
timmy.color("white")
timmy.shape("turtle")
my_screen = t.Screen()
my_screen.bgcolor(113,98,122)

while cont:
    while count <5:
        dotrow()
        count+=1
        y+= 10
    newrow()
    #this helps to finish the program.
    count = 0
    rows += 1
    if rows == 5:  #once five rows are made the program while loop stops.
        timmy.hideturtle()
        cont = False


my_screen.exitonclick()
