from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
#Window Title and Game Title
WIN_TITLE = "Quizler"
GAME_TITLE = "Quizler"
#Background Image
#BACKGROUND = ""
#Font type
FONT_NAME = "Courior"
WHITE = "white"
GREEN = "green"
CLOCK_COLOR = "white"
right_button_img = "images/true.png"
left_button_img = "images/false.png"

class QuizInterface():

    def __init__(self, quizbrain: QuizBrain):
        self.brain = quizbrain
        self.window = Tk()
        self.window.title(WIN_TITLE)
        self.window.config(padx= 10, pady= 10, bg=THEME_COLOR)
        self.window.geometry("400x520")

        self.header = Label(text=GAME_TITLE, font=(FONT_NAME, 20, "bold"), fg=WHITE, bg=THEME_COLOR, justify="center", padx= 10, pady= 10)
        self.header.grid(row= 1, column=1)
        self.score = Label(text="Score: 0", font=(FONT_NAME, 15, "bold"), fg=WHITE, bg=THEME_COLOR, justify="center")
        self.score.grid(row= 1, column=2)

        self.canvas = Canvas(height=290, width=340, bg=WHITE, highlightthickness=10)
        #self.bgimg = PhotoImage(file = BACKGROUND)
        #self.canvas.create_image(100 , 112, image = bgimg)
        self.canvas_text = self.canvas.create_text(160,160, text="", fill="black", font=(FONT_NAME, 20, "italic"), width=300)
        self.canvas.grid(row= 2, column= 1, columnspan=2, padx=10, pady=10)

        self.right_butt = PhotoImage(file = right_button_img)
        self.left_butt = PhotoImage(file = left_button_img)

        self.button_left = Button(image=self.left_butt, highlightthickness=0, text ="", command=self.button_left_action, justify='center')
        self.button_left.grid(row=4, column=1)
        #self.button_center = Button(text ="", command=self.button_center_action, justify='center')
        #self.button_center.grid(row=4, column=2
        self.button_right = Button(image=self.right_butt, highlightthickness=0, text ="", command=self.button_right_action, justify='center')
        self.button_right.grid(row=4, column=2)

        #self.bottom_gage = Label(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN)
        #self.bottom_gage.grid(row=5, column=2)

        self.set_question()


        self.window.mainloop()

    def button_left_action(self):
        #DEBUG print("False")
        self.scoreboard("False")

    def button_center_action(self):
        pass

    def button_right_action(self):
        #DEBUG print("True")
        self.scoreboard("True")


    def scoreboard(self, answer):
        result = self.brain.check_answer(answer)
        self.canvas.itemconfigure(self.canvas_text, text=result)
        #DEBUG self.brain.print_score()
        self.score["text"] = f"Score: {self.brain.score}"
        if self.brain.still_has_questions():
            self.window.after(1000, self.set_question)
        else:
            self.window.after(1000, self.end_board())

    def set_question(self):
        text = self.brain.next_question()
        self.canvas.itemconfigure(self.canvas_text, text=text)


    def end_board(self):
        self.canvas.itemconfigure(self.canvas_text, text=f"That's all the questions.\nYour final score is: {self.brain.score}/{self.brain.num_qs}")
        self.button_left.config(state="disabled")
        self.button_right.config(state="disabled")

