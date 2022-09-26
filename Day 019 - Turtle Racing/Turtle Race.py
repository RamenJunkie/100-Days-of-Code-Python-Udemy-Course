import turtle
from turtle import Turtle, Screen
from random import randint

def make_turtle(cur_turtle):
    cur_turtle = Turtle(shape="turtle")
    cur_turtle.color(each["color"])
    cur_turtle.penup()
    cur_turtle.goto(start_col, rows[each["start_row"]])
    cur_turtle.pendown()
    all_turtles.append(cur_turtle)
    writer.penup()
    writer.goto(start_col+30, rows[each["start_row"]])
    writer.write(each["name"].title())

def move_turtle(cur_turtle):
    cur_turtle.forward(randint(1,11))

rows = [125, 75, 25, -25, -75, -125]

turtles = [
    {"name": "leonardo", "color": "blue", "start_row": 0,},
    {"name": "donatello", "color": "purple", "start_row": 1,},
    {"name": "raphael", "color": "red", "start_row": 2,},
    {"name": "michaelangelo", "color": "orange", "start_row": 3,},
    {"name": "venus", "color": "aqua", "start_row": 4,},
    {"name": "slash", "color": "black", "start_row": 5,},
]

myscreen = Screen()
myscreen.setup(width=500, height=400)
turtle.title("Lets Win at the Turtle Races!")
start_col = -225
all_turtles = []
race_start = False
writer = Turtle()
writer.hideturtle()

for each in turtles:
    make_turtle(each["name"])

user_bet = myscreen.textinput(title = "Place your bets!", prompt="Which turtle will win the race? ").lower()

if user_bet:
    race_start = True

while(race_start):
    for each in all_turtles:
        move_turtle(each)
        if each.xcor() > -start_col:
            race_start = False
            winner = each.pencolor()

for each in turtles:
    if each["color"] == winner:
        winner_name = each["name"]

print(f"{winner_name.title()} is the winner of the race!")

if user_bet == winner_name:
    print("You bet correctly and win!")
else:
    print("Sorry, you lost.")


myscreen.exitonclick()
