class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {current_question.question} (True/False)?:")
        self.check_answer(user_input, current_question.answer)

    def check_answer(self,input,correct):
        if input.lower() == correct.lower():
            self.score +=1
            print("You are correct!")
        else:
            print("You are incorrect.")
        print(f"The correct answer is: {correct}")
        print(f"Current score: {self.score}/{self.question_number}")
        print("\n")

