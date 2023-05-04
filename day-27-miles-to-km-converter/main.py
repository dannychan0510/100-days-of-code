import tkinter as tk

# Create a new window and configure it
window = tk.Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

# Entry widget for user input
miles_entry = tk.Entry(width=10, justify="center")
miles_entry.grid(column=1, row=0, padx=10, pady=10)

# Label for miles
miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0, padx=10, pady=10)

# Label for "is equal to" text
equal_label = tk.Label(text="is equal to")
equal_label.grid(column=0, row=1, padx=10, pady=10)

# Label for the converted value
conversion_value = 0.00
converted_label = tk.Label(text=f"{conversion_value}")
converted_label.grid(column=1, row=1, padx=10, pady=10)

# Label for km
km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1, padx=10, pady=10)

# Function to perform the conversion
def calculate():
    conversion_value = round(float(miles_entry.get()) * 1.60934, 2)
    converted_label.config(text=f"{conversion_value}")

# Button to trigger the conversion
calculate_button = tk.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2, padx=10, pady=10)

# Start the main event loop to handle user interactions with the GUI
window.mainloop()
