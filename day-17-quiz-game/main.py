from question_model import Question
from data import question_data

# Initialise empty question bank
question_bank = []

# Populate question_bank with questions from question_data
for q in question_data:
    question_bank.append(Question(q['text'], q['answer']))

