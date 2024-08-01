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
count = 0
cont = True
t.colormode(255)  #allows the use of 0,255 rgb

def dotcolor():
    rColor = color_list[random.randint(0, len(color_list) - 1)]
    return rColor

def dotrow():
    global turn_logic, turn_check
    ruby_jr.speed("fastest")
    ruby_jr.dot(20, dotcolor())
    for i in range(0,10):
        ruby_jr.penup()
        ruby_jr.forward(5)
        ruby_jr.pendown()


def turnleft():
    ruby_jr.penup()
    ruby_jr.left(90)
    ruby_jr.forward(20)
    ruby_jr.left(90)

def turnright():
    ruby_jr.penup()
    ruby_jr.right(90)
    ruby_jr.forward(20)

ruby_jr = t.Turtle()
ruby_jr.shape("turtle")


while cont:
    for i in range(0,5):
        dotrow()
    turnleft()
    for i in range(0,5):
        dotrow()
    turnright()
cont = False
my_screen = t.Screen()
my_screen.exitonclick()
