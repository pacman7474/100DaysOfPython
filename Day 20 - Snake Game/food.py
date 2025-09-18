from turtle import Turtle
import random

COLORS = ["red","blue","purple","yellow","green","white"]

class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("purple")
        self.penup()
        self.shapesize(0.5,0.5)

        x_coord = random.randint(-280,280)
        y_coord = random.randint(-280,280)
        self.goto(x_coord,y_coord)
        self.speed("fastest")

    def eaten(self):
        x_coord = random.randint(-280,280)
        y_coord = random.randint(-280,280)
        self.color(random.choice(COLORS))
        self.goto(x_coord,y_coord)

