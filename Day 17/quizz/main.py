from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_bank = list()
for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Thanks!")
print(f"Your final score was: {quiz.get_score()}")