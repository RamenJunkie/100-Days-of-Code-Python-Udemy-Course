from turtle import Turtle

class Scores(Turtle):

    def __init__(self):
        super().__init__()
        self.score = [0,0]
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,180)
        self.write(f"{self.score[0]}    {self.score[1]}", font=("Courior", 25, "bold"), align="center")

    def add_point_p1(self):
        self.score[0] +=1
        self.clear()
        self.write(f"{self.score[0]}    {self.score[1]}", font=("Courior", 25, "bold"), align="center")

    def add_point_p2(self):
        self.score[1] +=1
        self.clear()
        self.write(f"{self.score[0]}    {self.score[1]}", font=("Courior", 25, "bold"), align="center")

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over return of Ganon...", font=("Courior", 25, "bold"), align="center")

