from turtle import Turtle, Screen
import time
import snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer("0")

# Make a fresh Snake
snakey = snake.Snake()
screen.update()

screen.listen()
screen.onkey(fun=snakey.go_up, key="w")
screen.onkey(fun=snakey.go_left, key="a")
screen.onkey(fun=snakey.go_down, key="s")
screen.onkey(fun=snakey.go_right, key="d")

# Keep on moving forward
while(True):
    screen.update()
    time.sleep(.1)
    snakey.move()



















screen.exitonclick()