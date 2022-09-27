from turtle import Turtle

class Net:

    def __init__(self):
        self.score = Turtle()
        self.score.hideturtle()
        self.score.speed("fastest")
        self.score.shape("square")
        self.score.penup()
        self.score.goto(0,-235)
        self.score.pensize(5)
        self.score.pencolor("white")
        self.score.left(90)

        for i in range(1,15):
            self.score.pendown()
            self.score.forward(20)
            self.score.penup()
            self.score.forward(20)
