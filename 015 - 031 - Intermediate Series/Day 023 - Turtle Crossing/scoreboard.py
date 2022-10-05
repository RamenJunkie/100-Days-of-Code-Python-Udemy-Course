from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score = 1
        self.goto(-150,220)
        self.write(f"Turtle Crossing\nLevel: {self.score}", font=("Verdana",20,"bold"), align="center")

    def add_level(self):
        self.score +=1
        self.clear()
        self.write(f"Turtle Crossing\nLevel: {self.score}", font=("Verdana",20,"bold"), align="center")

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over return of Ganon...", font=("Verdana",10,"bold"), align="center")