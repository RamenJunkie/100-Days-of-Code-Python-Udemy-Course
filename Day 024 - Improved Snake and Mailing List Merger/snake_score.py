from turtle import Turtle
from time import sleep

class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("snake_scores.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-50,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 270)
        self.write(f"Score: {self.score}  |  High Score: {self.high_score}", font=("Verdana",10,"bold"), align="center")

    def add_point(self):
        self.score +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over return of Ganon...", font=("Verdana",10,"bold"), align="center")
        sleep(3)
        if self.score > self.high_score:
            self.high_score = self.score
        with open("snake_scores.txt", mode = "w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()


