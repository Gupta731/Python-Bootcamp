from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 18, 'italic')
LABEL_FONT = ('Arial', 14, 'normal')
timer = 0


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.resizable(width=False, height=False)

        self.question_no_label = Label(text=f'Question: {self.quiz.question_number+1}/{len(self.quiz.question_list)}',
                                       bg=THEME_COLOR, fg='white', font=LABEL_FONT)
        self.question_no_label.grid(row=0, column=0)

        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR, font=LABEL_FONT)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text='Question here', fill=THEME_COLOR, font=FONT,
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, bd=0, highlightthickness=0, command=self.response_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, bd=0, highlightthickness=0, command=self.response_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg='white')
        self.enable_buttons()
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_question():
            self.question_no_label.config(
                text=f'Question: {self.quiz.question_number + 1}/{len(self.quiz.question_list)}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of quiz.')
            self.disable_buttons()
            self.window.after(2000, self.window.destroy)

    def response_true(self):
        check = self.quiz.check_answer('True')
        self.give_feedback(check)

    def response_false(self):
        check = self.quiz.check_answer('False')
        self.give_feedback(check)

    def give_feedback(self, check):
        if check:
            self.canvas.configure(bg='lightgreen')
        else:
            self.canvas.configure(bg='firebrick')
        self.disable_buttons()
        self.window.after(1000, self.get_next_question)

    def disable_buttons(self):
        self.true_button.config(state='disabled')
        self.false_button.config(state='disabled')

    def enable_buttons(self):
        self.true_button.config(state='active')
        self.false_button.config(state='active')
