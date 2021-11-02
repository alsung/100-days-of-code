from quiz_brain import QuizBrain
from question_model import Question
from data import question_data


question_bank = []
for question in question_data:
    q_object = Question(question["text"], question["answer"])
    question_bank.append(q_object)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

