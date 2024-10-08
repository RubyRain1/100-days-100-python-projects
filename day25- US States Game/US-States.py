import turtle
import pandas

game = True

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
author = turtle.Turtle()
author.hideturtle()
author.penup()
# allows us to access the states and location from csv
data = pandas.read_csv("50_states.csv")

score = 0
while game:
    if score == 0:
        # user input for game
        answer_state = screen.textinput("Guess a state", "enter a states name: ").lower().title()
        state_dict = data["state"].to_dict()
    else:
        answer_state = screen.textinput(f"{score}/50 States Guessed",
                                        "enter a states name: ").lower().title()
        state_dict = data["state"].to_dict()
    # isolate states row
    for i in state_dict:
        if state_dict[i] == answer_state:
            state_data = data[data.state == f"{answer_state}"]
            coordinates = (int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
            author.setpos(coordinates)
            author.write(f"{answer_state}")
            score += 1
        elif state_dict != answer_state:
            game = False

    game = True

    if score == 50:
        author.setpos(-250, 0)
        author.write("GAME OVER, YOU WIN", font=("", 40, "normal"))
        game = False

screen.exitonclick()
