import turtle

MOVE_DISTANCE = 20
COMPUTER_STARTING_POSITIONS = [(100, 0), (100, -20), (100, -40)]


class Computer:

    def __init__(self):
        self.computer_list = []
        self.createbody_computer()
        self.computer_start = self.computer_list[0]

    def createbody_computer(self):
        for start_computer_body in COMPUTER_STARTING_POSITIONS:
            self.add_body_computer(start_computer_body)

    def add_body_computer(self, start_computer_body):
        player = turtle.Turtle("square")
        player.color("white")
        player.penup()
        player.goto(420, 0)
        self.computer_list.append(player)

    def computer_move(self):
        for i in range(len(self.computer_list) - 1, 0, -1):
            next_x = self.computer_list[i - 1].xcor()
            next_y = self.computer_list[i - 1].ycor()
            self.computer_list[i].goto(next_x, next_y)
        self.computer_start.forward(MOVE_DISTANCE)

        if self.computer_start.ycor() < -275:
            self.computer_start.setheading(90)
        elif self.computer_start.ycor() > 275:
            self.computer_start.setheading(270)
