
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False


    def next_question(self):
        q_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?")
        self.question_number += 1
        self.check_answer(q_answer)


    def check_answer(self, q_answer):
        o_answer = self.question_list[self.question_number-1].answer
        if q_answer.lower() == o_answer.lower():
            self.score += 1
            print("That's right.")
            print(f"Your score:{self.score}/{self.question_number}")
        else:
            print(f"That's wrong.\n The correct answer was:{self.question_list[self.question_number-1].answer}")
            print(f"Your score:{self.score}/{self.question_number}")




