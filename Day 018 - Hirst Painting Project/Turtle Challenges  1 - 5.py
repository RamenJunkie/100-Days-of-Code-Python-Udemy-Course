import turtle
from turtle import Turtle, Screen
from random import randint, choice

def color_picker():
    return (randint(1,255),randint(1,255),randint(1,255))

turtle.colormode(255)

raphael = Turtle()
raphael.shape("turtle")
raphael.color("red")

michaelangelo = Turtle()
michaelangelo.shape("turtle")
michaelangelo.color("orange")

leonardo = Turtle()
leonardo.shape("turtle")
leonardo.color("blue")

donatello = Turtle()
donatello.shape("turtle")
donatello.color("purple")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# Challenge 1, Draw a Square
for i in range(0,4):
    raphael.forward(100)
    raphael.right(90)

# Challenge 2, Draw a Dashed Line
michaelangelo.left(90)
for i in range (0,4):
    michaelangelo.forward(25)
    michaelangelo.penup()
    michaelangelo.forward(25)
    michaelangelo.pendown()

# Challenge 3, Drawing Different Shapes
leonardo.right(180)
for sides in range(3,11):
    leonardo.pencolor(choice(colours))
    for step in range(0,sides):
        leonardo.forward(100)
        leonardo.right(360/sides)


# Challenge 4, Generate a Random Walk
don = 0
donatello.pensize(5)
donatello.speed(50)
while(don < 50):
    donatello.left(randint(0, 4)*90)
    donatello.pencolor(color_picker())
    donatello.forward(20)
    don+=1

# Challenge 5, Spiralgraph
spiral_steps = 60
raphael.speed(500)
for spirals in range(0,spiral_steps):
    raphael.pencolor(color_picker())
    raphael.circle(100,360)
    raphael.right(360/spiral_steps)


screen = Screen()
screen.exitonclick()
