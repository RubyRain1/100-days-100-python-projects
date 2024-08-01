
class Question:
    def __init__(self, text, answer):
        self.txt = text
        self.ans = answer


class QuizBrain:

    def __init__(self, listq):
        self.question_number = 0
        self.question_list = listq
        self.score = 0

    #cuts off after the number exceeds last question
    def still_has_question(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        retrieve_question = self.question_list[self.question_number]
        self.question_number += 1
        userI = input(f"Q.{self.question_number}: {retrieve_question.txt}? True/False: ")
        self.check_answer(userI, retrieve_question.ans)

    def check_answer(self,userA, correct_answer):
        if userA.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("That is the wrong answer")
        print(f"the correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")