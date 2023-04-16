from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Initialise empty question bank
question_bank = []

# Populate question_bank with questions from question_data
for q in question_data:
    question_bank.append(Question(q['text'], q['answer']))

# Create QuizBrain object
quiz = QuizBrain(question_bank)

# Continue quiz as long as quiz still has questions
while quiz.still_has_questions():
    quiz.next_question()

# Show final message and score once all questions are asked
print(f"You've completed the quiz!")
print(f"You're final score was: {quiz.score}/{quiz.question_number}")