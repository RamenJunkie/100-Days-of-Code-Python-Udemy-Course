from turtle import Turtle

SPEED = 30

class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(.5, 4)
        self.penup()
        self.goto(side, 0)

    def up(self):
        if (self.ycor() < 220):
            self.goto(self.xcor(), self.ycor()+SPEED)

    def down(self):
        if (self.ycor() > -200):
            self.goto(self.xcor(), self.ycor()-SPEED)
