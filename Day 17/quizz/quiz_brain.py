from mimetypes import init


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        print(f"Question {self.question_number}")
        print(self.question_list[self.question_number].text, "(True/False)")
        input("Your answer: ")
    
        self.question_number += 1