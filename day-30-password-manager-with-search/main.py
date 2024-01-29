import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Define character sets for the password
    letters = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
    numbers = [str(i) for i in range(10)]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Randomly select characters for the password
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine selected characters and shuffle the order
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Create the final password string
    password = "".join(password_list)

    # Insert the generated password into the password input field and copy it to the clipboard
    password_input.delete(0, tk.END)
    password_input.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    # Get values from input fields
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    entry = f"{website} | {username} | {password}\n"

    # Check if the website and password fields are not empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # Prompt the user to confirm the entered details
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                              f"Username: {username}\n"
                                                              f"Password: {password}\n"
                                                              f"Is it ok to save?")
        if is_ok:
            # Write the password entry to the data.txt file
            with open("data.txt", mode="a") as f:
                f.write(entry)

            # Clear the website and password input fields
            website_input.delete(0, tk.END)
            password_input.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
# Initialise window
window = tk.Tk()
window.title("Title Manager")
window.config(padx=50, pady=50)

# Create canvas
canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=2)

# Create Website input row
website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = tk.Entry(width=42)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

# Create Email/Username input row
username_label = tk.Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_input = tk.Entry(width=42)
username_input.insert(0, "@gmail.com")
username_input.grid(column=1, row=2, columnspan=2)

# Create Password input row
password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = tk.Entry(width=22)
password_input.grid(column=1, row=3)

generate_password_button = tk.Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(column=2, row=3)

# Create Add button row
add_button = tk.Button(text="Add", width=40, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

# Initialise mainloop()
window.mainloop()
