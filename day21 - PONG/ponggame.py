from turtle import Screen
from player import Player
from computer import Computer
from pongscoreboard import Scoreboard
from ball import Ball
import time  #use this to control update

screen = Screen()
screen.setup(width=900, height=550)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)  #this allows for screen.update to run animations

player = Player()
computer = Computer()
score = Scoreboard()
ball = Ball()
#this allows for keypress
screen.listen()

#this allows for movement
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

player.player_start.setheading(270)
computer.computer_start.setheading(270)

start = True

while start:
    screen.update()
    time.sleep(.07)
    player.player_move()
    computer.computer_move()
    ball.ball_move()


    #this is score section

    if ball.ball_start.xcor() > 440:
        score.player_score +=1
        score.clear()
        score.player_score_number()
        score.computer_score_number()
        ball.ball_reset()
        ball.ball_angle()
        time.sleep(1)

    if ball.ball_start.xcor() < -440:
        score.computer_score +=1
        score.clear()
        score.computer_score_number()
        score.player_score_number()
        ball.ball_reset()
        ball.ball_angle()
        time.sleep(1)

    #this is bounce angle section
    if ball.ball_start.xcor() > 440 or ball.ball_start.xcor() < -440:
        ball.bounce_x()
        ball.ball_move()

    if ball.ball_start.ycor() > 265 or ball.ball_start.ycor() < -265:
        ball.bounce_y()
        ball.ball_move()

    #this is player and computer bounce section
    for segment in player.player_list:
        if ball.ball_start.distance(segment) < 10:
            ball.bounce_x()
            ball.bounce_y()
            ball.ball_move()

    for segment in computer.computer_list:
        if ball.ball_start.distance(segment) < 10:
            ball.bounce_x()
            ball.bounce_y()
            ball.ball_move()

screen.exitonclick()
