from turtle import Screen
from food import Food
from score import Scoreboard
import time
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake on a plane!")
screen.colormode(255)

screen.tracer(0)
snake = Snake()

screen.update()
game_running = True
item = Food()
scoreboard = Scoreboard()


while game_running:
    snake.move()

    screen.onkey(key="a",fun=snake.left)
    screen.onkey(key="d",fun=snake.right)

    screen.onkey(key="e",fun=snake.eat)
    if snake.head.distance(item) < 15:
        snake.eat()
        snake.head.color(item.pencolor())
        item.eaten()
        scoreboard.increase_score()


    screen.listen()
    time.sleep(.1)
    screen.update()
    if snake.head.xcor() > 275 or snake.head.xcor() < -275 or snake.head.ycor() > 275 or snake.head.ycor() < -275:

        scoreboard.reset()
        snake.reset()

    for seg in snake.body[2:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()
            break



screen.exitonclick()