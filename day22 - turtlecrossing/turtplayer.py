import turtle
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        super().__init__()
        self.player_list = []
        self.make_player()
        self.player_instance = self.player_list[0] #this is to reference the player in code

    def make_player(self): #this creates a player
        player_turtle = turtle.Turtle("turtle")
        player_turtle.penup()
        player_turtle.setheading(90)
        player_turtle.setpos(STARTING_POSITION)
        self.player_list.append(player_turtle) #appends player to list for reference in code

    def reset(self):
        self.player_instance.goto(STARTING_POSITION)
    def up(self): #causes the player to go up/forward in the program
        new_y = self.player_instance.ycor() + MOVE_DISTANCE
        self.player_instance.goto(self.player_instance.xcor(), new_y)

