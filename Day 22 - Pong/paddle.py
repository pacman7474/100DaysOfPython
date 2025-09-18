from turtle import Turtle
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100

class Paddle(Turtle):
    def __init__(self,coord):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.turtlesize(stretch_wid=1,stretch_len=5)
        self.penup()
        self.color("white")
        self.goto(coord)

    def up(self):
        if self.distance((self.xcor(), 300)) > 50:
            self.forward(20)
        #prevent from going off screen (if hits the top)

    def down(self):
        #self.goto(self.xcor(),self.ycor()-20)
        if self.distance((self.xcor(),-300)) > 50:
            self.backward(20)
        #prevent from going off screen (if hits the bottom)
