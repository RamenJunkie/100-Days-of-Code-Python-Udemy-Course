from data import *
from question_model import Question
from quiz_brain import QuizBrain
import ui

## Add a Category and Difficulty Selector on launch and make those values adjustable

question_data = poll_api()
question_bank = []
for each in question_data:
    question_bank.append(Question(each["question"], each["correct_answer"]))

#debug print(question_bank[0].answer)

brain = QuizBrain(question_bank)
quizui = ui.QuizInterface(brain)

#while brain.still_has_questions():

quizui.set_question(next_quest)






