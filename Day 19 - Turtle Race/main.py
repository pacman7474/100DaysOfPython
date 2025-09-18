from turtle import Turtle, Screen
import random
colors = ["red","orange","yellow","green","blue","purple"]
starting_pos = [-75,-45,-15,15,45,75]
turtles = []
x_start = -240
y_start = -75

def setup_turtle(color,x,y,t):
    t.penup()
    t.color(color)
    t.goto(x,y)


def move_turtle(t,farthest):
    t.forward(random.randint(1,5))
    x_pos = t.xcor()
    if x_pos > farthest:
        farthest = x_pos
    return farthest

screen = Screen()
screen.setup(width=500,height=400)

for x in range(0,6):
    new_turtle = Turtle(shape="turtle")
    setup_turtle(colors[x],x_start,y_start + (x*30),new_turtle)
    turtles.append(new_turtle)




user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")



finish = 230
farthest = x_start
if user_bet:
    race_is_on = True

winner = ""
while race_is_on:
    for t in turtles:
        move_turtle(t,farthest)
        if t.xcor() >= 230:
            race_is_on = False
            winner = t.pencolor()

if user_bet == winner:
    print(f"Congrats your turtle {winner} has won!")
else:
    print(f"You lost. The winning turtle was {winner}.")

screen.exitonclick()