from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  # Call the parent class constructor
        self.hideturtle()  # Hide the turtle cursor
        self.penup()  # Lift the pen to prevent drawing
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setposition(-285, 265)  # Set the initial position of the scoreboard
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def level_up(self):
        self.level += 1