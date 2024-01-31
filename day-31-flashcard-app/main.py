import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# Read data
words = pd.read_csv('data/french_words.csv')
words = words.to_dict(orient='records')


# ---------------------------- FUNCTIONS ------------------------------- #
# Get new random word
def next_card():
    current_card = random.choice(words)
    french_word = current_card['French']
    english_word = current_card['English']
    canvas.itemconfig(card_word, text=french_word)


# ---------------------------- UI SETUP ------------------------------- #
# Initialise window
window = tk.Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Load images
card_front_img = tk.PhotoImage(file='images/card_front.png')
wrong_img = tk.PhotoImage(file='images/wrong.png')
right_img = tk.PhotoImage(file='images/right.png')

# Create canvas
canvas = tk.Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_front_img)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Add text to canvas
card_title = canvas.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='Word', font=('Arial', 60, 'bold'))

# Add buttons
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, command=next_card)
right_button = tk.Button(image=right_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

# Initialise first card, and start mainloop()
next_card()
window.mainloop()
