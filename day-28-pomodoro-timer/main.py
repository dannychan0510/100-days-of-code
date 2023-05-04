import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
# Initialise window
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title
title_label = tk.Label(text="Timer")
title_label.config(font=("Courier", 36), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# Pomodoro widget
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start and Reset buttons
start_button = tk.Button(text="Start")
start_button.config(highlightbackground=YELLOW)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset")
reset_button.config(highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)

# Tick counter
tick_label = tk.Label(text="✓")
tick_label.config(fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)

# Initialise mainloop()
window.mainloop()
