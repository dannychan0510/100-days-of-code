# Flashy - A Flashcard Application

Flashy is a simple flashcard application built with Python and the Tkinter library. It helps users learn French by showing them a French word and then the English translation after a short delay.

## Features

- Shows a random French word from a list.
- After 3 seconds, shows the English translation of the word.
- Allows users to mark words as "learned". Learned words are removed from the list and saved to a separate file.
- If all words are learned, displays a congratulatory message.

## How to Run

1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory and run `python main.py` in the terminal.

## Data Files

- `data/french_words.csv`: This file contains the initial list of French words and their English translations.
- `data/words_to_learn.csv`: This file is created by the application. It contains the words that the user has not yet learned.
- `data/learned_words.csv`: This file is created by the application. It contains the words that the user has marked as learned.

## Dependencies

- Python
- Tkinter
- Pandas

## Future Improvements

- Fix bug where program does not start if there are no more words to learn.

## License

This project is licensed under the terms of the MIT license.