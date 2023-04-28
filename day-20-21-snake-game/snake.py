from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Define a class Snake
class Snake:
    # Initialize the Snake object
    def __init__(self):
        self.segments = []            # Create an empty list for storing snake segments
        self.create_snake()           # Call the create_snake method to initialize the snake
        self.head = self.segments[0]  # Set the head of the snake as the first segment

    # Method to create the initial snake with segments
    def create_snake(self):
        for position in STARTING_POSITIONS:         # Iterate through the starting positions
            new_segment = Turtle(shape="square")    # Create a new Turtle object with square shape
            new_segment.color("white")              # Set the color of the segment to white
            new_segment.penup()                     # Lift the pen to prevent drawing
            new_segment.setposition(position)       # Set the position of the segment
            self.segments.append(new_segment)       # Add the segment to the segments list

    # Method to move the snake
    def move(self):
        # Iterate through the segments in reverse order, excluding the head
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the previous segment
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the previous segment
            self.segments[seg_num].goto(new_x, new_y)  # Move the current segment to the previous segment's position
        self.head.forward(MOVE_DISTANCE)               # Move the head of the snake forward by MOVE_DISTANCE

    # Method to change the snake's direction to up
    def up(self):
        if self.head.heading() != DOWN:  # Check if the snake is not heading down
            self.head.setheading(UP)     # Set the heading to up

    # Method to change the snake's direction to down
    def down(self):
        if self.head.heading() != UP:    # Check if the snake is not heading up
            self.head.setheading(DOWN)   # Set the heading to down

    # Method to change the snake's direction to left
    def left(self):
        if self.head.heading() != RIGHT:  # Check if the snake is not heading right
            self.head.setheading(LEFT)    # Set the heading to left

    # Method to change the snake's direction to right
    def right(self):
        if self.head.heading() != LEFT:   # Check if the snake is not heading left
            self.head.setheading(RIGHT)   # Set the heading to right
