# Import libraries
import pandas

# Reading the NATO phonetic alphabet data from a CSV file and storing it in a DataFrame
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

# Creating a dictionary comprehension to map each letter to its corresponding NATO phonetic code.
# The dictionary uses letters as keys and their corresponding NATO phonetic codes as values.
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


# Defining a function to convert user input into its equivalent NATO phonetic alphabet codes
def generate_phonetic():
    # Prompting the user to enter a word and converting the input to uppercase to match dictionary keys
    user_input = input("Enter a word: ").upper()

    # Attempting to map each letter of the user input to its NATO phonetic code
    try:
        # Using list comprehension to create a list of NATO phonetic codes corresponding to the user's input
        user_input_nato_alphabet = [nato_alphabet_dict[letter] for letter in user_input]
    except KeyError:
        # Handling the case where the user input contains characters not found in the NATO alphabet dictionary
        print('Sorry, only letters in the alphabet please.')
        # Recursively calling the function to prompt the user for another input
        generate_phonetic()
    else:
        # Displaying the NATO phonetic codes for the user's input
        print(user_input_nato_alphabet)


# Calling the function to start the program
generate_phonetic()
