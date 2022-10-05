from turtle import Turtle

class namer(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor("black")
        self.hideturtle()

    def add_label(self, xcord, ycord, name):
        self.goto(xcord, ycord)
        self.write(name, font=("Courior",10, "bold"), align="center")