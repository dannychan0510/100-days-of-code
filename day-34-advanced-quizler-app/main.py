# Import modules
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Initialize an empty list for the question bank
question_bank = []

# Loop through the question data
for question in question_data:
    # Extract the question text and correct answer
    question_text = question["question"]
    question_answer = question["correct_answer"]
    
    # Create a new Question object with the extracted data
    new_question = Question(question_text, question_answer)
    
    # Add the new question to the question bank
    question_bank.append(new_question)

# Create a QuizBrain object with the question bank
quiz = QuizBrain(question_bank)

# Create a QuizInterface object with the QuizBrain object
quiz_ui = QuizInterface(quiz)
