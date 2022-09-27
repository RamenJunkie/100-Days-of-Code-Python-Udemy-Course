from turtle import Turtle
from random import randint, choice

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.speed_x = 2
        self.speed_y = 2
        self.ball_start_dir()

    def ball_start_dir(self):
        flip = choice([0,1])
        if flip == 1:
            self.speed_y *= -1

    def move_ball(self):
        self.goto(self.xcor() + self.speed_x, self.ycor() + self.speed_y)

        if self.ycor() >= 230:
            self.bounce_down()
        #if self.xcor() >= 310:
        #    self.bounce_to_left()
        if self.ycor() <= -230:
            self.bounce_up()
        #if self.xcor() <= -310:
        #    self.bounce_to_right()


    def bounce_down(self):
        self.speed_y = -self.speed_y
    def bounce_up(self):
        self.speed_y = -self.speed_y
    def bounce_to_left(self):
        self.speed_x = -(self.speed_x+1)
    def bounce_to_right(self):
        self.speed_x = -(self.speed_x-1)

