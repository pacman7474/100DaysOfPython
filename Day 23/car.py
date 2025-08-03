from turtle import Turtle

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        boundary_x = []
        boundary_y = []

    def import_left_car(self):
        self.shape("car_left.gif")
    def import_right_car(self):
        self.shape("car_right.gif")
