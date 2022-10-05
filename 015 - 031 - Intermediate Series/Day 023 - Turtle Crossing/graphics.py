from turtle import Turtle

class Background(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.speed("fastest")
        self.goto(300,-260)
        self.pendown()
        self.goto(-300,-260)
        self.penup()
        self.goto(300,200)
        self.pendown()
        self.goto(-300,200)
        self.penup()