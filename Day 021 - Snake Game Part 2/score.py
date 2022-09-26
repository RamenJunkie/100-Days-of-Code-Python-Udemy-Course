from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-50,270)
        self.hideturtle()
        self.write(f"Score: {self.score}", font=("Verdana"), align="center")

    def add_point(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}", font=("Verdana"), align="center")

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over return of Ganon...", font=("Verdana"), align="center")
