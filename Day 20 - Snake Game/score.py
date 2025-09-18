from turtle import Turtle

FONT = ("Comic Sans MS",16,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.speed("fastest")
        self.goto(-280,270)
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align='center',font=FONT)



    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}  High Score: {self.high_score}", align='left', font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_scoreboard()