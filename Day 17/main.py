from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for x in question_data:
    question_bank.append(Question(x["question"],x["correct_answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{len(quiz_brain.question_list)}")