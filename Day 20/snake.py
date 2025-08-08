from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_SEGMENTS = 3

class Snake:

    def __init__(self):
        self.create_snake()

    def create_snake(self):
        self.body = []
        for x in range(STARTING_SEGMENTS):
            new_seg = self.create_seg()
            new_seg.goto(x * -20 + x, 0)
            self.body.append(new_seg)
        self.head = self.body[0]
        self.tail = self.body[-1]

    def create_seg(self):
        seg = Turtle("square")
        seg.penup()
        seg.color("white")
        return seg

    def eat(self):
        new_seg = self.create_seg()
        new_seg.goto(self.tail.xcor(),self.tail.ycor())
        self.body.append(new_seg)
        self.tail = new_seg

    def move(self):
        for i in range(len(self.body)-1,0,-1):
            new_x = self.body[i -1].xcor()
            new_y = self.body[i -1].ycor()
            self.body[i].goto(new_x,new_y)
            self.body[i].color(self.body[i-1].pencolor())
        self.body[0].forward(MOVE_DISTANCE)

    def left(self):
        self.body[0].left(90)

    def right(self):
        self.body[0].right(90)

    def reset(self):
        for x in self.body:
            x.goto(1000,1000)
        self.body.clear()
        self.create_snake()




