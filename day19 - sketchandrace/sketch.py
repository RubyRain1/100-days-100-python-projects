from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
screen = Screen()


def forward():
    timmy.forward(10)


def backwards():
    timmy.backward(10)


def counter_clockwise():
    timmy.left(10)


def clockwise():
    timmy.right(10)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=forward, key="w")
screen.onkey(fun=backwards, key="s")
screen.onkey(fun=clear, key="c")
screen.exitonclick()