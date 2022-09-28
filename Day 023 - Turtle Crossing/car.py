from turtle import Turtle
from random import randint, choice
START_X = 305
color_choices = ["red","blue","yellow","purple","gray","white"]

class Car(Turtle):

    def __init__(self, cur_speed):
        super().__init__()
        self.penup()
        self.goto(START_X,(randint(1,22)*20)-260)
        self.color(choice(color_choices))
        self.shape("square")
        self.shapesize(.95,1.5)
        self.setheading(180)
        self.speed_up(cur_speed)
        #debug print(f"car at: {self.ycor()}")

    def move_car(self):
        self.forward(self.speed)

    def speed_up(self, cur_speed):
        self.speed = cur_speed
