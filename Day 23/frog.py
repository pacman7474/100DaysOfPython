from turtle import Turtle
import pygame

class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.color("purple")
        self.shape("turtle")
        self.shapesize(2.5, 2.5)
        self.goto(0, -100)
        self.rect = pygame.Rect(self.xcor()-10,self.ycor()+10,20,20)

    def move_up(self):
        self.forward(15)
        self.rect.center = (int(self.xcor()),int(self.ycor()))