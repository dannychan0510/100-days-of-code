import tkinter as tk
import pandas as pd
import random
import csv

import pandas.errors

BACKGROUND_COLOR = "#B1DDC6"

# Read data
try:
    words = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    words = pd.read_csv('data/french_words.csv')

words = words.to_dict(orient='records')
current_card = {}


# ---------------------------- FUNCTIONS ------------------------------- #
# Get new random word
def next_card():
    global current_card, flip_timer

    # Cancel current timer
    window.after_cancel(flip_timer)

    # Change image to front card
    canvas.itemconfig(canvas_image, image=card_front_img)

    # Change title color
    canvas.itemconfig(card_title, text='French', fill='black')

    # If no more words:
    if len(words) != 0:
        # Get new word
        current_card = random.choice(words)
        canvas.itemconfig(card_word, text=current_card['French'], fill='black')

        # Change answer after 3 seconds
        flip_timer = window.after(3000, show_answer)
    else:
        canvas.itemconfig(card_word, text='You learned \nall the words!',
                          font=('Arial', 24, 'italic'), fill='black')


def correct_card():
    # Write remembered words into learned_words.csv
    with open('data/learned_words.csv', 'a', newline='', encoding='utf-8') as learned_words:
        # Specify the fieldnames based on the dictionary keys
        fieldnames = current_card.keys()

        # Create a DictWriter object with the fieldnames
        writer = csv.DictWriter(learned_words, fieldnames=fieldnames)

        # Append the dictionary to the CSV file as a single record
        writer.writerow(current_card)

    # Remove word from list
    words.remove(current_card)

    # Save words to words_to_learn.csv
    words_df = pd.DataFrame(words)
    words_df.to_csv('data/words_to_learn.csv', index=False)

    # Go to next card
    next_card()


# Show answer
def show_answer():
    # Change title
    canvas.itemconfig(card_title, text='English', fill='white')

    # Show answer
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')

    # Change image to back card
    canvas.itemconfig(canvas_image, image=card_back_img)


# ---------------------------- UI SETUP ------------------------------- #
# Initialise window
window = tk.Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, show_answer)

# Load images
card_front_img = tk.PhotoImage(file='images/card_front.png')
card_back_img = tk.PhotoImage(file='images/card_back.png')
wrong_img = tk.PhotoImage(file='images/wrong.png')
right_img = tk.PhotoImage(file='images/right.png')

# Create canvas
canvas = tk.Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=card_front_img)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Add text to canvas
card_title = canvas.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='Word', font=('Arial', 60, 'bold'))

# Add buttons
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, command=next_card)
right_button = tk.Button(image=right_img, highlightthickness=0, command=correct_card)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

# Initialise first card + mainloop
next_card()
window.mainloop()
