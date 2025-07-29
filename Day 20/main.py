from turtle import Screen
from food import Food
from score import Scoreboard
import time
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake on a plane!")

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
        item.eaten()
        scoreboard.update_score()


    screen.listen()
    time.sleep(.1)
    screen.update()





screen.exitonclick()