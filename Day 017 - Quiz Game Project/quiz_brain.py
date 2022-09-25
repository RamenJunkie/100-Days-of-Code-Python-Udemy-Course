class QuizBrain:

    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0
        self.num_qs = len(questions)

    def still_has_questions(self):
        return self.question_number < self.num_qs

    def next_question(self):
        self.current_q = self.question_list[self.question_number]
        self.question_number += 1
        self.answer = input(f"Q{self.question_number}: {self.current_q.text} (True/False): ").title()
        if(self.answer == "T"):
            self.answer = "True"
        if(self.answer == "F"):
            self.answer = "False"

        self.check_answer()
        self.print_score()

    def check_answer(self):
        if(self.answer == self.current_q.answer):
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
            #debug self.question_number = self.num_qs

    def print_score(self):
        print(f"Your score is: {self.score}/{self.question_number}.\n")