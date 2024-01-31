import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ----------------------------- SEARCH PASSWORD --------------------------------- #
def search_password():
    # Get values from input fields
    website = website_input.get()

    # Search for website in data.json
    try:
        with open('data.json', 'r') as data_file:
            # Read old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message=f"No data file exists.")
    else:
        if website in data:
            username = data[website]['username']
            password = data[website]['password']
            messagebox.showinfo(title="Details found", message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops", message=f"There is no password saved for {website}")


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
    new_data = {
        website: {
            'username': username,
            'password': password
        }
    }

    # Check if the website and password fields are not empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            # Write the password entry to the data.json file
            with open('data.json', 'r') as data_file:
                # Read old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
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
canvas.grid(column=1, row=0)

# Create Website input row
website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e")  # Align labels to the right (east)

website_input = tk.Entry(width=21)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2, sticky="ew")  # Make Entry span two columns and fill space

# Create Email/Username input row
username_label = tk.Label(text="Email/Username:")
username_label.grid(column=0, row=2, sticky="e")

username_input = tk.Entry(width=35)
username_input.insert(0, "@gmail.com")
username_input.grid(column=1, row=2, columnspan=2, sticky="ew")

# Create Password input row
password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e")

password_input = tk.Entry(width=21)
password_input.grid(column=1, row=3, sticky="ew")

# Buttons
search_button = tk.Button(text="Search", width=15, command=search_password)
search_button.grid(column=2, row=1)

generate_password_button = tk.Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

# Initialise mainloop()
window.mainloop()