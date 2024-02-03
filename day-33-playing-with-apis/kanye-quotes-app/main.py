from tkinter import *
import requests

# Function to get a quote from the Kanye REST API and update the quote text on the canvas.
def get_quote():
    response = requests.get(url="http://api.kanye.rest").json()['quote']
    response.raise_for_status()
    quote = response.json()['quote']
    canvas.itemconfig(quote_text, text=quote)

# Create the main window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Create a canvas to display the background image and quote text
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, 
                                text="Kanye Quote Goes HERE", 
                                width=250, 
                                font=("Arial", 20, "bold"), 
                                fill="white")
canvas.grid(row=0, column=0)

# Create a button with Kanye's image to get a new quote
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# Get an initial quote when the app starts
get_quote()

# Start the main event loop
window.mainloop()