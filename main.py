import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .25
SHORT_BREAK_MIN = .25
LONG_BREAK_MIN = .10
reps = 0
timer = None  # Value assigned in count_down func


# ---------------------------- TIMER RESET ------------------------------- #
# Reset check marks, text in timer, stop timer, and return to default text

def reset_timer():
    wn.after_cancel(timer)  # timer is what we want to cancel, so it must be in a variable.
    canvas.itemconfig(timer_text, text="00:00")
    sub_title.config(text="TOMATO TIMER")
    tally_mark.config(text=" ")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        sub_title.config(text="LONG BREAK", fg=RED)

    elif reps % 2 == 0:
        sub_title.config(text="BREAK TIME", fg=PINK)
        count_down(short_break_sec)
    else:
        sub_title.config(text="WORK")

        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # Dynamic typing is unique to python
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = wn.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_marks = " "
            work_sessions = math.floor(reps / 2)
            for _ in range(work_sessions):
                check_marks += "✓"
            tally_mark.config(text=check_marks)


# ---------------------------- BUTTON FUNCTIONS ------------------------------- #
# GUIs ARE EVENT DRIVEN
# Meaning GUIs need to keep listening to check if an event happened on screen
# GUIs listen through the "mainloop()". As it loops it checks if something happened. If yes, the GUI reacts to the event
# Issue is that it can only listen in mainloop not nested loops?

# "af" built in method overcomes this
# Takes the amount of time provided then calls the function
# *args allows you to put in an unlimited amount of positional arguments

# def say_something(a, b, c):
#     print(a)
#     print(b)
#     print(c)

# ---------------------------- UI SETUP ------------------------------- #
wn = tk.Tk()
wn.title("TOMATO TIMER")
wn.config(padx=100, pady=50, bg=YELLOW)
# wn.after(1000, say_something, 3, 5, 8)


sub_title = tk.Label(text="TOMATO TIMER", fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
sub_title.grid(column=1, row=0)

start_button = tk.Button(text="Start", width=5, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = tk.Button(text="Reset", width=5, command=reset_timer)
reset_button.grid(column=2, row=3)

tally_mark = tk.Label(font=(FONT_NAME, 13, "bold"), pady=10, bg=YELLOW, fg=GREEN, highlightthickness=0)
tally_mark.grid(column=1, row=3)

# Canvas widget allows you to put images on screen and allows you to layer things one on top of the other (i.e. z pos?)
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")  # Converts the image into a photo image
canvas.create_image(100, 112, image=tomato_img)  # x_pos, y_pos, photo image (above)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

wn.mainloop()
