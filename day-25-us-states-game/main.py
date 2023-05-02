import turtle
import pandas

# Set up the turtle screen with a title and background image
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create a turtle to point to and write the state names
pointer = turtle.Turtle()
pointer.penup()
pointer.hideturtle()

# Load state data from the CSV file
data = pandas.read_csv("50_states.csv")

# Initialise empty list to store correct answers
correct_answers = []

# Main game loop
while len(correct_answers) < len(data["state"]):
    # Prompt the user to input a state name, and convert to title case
    answer_state = screen.textinput(title=f"{len(correct_answers)} / {len(data['state'])} correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    # Check if the input state name is in the dataset
    if answer_state in data["state"].values:
        # Get the state name and its x and y coordinates
        state_name = str(data[data["state"] == answer_state]["state"].iloc[0])
        state_xcor = int(data[data["state"] == answer_state]["x"].iloc[0])
        state_ycor = int(data[data["state"] == answer_state]["y"].iloc[0])

        # Move the pointer to the state's location and write the state name
        pointer.goto(state_xcor, state_ycor)
        pointer.write(state_name, align="center")

        # Add answer to correct_answers list
        correct_answers.append(state_name)

# Open a new file to store results
with open("states_to_learn.csv", mode="w") as f:
    # Write correctly guessed states to the file
    f.write(f"Correctly guessed states: {len(correct_answers)} / {len(data['state'])}\n")
    for state in sorted(correct_answers):
        f.write(f"{state}\n")

    # Write missed states to the file
    f.write(f"\n")
    f.write(f"Missed states: {len(data['state']) - len(correct_answers)} / {len(data['state'])}\n")

    for state in data["state"].to_list():
        if state not in sorted(correct_answers):
            f.write(f"{state}\n")
