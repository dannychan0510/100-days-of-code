from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


# Define a class Scoreboard that inherits from Turtle
class Scoreboard(Turtle):
    # Initialize the Scoreboard object
    def __init__(self):
        super().__init__()  # Call the parent class constructor
        self.hideturtle()  # Hide the turtle cursor
        self.penup()  # Lift the pen to prevent drawing
        self.setposition(0, 270)  # Set the initial position of the scoreboard
        self.score = 0  # Initialize the score to 0

        # Read high score from data.txt
        with open("data.txt", "r") as file:
            self.highscore = int(file.read())

        # Call the print_score method to display the initial score
        self.print_score()

    # Method to display the current score on the screen
    def print_score(self, color="white"):
        self.pencolor(color)  # Set the text color to white
        self.clear()  # Clear the previous score display
        self.write(f"Current score: {self.score} High score: {self.highscore}", align=ALIGNMENT, font=FONT)

    # Method to increase the score by 1
    def increase_score(self):
        self.score += 1  # Increment the score by 1
        self.print_score()  # Call the print_score method to display the updated score

    def reset(self):
        if self.score > self.highscore:
            # Update highscore attribute
            self.highscore = self.score

            # Write high score to data.txt
            with open("data.txt", "w") as file:
                file.write(f"{self.highscore}")

        self.score = 0
        self.print_score()
