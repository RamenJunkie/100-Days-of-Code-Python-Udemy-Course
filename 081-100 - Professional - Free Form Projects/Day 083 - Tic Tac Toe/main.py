import turtle
from turtle import *
from random import randint
from time import sleep

def reset_board():
    return [[False, False, False],
            [False, False, False],
            [False, False, False]]


coords = [[[-150,-220],[0,-220],[150,-220]],
          [[-150,-60],[0,-60],[150,-60]],
          [[-150,100],[0,100],[150,100]]]
played = reset_board()
turn = True
rounds = 0

screen = Screen()
screen.setup(width=600, height=600)

turt = Turtle()
turt.hideturtle()
turt.speed(500)


def draw_board(turt):
    turt.clear()
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
    turt.goto(-220,-275)
    turt.pendown()
    turt.write('RESTART', move=False, align='left', font = ('Arial', 20, 'normal'))
    turt.penup()
    turt.goto(-150,240)
    turt.pendown()
    turt.write('TIC * TAC * TOE', move=False, align='left', font = ('Arial', 30, 'normal'))
    turt.penup()

def restart_game():
    global played
    global turn
    global rounds
    played = reset_board()
    turn = True
    rounds = 0
    draw_board(turt)

def draw_circle(coords):
    turt.penup()
    turt.goto(coords[0],coords[1])
    turt.pendown()
    turt.circle(60,360)
    turt.penup()

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
    turt.penup()

def check_position(j,i):
    global turn
    global rounds
    if j > 120 and j < 180 and i < -250 and i > -275:
        quit()
    if j > -220 and j < -100 and i < -250 and i > -275:
        restart_game()

    if abs(i) < 225 and abs(j) <225:
        # print(f"{int((i+225)/150)},{int((j+225)/150)}")
        x_point = int((i+225)/150)
        y_point = int((j+225)/150)
        if not played[x_point][y_point]:
            if turn:
                draw_circle(coords[x_point][y_point])
                played[x_point][y_point] = "O"
            else:
                draw_exe(coords[x_point][y_point])
                played[x_point][y_point] = "X"
            turn = not turn
            rounds += 1
        mainscr()

def check_win(board):
    # check rows
    for each in board:
        if each.count("X") == 3 or each.count("O") == 3:
            return each[0]
    for i in range(0,3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return board[0][i]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    return False

draw_board(turt)

def mainscr():
    global rounds
    global turn
    winner = check_win(played)

    if winner:
        print(f"{winner} has won the game!")
        rounds = 20

    if rounds < 9:
        if turn:
            #print("Player Turn")
            turtle.onscreenclick(check_position)
        else:
            #print("Computer Turn")
            #turtle.onscreenclick(check_position)
            sleep(1)
            check_position(randint(-224,224),randint(-224,224))
    else:
        print("Game Over")


    turtle.mainloop()

mainscr()

screen.exitonclick()