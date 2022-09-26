import colorgram
from turtle import Turtle, Screen
from random import choice
turtle.colormode(255)

#Sample image, cover of CHVRCHES Every Open Eye Album
color_extracted = colorgram.extract("image.jpg", 20)
color_choices = []
for i in color_extracted:
    color_choices.append((i.rgb.r, i.rgb.g, i.rgb.b))

# debug print(color_choices)
#color_choices = [(193, 137, 150), (128, 74, 88), (22, 28, 47), (59, 32, 48), (219, 210, 206), (184, 161, 155), (17, 11, 11), (174, 101, 116), (217, 179, 189), (148, 152, 159), (94, 47, 60), (93, 104, 114), (227, 201, 206), (154, 159, 156), (122, 83, 78), (209, 183, 180), (203, 206, 202), (164, 109, 105), (81, 95, 91), (59, 60, 74)]


marker = Turtle()
marker.speed(100)
marker.penup()
marker.hideturtle()

for y_coord in range(1,10):
    for x_coord in range(0,10):
        marker.setpos(-300 + x_coord * 50,-280 + y_coord * 50)
        marker.pencolor(choice(color_choices))
        marker.dot(30)




screen = Screen()
screen.screensize(600, 600)
screen.exitonclick()