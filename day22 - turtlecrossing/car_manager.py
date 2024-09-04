import random
import turtle
from turtplayer import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
speed_count = 0

STARTING_LANES = [()]

class CarManager(Player):

    def __init__(self):
        super().__init__()
        self.car_list = []
        self.createcars()
        self.player_instance.hideturtle()  #hides the second turtle created by inheriting player.
    def createcars(self):
        self.addcars()

    def addcars(self):  #create a singular body
        global speed_count
        rand_color = random.choice(COLORS)
        rand_y = random.randint(-250, 250)
        car = turtle.Turtle("square")
        car2 = turtle.Turtle("square")
        car.penup()
        car2.penup()
        car.color(rand_color)
        car2.color(rand_color)
        car.setheading(180)
        car2.setheading(180)
        if speed_count <= 10:
            car.speed("fastest")
            car.goto(200, rand_y)
            car2.goto(220, rand_y)
            speed_count += 1
        else:
            car.speed("fast")
            car.goto(300, rand_y)
            car2.goto(320, rand_y)
        self.car_list.append(car)
        self.car_list.append(car2)
        self.car_instance = self.car_list[0]

    #make bodies move
    def carmove(self):
        for i in self.car_list:
            i.forward(STARTING_MOVE_DISTANCE)
            #use player to detect speed change:


    def new_speed(self):
        for i in self.car_list:
            i.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT)
