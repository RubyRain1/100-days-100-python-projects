import random
import turtle
from turtplayer import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
speed_count = 0
FIRST_XCORD = 200
X_CORD = 300

#7 lanes
FIRST_POSTIONS = [(FIRST_XCORD,-215), (FIRST_XCORD,-145), (FIRST_XCORD,-75),
                  (FIRST_XCORD,-5), (FIRST_XCORD,65), (FIRST_XCORD,135),
                  (FIRST_XCORD,205)]

STARTING_LANES = [(X_CORD,-215), (X_CORD,-145), (X_CORD,-75),
                  (X_CORD,-5), (X_CORD,65), (X_CORD,135),
                  (X_CORD,205)]

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
            first_lane = random.choice(FIRST_POSTIONS)
            car.goto(first_lane) #spawn in lanes
            car2.goto(first_lane)
            speed_count += 1
        else:
            car.speed("fast")
            second_lane = random.choice(STARTING_LANES)
            car.goto(second_lane)
            car2.goto(second_lane)
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
