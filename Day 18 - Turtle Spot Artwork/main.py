from turtle import Turtle, Screen
import random
import colorgram

direction = [0,90,180,270]

tim = Turtle()
screen = Screen()
screen.colormode(255)


colors = colorgram.extract("spot_color.jpg",20)

def pick_direction():
    tim.setheading(random.choice(direction))

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    return r,g,b


tim.shape("circle")
tim.pensize(1)
tim.speed(0)
tim.penup()
tim.hideturtle()
dot_size = 20
distance = dot_size + 30
dots = 10
offset = int((dots * distance)/2) * -1
for x in range(dots):
    for y in range(dots):
        tim.goto(y*distance + offset,x*distance + offset)
        color = random.choice(colors)
        while color.rgb[0] >= 240 and color.rgb[1] >= 240 and color.rgb[2] >= 240:
            color = random.choice(colors)
        tim.dot(dot_size,color.rgb)




screen.exitonclick()