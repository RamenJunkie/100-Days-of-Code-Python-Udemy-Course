#Just the spirograph fromt he Turtle Practice

import turtle
from turtle import Turtle, Screen
from random import randint, choice

def color_picker():
    return (randint(1,255),randint(1,255),randint(1,255))

turtle.colormode(255)

raphael = Turtle()
raphael.hideturtle()

def spirals(spiral_steps):
    raphael.speed(500)
    for spirals in range(0,spiral_steps):
        raphael.pencolor(color_picker())
        raphael.circle(100,360)
        raphael.right(360/spiral_steps)


spirals(60)

screen = Screen()
screen.exitonclick()
