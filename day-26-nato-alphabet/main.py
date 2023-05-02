import pandas

# Read the NATO phonetic alphabet data from a CSV file
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary with letters as keys and their corresponding NATO phonetic codes as values
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

# Get user input, and convert to upper case
user_input = input("Enter a word: ").upper()

# Convert the user input into a list of NATO phonetic alphabet codes
user_input_nato_alphabet = [nThaato_alphabet_dict[letter] for letter in user_input]

# Print the NATO phonetic alphabet codes for the user input
print(user_input_nato_alphabet)
