from turtle import Turtle, Screen
import net
import paddle
import ball
import scores
from time import sleep
LEFT = -300
RIGHT = 300

screen = Screen()
screen.setup(width=640, height=480)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

bouncer = ball.Ball()
game_on = True
score = scores.Scores()
the_net = net.Net()

left_p = paddle.Paddle(LEFT)
right_p = paddle.Paddle(RIGHT)

screen.listen()
screen.onkey(fun=left_p.up, key="w")
screen.onkey(fun=left_p.down, key="s")
screen.onkey(fun=right_p.up, key="8")
screen.onkey(fun=right_p.down, key="2")
#debug screen.onkey(fun=score.add_point_p1, key="z")
#debug screen.onkey(fun=score.add_point_p2, key="x")


while game_on:
    bouncer.move_ball()
    # Detect Paddle Collisions
    if bouncer.distance(left_p) < 40 and bouncer.xcor() <= -305:
        bouncer.bounce_to_right()
    if bouncer.distance(right_p) < 40 and bouncer.xcor() >= 305:
        bouncer.bounce_to_left()

    if bouncer.xcor() >= 320:
        score.add_point_p1()
        bouncer.home()
        bouncer.speed_x = -2

    if bouncer.xcor() <= -320:
        score.add_point_p2()
        bouncer.home()
        bouncer.speed_x = 2

    sleep(.005)
    screen.update()



score.game_over()
screen.exitonclick()













