import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # Cancel the current timer
    window.after_cancel(timer)
    # Reset the title and timer display
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    # Clear tick marks
    tick_label.config(text="")
    # Reset the number of repetitions
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    # Convert minutes to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Increment the repetition counter
    reps += 1

    # Determine the type of interval based on the repetition count
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # Convert seconds to minutes and seconds, adding leading zeros if needed
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    count_text = f"{count_min}:{count_sec}"

    # Update the timer display
    canvas.itemconfig(timer_text, text=count_text)
    if count > 0:
        # Continue counting down
        global timer
        timer = window.after(1, count_down, count - 1)
    else:
        # Start the next interval and update tick marks
        start_timer()
        checks = math.floor(reps/2) * "✓"
        tick_label.config(text=checks)

# ---------------------------- UI SETUP ------------------------------- #
# Initialise window
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title label
title_label = tk.Label(text="Timer")
title_label.config(font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# Pomodoro timer display
canvas = tk.Canvas(width=400, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(200, 112, image=tomato_img)
timer_text = canvas.create_text(200, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start and Reset buttons
start_button = tk.Button(text="Start", command=start_timer)
start_button.config(highlightbackground=YELLOW)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", command=reset_timer)
reset_button.config(highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)

# Tick counter
tick_label = tk.Label()
tick_label.config(fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)

# Initialise mainloop()
window.mainloop()
