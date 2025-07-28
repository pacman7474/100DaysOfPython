from turtle import Screen
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



while game_running:
    snake.move()

    screen.onkey(key="a",fun=snake.left)
    screen.onkey(key="d",fun=snake.right)
    screen.onkey(key="e",fun=snake.eat)

    screen.listen()
    time.sleep(.1)
    screen.update()





screen.exitonclick()