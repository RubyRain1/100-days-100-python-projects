from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

start_x = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
start = True
food.spawn()
score_board.score()
while start:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) < 15:
        food.spawn()
        score_board.count += 1
        score_board.clear()
        score_board.score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    #detecting tail collision.
    for i in snake.snake_list[1:]:
        if snake.head.distance(i) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()
