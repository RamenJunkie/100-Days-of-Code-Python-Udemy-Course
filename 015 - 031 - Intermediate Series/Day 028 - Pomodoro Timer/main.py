from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
CLOCK_COLOR = GREEN
WINDOW_BG = YELLOW
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
BACKGROUND = "tomato.png"
timer = None

countdown = WORK_MIN
round = 0
check_text = ""
timer_text = "00:00"

#def timer_pause():
#    header.config(text = "PAUSED", fg = PINK)
#    window.after_idle()


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    header.config(text = "Pomodoro", fg = RED)
    window.after_cancel(timer)
    timer_text = "00:00"
    canvas.itemconfigure(canvas_text, text=timer_text)
    checks["text"] = ""

# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_start():
    header.config(text = "Work", fg = GREEN)
    round = 7
    #window.after(1000, counter, WORK_MIN*60, round)
    counter(WORK_MIN*60, round)

def timer_label(time):
    seconds = int(time%60)
    minutes = int((time-seconds)/60)
    timer_text = f"{'%02d' % minutes}:{'%02d' % seconds}"
    canvas.itemconfigure(canvas_text, text=timer_text)

def make_checks(num_checks):
    check_text = ""
    for n in range(0,int(num_checks)):
        check_text += "✔"
    return check_text


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(countdown, round):
    global timer
    countdown -= 1
    timer_label(countdown)
    if countdown <= 0:
        round -= 1
        if round == 0:
            header.config(text="Long Break", fg=RED)
            countdown = LONG_BREAK_MIN*60
        elif round < 0:
            round = timer_reset()
        elif round % 2 == 0:
            header.config(text="Break", fg=RED)
            countdown = SHORT_BREAK_MIN*60
        else:
            header.config(text="Work", fg=GREEN)
            check_text = make_checks(5-round/2)
            checks["text"] = check_text
            countdown = WORK_MIN*60

    if(round >= 0):
        timer = window.after(1000, counter, countdown, round)
    else:
        return


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx= 10, pady= 10, bg=WINDOW_BG)
bgimg = PhotoImage(file = BACKGROUND)
window.minsize(350, 350)
window.maxsize(350, 350)

header = Label(text="Pomodoro", font=(FONT_NAME, 20, "bold"), fg=RED, bg=WINDOW_BG, justify="center")
header.place(x=100,y=20)

canvas = Canvas(height=250, width=230, bg=WINDOW_BG, highlightthickness=0)
canvas.create_image(100 , 112, image = bgimg)
canvas_text = canvas.create_text(100,130, text=timer_text, fill=CLOCK_COLOR, font=(FONT_NAME, 40, "bold"))
canvas.place(x=60, y=60)

button_start = Button(text = "Start", command=timer_start, justify='center')
button_start.place(x=25, y=300)
#button_pause = Button(text = "Pause", command=timer_pause, justify='center')
#button_pause.place(x=135, y=300)
button_reset = Button(text = "Reset", command=timer_reset, justify='center')
button_reset.place(x=250, y=300)

checks = Label(text=check_text, font=(FONT_NAME, 15, "bold"), fg=GREEN)
checks.place(x=100, y=300)

window.mainloop()