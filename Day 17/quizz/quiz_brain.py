# from mimetypes import init


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.total_quest = len(self.question_list)
        self.score = 0

    def still_has_questions(self):
        return  self.question_number < self.total_quest

    def get_score(self):
        return f"{self.score}/{self.total_quest}"

    def next_question(self):
        print("\n" * 3)
        print(f"Q.{self.question_number + 1}")
        print(self.question_list[self.question_number].text, "(True/False)")

        answ = input("Your answer: ")

        self.check_answer(answ, self.question_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}")
        print(f"Actual scrore: {self.get_score()}")
    
