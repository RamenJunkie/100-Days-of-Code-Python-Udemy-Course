from turtle import Turtle, Screen
import time
import snake
import food
import score

def draw_border():
    border = Turtle()
    border.hideturtle()
    border.penup()
    border.speed("fastest")
    border.color("blue")
    border.pensize(20)
    border.goto(-300, -295)
    border.pendown()
    for edge in range(0, 4):
        border.forward(595)
        border.left(90)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer("0")

# Make a fresh Snake
snakey = snake.Snake()
food = food.Food()
score = score.Score()
screen.update()
snake_alive = True
draw_border()

screen.listen()
screen.onkey(fun=snakey.go_up, key="w")
screen.onkey(fun=snakey.go_left, key="a")
screen.onkey(fun=snakey.go_down, key="s")
screen.onkey(fun=snakey.go_right, key="d")

# Keep on moving forward
while(snake_alive):
    screen.update()
    time.sleep(.1)
    snakey.move()

    if snakey.head.distance(food) < 15:
        food.refresh()
        score.add_point()
        snakey.new_seg()

    if abs(snakey.head.xcor()) > 290 or abs(snakey.head.ycor()) > 290:
        snake_alive = False

    if snakey.eat_self():
        snake_alive = False


score.game_over()

#create and add Game Over




















screen.exitonclick()