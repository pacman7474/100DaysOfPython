import time
from wsgiref.validate import check_input
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

from tkinter import *

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        #Score
        self.score = Label(text=f"Score: {self.quiz.score}",fg="White",font=("Ariel",13,"bold"),bg=THEME_COLOR)
        self.score.grid(row=0,column=1)

        #Question
        self.question = Canvas(width=300,height=250)
        self.question.config(background="white")
        self.question_text = self.question.create_text(150,
                                                       125,
                                                       text="Test Question",
                                                       width=280,
                                                       font=("Ariel",20,"italic"),
                                                       fill=THEME_COLOR)
        self.question.grid(row=1,column=0,columnspan=2,pady=50)

        #Green Check
        check_image = PhotoImage(file="images/true.png")
        self.check_button = Button(image=check_image,highlightthickness=0,borderwidth=0,command=self.check_true)
        self.check_button.grid(row=2,column=0)

        #Red X
        x_image = PhotoImage(file="images/false.png")
        self.x_button = Button(image=x_image, highlightthickness=0, borderwidth=0, command=self.check_false)
        self.x_button.grid(row=2, column=1)

        self.update_question()

        self.window.mainloop()

    def check_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def update_question(self):
        self.question.config(bg="White")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question.itemconfig(self.question_text,text=q_text)
        else:
            self.question.itemconfig(self.question_text,text="You've reached the end of the quiz")
            self.check_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def give_feedback(self,is_right):
        if is_right:
            self.question.config(bg="Green")
        else:
            self.question.config(bg="Red")
        self.score.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000,self.update_question)

