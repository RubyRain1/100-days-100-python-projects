import turtle as t
from turtle import Screen
from snake import Snake
import time

start_x = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.left,"a")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
start = True
while start:
    screen.update()
    time.sleep(0.05)
    snake.move()
