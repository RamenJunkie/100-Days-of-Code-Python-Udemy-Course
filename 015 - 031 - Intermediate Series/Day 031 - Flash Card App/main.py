from tkinter import *
import pandas
from random import choice

LANGUAGE = "Norwegian"
INPUT_FILE = "data/norwegian_words.csv"
OUTPUT_FILE = "data/norwegian_words_known.csv"
TO_LEARN = "data/norwegian_words_to_learn.csv"
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courior"

try:
    with open(OUTPUT_FILE, mode="r") as test:
        pass
except FileNotFoundError:
    with open(OUTPUT_FILE, mode="a") as output:
        output.write(f"{LANGUAGE},English\n")

try:
    with open(TO_LEARN, mode="r") as test:
        pass
    input_data = TO_LEARN
except FileNotFoundError:
    input_data = INPUT_FILE

def wrong():
    pick_word()

def right():
    global word_dict
    known = pick_word()
    word_dict.remove(known[2])
    with open(OUTPUT_FILE, mode="a") as output:
        output.write(f"{known[1]},{known[0]}\n")
    to_learn_data = pandas.DataFrame(word_dict)
    to_learn_data.to_csv(TO_LEARN, index=False, header=True)

def flip(word):
    canvas.itemconfigure(canvas_word, text=word, fill = "white")
    canvas.itemconfigure(canvas_lang, text="English", fill = "white")
    canvas.itemconfigure(card_image, image = c_back)

def pick_word():
    global flip_timer
    window.after_cancel(flip_timer)
    ran_word = choice(word_dict)
    en_word = ran_word["English"]
    fr_word = ran_word[LANGUAGE]
    canvas.itemconfigure(card_image, image = c_front)
    canvas.itemconfigure(canvas_word, text=fr_word, fill = "black")
    canvas.itemconfigure(canvas_lang, text=LANGUAGE, fill = "black")

    if len(word_dict) > 0:
        flip_timer = window.after(3000, flip, en_word)
    return [en_word,fr_word, ran_word]


data = pandas.read_csv(input_data, delimiter=',')
word_dict = data.to_dict(orient="records")

window = Tk()
window.title("Flash Cards")
window.config(padx= 50, pady= 50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip, "English")

c_front = PhotoImage(file ="images/card_front.png")
c_back = PhotoImage(file ="images/card_back.png")
wrong_button = PhotoImage(file ="images/wrong.png")
right_button = PhotoImage(file ="images/right.png")

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image = c_front)
canvas_lang = canvas.create_text(400,150, text="", font=(FONT_NAME, 40, "italic"))
canvas_word = canvas.create_text(400,263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=1, row=1, columnspan=2)

button_wrong = Button(image=wrong_button, highlightthickness=0, command=wrong)
button_wrong.grid(column=1, row=2)
button_right = Button(image=right_button, highlightthickness=0, command=right)
button_right.grid(column=2, row=2)

pick_word()

window.mainloop()

