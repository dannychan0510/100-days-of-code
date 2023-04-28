from turtle import Turtle
import random

LOWER_BOUND = -280
UPPER_BOUND = 280
STEP = 20

# Define a class Food that inherits from Turtle
class Food(Turtle):
    # Initialize the Food object
    def __init__(self):
        # Call the parent class constructor
        super().__init__()
        # Set the shape of the Food object to a circle
        self.shape("circle")
        # Lift the pen up to prevent drawing lines while moving
        self.penup()
        # Set the size of the Food object using stretch_len and stretch_wid
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        # Set the color of the Food object to blue
        self.color("blue")
        # Set the animation speed of the Food object to fastest
        self.speed("fastest")
        # Call the refresh method to set the initial position
        self.refresh()

    # Method to move the Food object to a random position on the screen
    def refresh(self):
        # Generate random x and y coordinates that are divisible by 20
        random_x = random.randint(LOWER_BOUND // 20, UPPER_BOUND // 20) * 20
        random_y = random.randint(LOWER_BOUND // 20, UPPER_BOUND // 20) * 20

        # Move the Food object to the new random position
        self.goto(random_x, random_y)
