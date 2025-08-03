from turtle import Turtle, Screen
import time
from lane import Lane


num_lanes = 6
lanes = []

screen = Screen()
screen.setup(1200,1200)
screen.tracer(0)
screen.register_shape("car_left.gif")
screen.register_shape("car_right.gif")

screen.listen()

for x in range(num_lanes):
    new_lane = Lane()
    new_lane.set_position(x * 75)
    lanes.append(new_lane)

game_is_on = True

while game_is_on:
    time.sleep(.1)
    for i in lanes:
        i.move_lane()
    screen.update()


screen.exitonclick()