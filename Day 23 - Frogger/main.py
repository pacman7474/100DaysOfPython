from turtle import Turtle, Screen
import time
from lane import Lane
from frog import Frog


num_lanes = 6
lanes = []
collision = False

screen = Screen()
screen.setup(1200,1200)
screen.tracer(0)
screen.register_shape("car_left.gif")
screen.register_shape("car_right.gif")

screen.listen()

def check_collision():
    for x in lanes:
        for i in x.cars:
            if my_frog.rect.colliderect(i.rect):
                return True
    return False

for x in range(num_lanes):
    new_lane = Lane()
    new_lane.set_position(x * 75)
    lanes.append(new_lane)

game_is_on = True
my_frog = Frog()


screen.onkeypress(fun=my_frog.move_up,key="w")

while game_is_on:
    time.sleep(.1)
    screen.update()
    for i in lanes:
        i.move_lane()
    if check_collision():
        game_is_on = False
        print("Turtle was run over")
    screen.update()


screen.exitonclick()