import turtle as t
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTION = [0, 90, 180, 270]
UP = 90
DOWN = 270
LEFT = 0
RIGHT = 180


class Snake:
    def __init__(self):
        self.snake_list = []
        self.createbody()
        self.head = self.snake_list[0]

    def createbody(self):
        for start_snake_body in STARTING_POSITIONS:
            self.add_body(start_snake_body)


    def add_body(self, start_snake_body):
        snake = t.Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(start_snake_body)
        self.snake_list.append(snake)

    def reset(self):
        for i in self.snake_list:
            i.hideturtle()
        self.snake_list.clear()
        self.createbody()
        self.head = self.snake_list[0]

    def extend(self):
        self.add_body(self.snake_list[-1].position())
    def move(self):
        for i in range(len(self.snake_list) - 1, 0, -1):
            next_x = self.snake_list[i - 1].xcor()
            next_y = self.snake_list[i - 1].ycor()
            self.snake_list[i].goto(next_x, next_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


