# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're at the end of the quiz

class QuizBrain:

    def __init__(self, q_bank):
        self.question_number = 0
        self.question_list = q_bank

    def next_question(self):
        """Retrieve an item from current question_number from the question_list.
        Shows the user the Question text and ask for the user's answer."""
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        print(answer)

    def still_has_questions(self):
        """Return True if there are still questions to be asked, False otherwise."""
        return self.question_number < len(self.question_list)