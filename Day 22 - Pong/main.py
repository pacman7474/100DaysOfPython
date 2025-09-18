from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

TOP = 300
BOTTOM = -300


def up():
    user_paddle.forward(10)



def down():
    user_paddle.backward(10)


#Class Objects ( paddle (2), ball, line, score (2) )
screen = Screen()
screen.setup(width=800,height=TOP*2)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")
line = Turtle()
line.hideturtle()
line.pensize(3)
line.color("white")
line.penup()
line.speed("fastest")
line.setheading(270)
line.goto(0,TOP)
while line.ycor() > BOTTOM:
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)
user_paddle = Paddle((350,0))
user2_paddle = Paddle((-350,0))
ball = Ball()

screen.update()
score = Scoreboard()
screen.listen()
screen.onkeypress(key="Up",fun=user_paddle.up)
screen.onkeypress(key="Down",fun=user_paddle.down)
screen.onkeypress(key="s",fun=user2_paddle.down)
screen.onkeypress(key="w",fun=user2_paddle.up)
sleep_speed = .1
game_is_on = True
while game_is_on:
    ball.move()
    scored = ball.check_score()
    if scored == "left":
        score.l_score += 1
        score.update_score()
    elif scored == "right":
        score.r_score += 1
        score.update_score()

    if ball.distance(user_paddle) < 50 and ball.xcor() >=320 or ball.distance(user2_paddle) < 50 and ball.xcor() <= -320:
        ball.setheading(ball.heading()*-1+180)
        ball.speed_multiplier *= 0.9

    time.sleep(ball.speed_multiplier)
    screen.update()




screen.exitonclick()