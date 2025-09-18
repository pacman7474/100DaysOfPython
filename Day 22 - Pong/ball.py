from turtle import Turtle
import random


STARTING_HEADING = [45,135,225,315]
INITIAL_SPEED = 20

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = INITIAL_SPEED
        self.speed_multiplier = .1
        self.shape("circle")
        self.penup()
        self.color("white")
        self.starting_heading()

    def starting_heading(self):
        rand_heading = random.choice(STARTING_HEADING)
        self.setheading(rand_heading)


    def move(self):
        self.forward(self.speed)
        self.check_wall()

    def reset(self):
        super().reset()
        self.speed_multiplier = .1
        self.shape("circle")
        self.penup()
        self.color("white")
        self.starting_heading()

    def check_wall(self):
        if self.distance((self.xcor(),300))<=20 or self.distance((self.xcor(),-300))<=20:
            self.setheading(self.heading()*-1)


    def check_score(self):
        if self.xcor() <= -380:
            self.reset()
            return "right"
        if self.xcor() >= 380:
            self.reset()
            return "left"
        return ""