from turtle import Turtle, Screen

def move_forward():
    raphael.forward(10)

def move_backward():
    raphael.forward(-10)

def turn_left():
    raphael.left(10)

def turn_right():
    raphael.right(10)

def clear():
    raphael.penup()
    raphael.home()
    raphael.clear()
    raphael.pendown()

raphael = Turtle()
raphael.speed("fastest")

myscreen = Screen()
myscreen.listen()
myscreen.onkey(fun = move_forward, key = "w")
myscreen.onkey(fun = turn_left, key = "a")
myscreen.onkey(fun = move_backward, key = "s")
myscreen.onkey(fun = turn_right, key = "d")
myscreen.onkey(fun = clear, key = "c")

myscreen.exitonclick()