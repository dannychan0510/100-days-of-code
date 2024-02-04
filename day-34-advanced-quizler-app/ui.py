from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

# QuizInterface class
class QuizInterface:

    # Initialization method
    def __init__(self, quiz_brain: QuizBrain):

        # Set up quiz brain
        self.quiz = quiz_brain

        # Set up window
        self.window = Tk()
        self.window.title('Quizler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Load images
        false_img = PhotoImage(file='images/false.png')
        true_img = PhotoImage(file='images/true.png')

        # Set up score label
        self.score_label = Label(text='Score: 0', 
                                 fg='white', 
                                 bg=THEME_COLOR, 
                                 font=('Arial', 12, 'normal'))
        self.score_label.grid(row=0, column=1)

        # Set up canvas
        self.canvas = Canvas(self.window, width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='question text',
            fill=THEME_COLOR,
            font=('Arial', 14, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        # Set up buttons
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_selected)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        # Get the first question
        self.get_next_question()

        # Start the main loop
        self.window.mainloop()

    # Method to get the next question
    def get_next_question(self):
        # Reset canvas background color
        self.canvas.config(bg='white')
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)

        # Check if there are still questions left
        if self.quiz.still_has_questions():
            # Update score label
            self.score_label.config(text=f'Score: {self.quiz.score} / {self.quiz.question_number}')

            # Get next question text
            q_text = self.quiz.next_question()

            # Update question text on canvas
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # End of quiz, update question text on canvas
            self.canvas.itemconfig(self.question_text, text=f'You finished the quiz! You scored {self.quiz.score} out of 10')

            # Disable buttons
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    # Method to handle true button press
    def true_pressed(self):
        # Check if answer is correct
        is_correct = self.quiz.check_answer('True')

        # Give feedback
        self.give_feedback(is_correct)

    # Method to handle false button press
    def false_selected(self):
        # Check if answer is correct
        is_correct = self.quiz.check_answer('False')

        # Give feedback
        self.give_feedback(is_correct)

    # Method to give feedback
    def give_feedback(self, is_right):
        # Change canvas background color based on whether answer is correct
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        # Reset question text color
        self.canvas.itemconfig(self.question_text, fill='white')

        # Wait 1 second then get the next question
        self.window.after(1000, self.get_next_question)