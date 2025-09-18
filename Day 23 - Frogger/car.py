from turtle import Turtle
import pygame

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()


    def import_left_car(self):
        self.shape("car_left.gif")
    def import_right_car(self):
        self.shape("car_right.gif")

    def set_position(self):
        self.rect = pygame.Rect(self.xcor() - 62, self.ycor() + 30, 124, 60)

    def move_car(self,speed):
        self.forward(speed)
        self.rect.center = (int(self.xcor()),int(self.ycor()))
