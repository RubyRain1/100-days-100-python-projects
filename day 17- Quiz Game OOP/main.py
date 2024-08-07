from data import question_data

from Quiz import Question

from Quiz import QuizBrain


question_bank = []

data = question_data

for i in range(len(question_data)):
    qText = (data[i]['question'])
    qAns = (data[i]['correct_answer'])
    qNew = Question(qText, qAns)
    question_bank.append(qNew)

qNum = QuizBrain(question_bank)
is_true = qNum.still_has_question()

while is_true:
    qNum.next_question()

if not is_true:
    print("you have completed the quiz")
    print(f"Your total score was {qNum.score}/{qNum.question_number}")
