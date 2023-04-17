# Import packages
from turtle import Turtle, Screen
import random

# Create a turtle screen object
screen = Screen()
screen.setup(width=500, height=400)

# Get user input for turtle bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# List of colors and corresponding y-positions for turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# Create a list to store all turtle objects
all_turtles = []

# Set initial race status to False
is_race_on = False

# Create turtles and append them to the all_turtles list
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Check if user_bet is not empty, set is_race_on to True
if user_bet:
    is_race_on = True

# Start the turtle race
while is_race_on:
    for turtle in all_turtles:
        # Move each turtle forward by a random distance
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        # Check if any turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            # Check if the winning turtle color matches the user's bet and print result
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            # Exit the loop after determining the winner
            break

# Exit the turtle screen on click
screen.exitonclick()
