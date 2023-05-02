# Day 26: NATO Phonetic Alphabet Converter

This simple program converts a user-provided word into its corresponding NATO 
phonetic alphabet representation. For example, if you enter the word "hello", 
the program will output `['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']`.

## 🐍 Python Concepts Learned

I learnt the following Python concepts through this project:

1. **List Comprehension**: I use list comprehension to efficiently create a list 
   of NATO phonetic codes for each letter in the user input.

2. **Dictionary Comprehension**: I create a dictionary with letters as keys and 
   their corresponding NATO phonetic codes as values using dictionary comprehension.

3. **Iterating over a Pandas DataFrame**: I iterate over the rows of a Pandas 
   DataFrame, which contains the NATO phonetic alphabet data, to create our dictionary.

## 🚀 How to Run the Program

1. Install Python 3.x if you haven't already.
2. Install the required library by running `pip install pandas`.
3. Download the `nato_phonetic_alphabet.csv` file and place it in the same 
   directory as the program.
4. Run the program with `python nato_phonetic_converter.py` (or 
   `python3 nato_phonetic_converter.py` on some systems).
5. Enter a word when prompted, and the program will output the NATO phonetic 
   alphabet representation of the word.

---

Disclaimer: This README is generated using ChatGPT-4.
