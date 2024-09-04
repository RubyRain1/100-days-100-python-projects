import time
from turtle import Screen
from turtplayer import Player
from car_manager import CarManager
from turtscoreboard import Scoreboard
from lanes import Lanes

# GLOBALS
car_count = 0
spawn_rate = 6  #this is the delay between
frame_count = 0

# SCREEN LOGIC
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.tracer(0)
screen.listen()

# OBJECT CREATION
player = Player()
car = CarManager()
score = Scoreboard()
lane = Lanes()

screen.onkey(player.up, "Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if frame_count % spawn_rate == 0 and car_count <= 10000: #control spawn rate
        car.createcars()
        car_count += 1
    frame_count += 1

    if score.level <= 1: #car speed
        car.carmove()
    else:
        car.new_speed()

    if player.player_instance.ycor() == 200: #level increment
        score.level += 1
        score.clear()
        score.turt_score()
        time.sleep(1)
        player.reset()
    for car_instance in car.car_list:
        if player.player_instance.distance(car_instance) < 20:
            score.game_over()
            game_is_on = False
screen.exitonclick()
