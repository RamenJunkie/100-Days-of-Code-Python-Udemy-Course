import turtle
from turtle import *
from random import randint

def reset_board():
    return [[False, False, False],
            [False, False, False],
            [False, False, False]]


coords = [[[-150,-220],[0,-220],[150,-220]],
          [[-150,-60],[0,-60],[150,-60]],
          [[-150,100],[0,100],[150,100]]]
played = reset_board()
turn = True

screen = Screen()
screen.setup(width=600, height=600)

turt = Turtle()
turt.hideturtle()
turt.speed(500)


def draw_board(turt):
    turt.penup()
    turt.goto(75,225)
    turt.pendown()
    turt.goto(75,-225)
    turt.penup()
    turt.goto(-75,225)
    turt.pendown()
    turt.goto(-75,-225)
    turt.penup()
    turt.goto(225,75)
    turt.pendown()
    turt.goto(-225,75)
    turt.penup()
    turt.goto(225,-75)
    turt.pendown()
    turt.goto(-225,-75)
    turt.penup()
    turt.goto(120,-275)
    turt.pendown()
    turt.write('EXIT', move=False, align='left', font = ('Arial', 20, 'normal'))
    turt.penup()

def draw_circle(coords):
    turt.penup()
    turt.goto(coords[0],coords[1])
    turt.pendown()
    turt.circle(60,360)

def draw_exe(coords):
    turt.penup()
    turt.goto(coords[0]+50,coords[1])
    turt.pendown()
    turt.right(225)
    turt.forward(144)
    turt.penup()
    turt.goto(coords[0]-50,coords[1])
    turt.pendown()
    turt.right(90)
    turt.forward(144)
    turt.left(315)

def check_position(j,i):
    global turn
    if j > 120 and j < 180 and i < -250 and i > -275:
        quit()

    if abs(i) < 225 and abs(j) <225:
        # print(f"{int((i+225)/150)},{int((j+225)/150)}")
        x_point = int((i+225)/150)
        y_point = int((j+225)/150)
        if not played[x_point][y_point]:
            if turn:
                draw_circle(coords[x_point][y_point])
            else:
                draw_exe(coords[x_point][y_point])
            played[x_point][y_point] = True
            turn = not turn
    print(turn)


draw_board(turt)

def mainscr():

    if turn:
        print("Player Turn")
        turtle.onscreenclick(check_position)
    else:
        print("Computer Turn")
        #turtle.onscreenclick(check_position)
        check_position([randint(-224,224),randint(-224,224)])

    turtle.mainloop()

mainscr()

screen.exitonclick()