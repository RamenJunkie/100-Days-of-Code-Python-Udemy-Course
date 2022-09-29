#State Guessing Game - Guess the states and the show up on a map
# 2022.09.29

from turtle import Turtle, Screen
import state_namer
import pandas

BG_IMAGE = "blank_states_img.gif"
FILE = "50_states.csv"
GAMENAME = "US States Game"


screen = Screen()
screen.setup(height= 491, width = 725)
screen.bgpic(BG_IMAGE)
screen.title(GAMENAME)
guessed = []
gameon = True

pen = state_namer.namer()

data = pandas.read_csv(FILE)

while gameon:
    user_state = screen.textinput(title = GAMENAME, prompt="Enter the name of a state. ").title()

    if user_state not in guessed and user_state in data["state"].values:
        row_data = data[data.state == user_state]
        #debug print(row_data["state"])
        pen.add_label(xcord = int(row_data["x"]), ycord= int(row_data["y"]), name = user_state)
        #debug print("Yes!")
        guessed.append(user_state)
    #debug print(guessed)

    if len(guessed) >= 50:
        gameon = False

    if user_state == "Exit":
        missing_states = []
        for each in data["state"].values:
            if each not in guessed:
                missing_states.append(each)
        new_data = pandas.DataFrame(missing_states)

        new_data.to_csv("States_To_Learn.csv")

        gameon = False



screen.exitonclick()