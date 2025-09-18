import turtle

import pandas
from turtle import Turtle,Screen

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


#turtle.mainloop()
states = pandas.read_csv("50_states.csv")
state_list = states.state.to_list()
correct = 0
states_guessed = []
state_guess = screen.textinput(title=f"{correct}/50 Guess a state",prompt="Enter a state name: ")
while state_guess != None:
    state_guess = state_guess.title()
    if state_guess in state_list:
        new_state = Turtle()
        new_state.hideturtle()
        new_state.penup()
        x_coord = int(states[states.state == state_guess].x.iloc[0])
        y_coord = int(states[states.state == state_guess].y.iloc[0])
        new_state.goto(x_coord,y_coord)
        new_state.write(state_guess)
        states_guessed.append(new_state)
        correct += 1
        state_list.remove(state_guess)
    state_guess = screen.textinput(title=f"{correct}/50 Guess a state", prompt="Enter a state name: ")
output = pandas.DataFrame(state_list)
output.to_csv("missed_states.csv")
