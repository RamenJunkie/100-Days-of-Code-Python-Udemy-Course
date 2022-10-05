from turtle import Turtle

class TheTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.reset()

    def move(self):
        self.forward(20)
#debug        print("moving")
        print(self.ycor())

    def reset(self):
        self.goto(0, -280)
