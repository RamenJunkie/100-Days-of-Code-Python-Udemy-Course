import car
import the_turtle
import scoreboard
import graphics
from turtle import Screen
from time import sleep

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Crossey Turtle")
background = graphics.Background()
score = scoreboard.Scoreboard()
game_on = True
all_cars = []
counter = 0
car_speed = 5


player = the_turtle.TheTurtle()
screen.update()

screen.listen()
screen.onkey(fun = player.move,key = "space")

while game_on:
    screen.update()
    sleep(.05)


    if player.ycor() >= 200:
        player.goto(0,320)
        player.reset()
        car_speed += 1
        for each in all_cars:
            each.speed_up(car_speed)
        score.add_level()

    counter += 1

    if counter == 4:
        counter = 0
        all_cars.append(car.Car(car_speed))

    for each in all_cars:
        each.move_car()
        if each.ycor() == player.ycor() and player.distance(each) < 15:
            game_on = False

score.game_over()

screen.exitonclick()