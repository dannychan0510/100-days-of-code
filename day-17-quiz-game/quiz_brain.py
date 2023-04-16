# TODO: asking the question
# TODO: checking if the answer was correct
# TODO: checking if we are at the end of the quiz

class QuizBrain():

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list


    def still_has_questions(self):
        """
        Returns True if quiz still has questions in question_list to ask user
        """
        return len(self.question_list) > self.question_number


    def next_question(self):
        """
        Retrieves the next question from the question_list, increments the question_number by 1,
        shows the question to the user, and waits for the user's response.
        """
        # Retrieve the item at the current question_number from the question_list
        question = self.question_list[self.question_number]

        # Increment question number by 1
        self.question_number += 1

        # User the input() function to show the user the q text and ask for the user's answer
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")

        # Check answer
        self.check_answer(user_answer, question.answer)


    def check_answer(self, user_answer, correct_answer):
        """
        Checks if the user's answer is correct and updates the score.
        """
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That is wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
