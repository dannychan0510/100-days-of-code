# Import packages
from turtle import Turtle, Screen

# Create Turtle object
pointer = Turtle()

# Create Screen object
screen = Screen()


# Create functions
def move_forwards():
    pointer.forward(10)


def move_backwards():
    pointer.backward(10)


def turn_right():
    pointer.right(10)


def turn_left():
    pointer.left(10)


def reset():
    pointer.reset()


# Create listener functions
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset)

# Set screen to exit only on click
screen.exitonclick()
