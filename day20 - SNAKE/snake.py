import turtle as t
from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTION = [0, 90, 180, 270]
class Snake:
    def __init__(self):
        self.snake_list = []
        self.createbody()

    def createbody(self):
        for start_snake_body in STARTING_POSITIONS:
            snake = t.Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(start_snake_body)
            self.snake_list.append(snake)

    def move(self):
        for i in range(len(self.snake_list) - 1, 0, -1):
            next_x = self.snake_list[i - 1].xcor()
            next_y = self.snake_list[i - 1].ycor()
            self.snake_list[i].goto(next_x, next_y)
        self.snake_list[0].forward(MOVE_DISTANCE)

    def up(self):
        self.snake_list[0].setheading(90)

    def left(self):
        self.snake_list[0].setheading(180)

    def right(self):
        self.snake_list[0].setheading(DIRECTION[0])

    def down(self):
        self.snake_list[0].setheading(270)