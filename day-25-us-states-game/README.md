# Day 25: U.S. States Game

The U.S. States Game is a simple educational game that tests your knowledge of 
U.S. state names. The program displays a map of the United States with empty 
placeholders for the state names. The player's goal is to guess as many state 
names as possible. When a correct guess is made, the program displays the state 
name on the map. The game ends when the player has guessed all state names or 
decides to exit the game. The results, including the correctly guessed states 
and missed states, are saved to a file called `states_to_learn.csv`.

## Python Concepts Learned

This program demonstrates the following Python concepts:

1. **Working with CSVs using Pandas**: The program uses the 
   [Pandas library](https://pandas.pydata.org/) to load state data from a CSV 
   file, which includes state names and their x and y coordinates on the map. 
   Pandas is used to filter and access the data as needed during the game.

2. **Reading and Writing Files to Disk**: At the end of the game, the program 
   writes the results to a file called `states_to_learn.csv`. The file includes 
   the number of correctly guessed states, the list of correctly guessed states 
   in alphabetical order, the number of missed states, and the list of missed 
   states in alphabetical order.

3. **Using the Turtle Graphics library**: The program uses the 
   [Turtle graphics library](https://docs.python.org/3/library/turtle.html) to 
   display the map, create a turtle object to point to the state locations, and 
   write the state names on the map.

## How to Run the Program

1. Install Python 3.x if you haven't already.
2. Install the required libraries by running `pip install pandas turtle`.
3. Download the `blank_states_img.gif` and `50_states.csv` files and place them 
   in the same directory as the program.
4. Run the program with `python us_states_game.py` (or `python3 us_states_game.py` 
   on some systems).
5. Start guessing state names. Type "Exit" to end the game early.

---

Disclaimer: This README is generated with the help of ChatGPT-4.