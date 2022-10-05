from my_data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for each in question_data:
    question_bank.append(Question(each["question"], each["correct_answer"]))

#debug print(question_bank[0].answer)

brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()

print("That's all the questions.")
print(f"Your final score is: {brain.score}/{brain.num_qs}")
