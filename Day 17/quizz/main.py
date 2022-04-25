from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_bank = list()
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

quiz = QuizBrain(question_bank)
quiz.next_question()