from turtle import Turtle
import random

LOWER_BOUND = -280
UPPER_BOUND = 280
STEP = 20


# Define a class Food that inherits from Turtle
class Food(Turtle):
    # Initialize the Food object
    def __init__(self, snake):
        super().__init__()  # Call the parent class constructor
        self.snake = snake
        self.shape("circle")  # Set the shape of the Food object to a circle
        self.penup()  # Lift the pen up to prevent drawing lines while moving
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)  # Set the size of the Food object
        self.color("blue")  # Set the color of the Food object to blue
        self.speed("fastest")  # Set the animation speed of the Food object to fastest
        self.refresh()  # Call the refresh method to set the initial position

    # Method to move the Food object to a random position on the screen
    def refresh(self):
        # Keep generating new positions until a valid one is found
        while True:
            # Generate random x and y coordinates that are divisible by 20
            random_x = random.randint(LOWER_BOUND // 20, UPPER_BOUND // 20) * 20
            random_y = random.randint(LOWER_BOUND // 20, UPPER_BOUND // 20) * 20
            # Move the Food object to the new random position
            self.goto(random_x, random_y)

            # Initialize a flag to check if the new position is inside the snake
            is_inside_snake = False
            # Iterate through the snake's segments
            for segment in self.snake.segments:
                # If the distance between the food and the segment is less than 20, the food is inside the snake
                if self.distance(segment) < 20:  # Consider a small threshold for better gameplay
                    is_inside_snake = True
                    break

            # If the new position is not inside the snake, break the loop and use this position
            if not is_inside_snake:
                break
