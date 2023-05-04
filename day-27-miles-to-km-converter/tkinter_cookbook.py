import tkinter as tk

# Creating a new window and configurations
window = tk.Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Labels
label = tk.Label(text="This is new text")
label.pack()

# Buttons
def action():
    print("Do something")

button = t
button.pack()

# Entries
entry = tk.Entry(width=30)
entry.insert(tk.END, "Some text to begin with.")
print(entry.get())
entry.pack()

# Text
text = tk.Text(height=5, width=30)
text.insert(tk.END, "Example of multi-line text entry.")
print(text.get("1.0", tk.END))
text.pack()

# Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)

scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
def checkbutton_used():
    print(checked_state.get())

checked_state = tk.IntVar()
checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())

radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tk.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for index, item in enumerate(fruits):
    listbox.insert(index, item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
