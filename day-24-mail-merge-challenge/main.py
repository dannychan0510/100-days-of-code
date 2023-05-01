# Open the file "Input/Letters/starting_letter.txt" in read mode.
# The variable `starting_letter` will contain the contents of the file as a list of lines.
with open("Input/Letters/starting_letter.txt", mode="r") as f:
    starting_letter = f.readlines()

# Open the file "Input/Names/invited_names.txt" in read mode.
# The variable `invited_names` will contain the contents of the file as a list of lines.
with open("Input/Names/invited_names.txt", mode="r") as f:
    invited_names = f.readlines()

# Iterate over the list of invited names.
for name in invited_names:

    # Remove the newline character from the end of the name.
    name = name.strip("\n")

    # Open a new file called "Output/ReadyToSend/letter_to_" + name + ".txt" in write mode.
    # The variable `f` will refer to the file object.
    with open(f"Output/ReadyToSend/letter_to_{name}.txt", mode="w") as f:

        # Iterate over the list of lines in the starting letter.
        for line in starting_letter:

            # Replace the placeholder "[name]" with the current name.
            new_line = line.replace("[name]", name)

            # Write the new line to the file.
            f.write(new_line)
