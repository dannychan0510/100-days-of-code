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
        self.print_score()  # Call the print_score method to display the initial score

    # Method to display the current score on the screen
    def print_score(self, color="white"):
        self.pencolor(color)  # Set the text color to white
        self.write(f"Current score: {self.score}", align=ALIGNMENT, font=FONT)

    # Method to increase the score by 1
    def increase_score(self):
        self.score += 1  # Increment the score by 1
        self.clear()  # Clear the previous score display
        self.print_score()  # Call the print_score method to display the updated score

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
