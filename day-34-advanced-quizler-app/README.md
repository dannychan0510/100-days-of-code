# Quiz Application

This is a simple quiz application built using Python. The application uses the Tkinter library for the graphical user interface and a custom `QuizBrain` class for the quiz logic.

## Files

- `ui.py`: This file contains the `QuizInterface` class which is responsible for creating the graphical user interface for the quiz application. It uses the Tkinter library to create a window, buttons, labels, and a canvas to display the questions.

- `quiz_brain.py`: This file contains the `QuizBrain` class which handles the quiz logic such as keeping track of the score, the current question, and checking if the user's answer is correct.

## How it Works

When the application is launched, it creates an instance of the `QuizInterface` class, passing in an instance of the `QuizBrain` class. The `QuizInterface` class sets up the window, score label, question canvas, and true/false buttons. It then calls the `get_next_question` method to display the first question.

The `get_next_question` method checks if there are still questions left in the quiz. If there are, it updates the score label, gets the next question from the `QuizBrain` instance, and updates the question text on the canvas. If there are no more questions, it displays a message that the quiz is finished and disables the buttons.

The `true_pressed` and `false_selected` methods are called when the true and false buttons are pressed, respectively. They check if the user's answer is correct and give feedback by changing the background color of the canvas to green (for correct answers) or red (for incorrect answers).

The `give_feedback` method is responsible for changing the background color of the canvas and resetting the question text color. It then waits for 1 second before getting the next question.

## Requirements

- Python 3
- Tkinter library (usually comes pre-installed with Python)

## Usage

To run the application, navigate to the directory containing the files and run the `ui.py` script:

```bash
python ui.py
```

Enjoy the quiz!