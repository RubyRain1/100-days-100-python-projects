import turtle
import pandas
import csv

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
guessed_sates = []
remain = data["state"].to_dict()

score = 0
while game:
    if score == 0:
        # user input for game
        answer_state = screen.textinput("Guess a state", "enter a states name: ").title()
        state_dict = data["state"].to_dict()
    else:
        answer_state = screen.textinput(f"{score}/50 States Guessed",
                                        "enter a states name: ").title()
        state_dict = data["state"].to_dict()

    if answer_state == "Exit":
        states_remaining_data = pandas.DataFrame(remain.items(), columns=['Index', 'State'])
        states_remaining_data.to_csv("remaining_states.csv")
        break

    # isolate states row
    for i in state_dict:
        if state_dict[i] == answer_state:
            state_data = data[data.state == f"{answer_state}"]
            coordinates = (int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
            author.setpos(coordinates)
            author.write(f"{answer_state}")
            guessed_sates.append(answer_state)
            score += 1

    for i in guessed_sates:
        for key, state in list(remain.items()):  # Convert to list to safely modify
            if state == i:
                remain.pop(key)

        else:
            game = False


    print(remain)
    game = True

    if score == 50:
        author.setpos(-250, 0)
        author.write("GAME OVER, YOU WIN", font=("", 40, "normal"))
        game = False


