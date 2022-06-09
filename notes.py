import tkinter as tk
from tkinter import END, messagebox, FLAT, RAISED, GROOVE, RIDGE, SUNKEN


# COMMON WIDGETS:
#   Label(i.e. text on screen)
#   Button
#   Entry(i.e. single line input)
#   Text (i.e. multiple line input)
#   Spinbox (i.e. click up & down to change its value)
#   Scale (i.e .slider)
#   Checkbutton
#   Radiobutton
#   Listbox (i.e. choices you can pick from)

# Creates a component (i.e. widget).
# my_label.pack() # Pack method allow you to layout components you are building


# COMMAND FOR BUTTON
def button_clicked():
    print("I got clicked")
    new_text = cha.get()
    my_label.config(text=new_text)


# Window Setup
wn = tk.Tk()
wn.title("My first GUI Program")
wn.minsize(500, 300)
# HOW TO ADD PADDING AROUND ENTIRE WINDOW
wn.config(padx=50, pady=50)

# MAKE LABEL
my_label = tk.Label(text="Hello", font=("Arial", 24, "bold"))
# my_label.pack()  # Has a variety of diff parameters. See Documentation.
# HOW TO ADD PADDING AROUND SPECIFIC COMPONENT
my_label.config(padx=100, pady=100)

# Change the message in your component E.g of 2 different way below:
my_label["text"] = "Ningguang Main"
my_label.config(text="New Text")

# MAKE BUTTON
# "state" parameter determines whether a button is clickable. Default is clickable
# If state = DISABLED button is no longer clickable
# () calls the function, but for command parameter () is not needed. Just the name.
button = tk.Button(text="Click Me", command=button_clicked)
# button.pack()

# MAKE ENTRY
cha = tk.Entry(width=10)
# ha.pack()
print(cha.get())

# Tkinter Layout Managers which define how you position your components in your GUI
# 3 Main ones you should know about

# pack()
# always starts from the top
# you can change the side paratmeter
# but it hard to position components in particular pos w pack()

# place()
# provides x & y values to set pos
# requires precise co-ordinates
# similar tutrtle.setpos(x, y)

# grid()
# imagines your your entire program is a grid of any amount of rows and columns
# relative to other components
# easiest way to work with grid is starting with top left by stating column and row

## NOTE: You can only use ONE layout manager in a program (i.e. no mixing them), else error.
my_label.grid(column=0, row=0)
button.grid(column=1, row=1)
button_2 = tk.Button(text="2nd Button", command=button_clicked)
button_2.grid(column=2, row=0)
cha.grid(column=3, row=2)

# REMOVING A WIDGET
# You can use the methods:
# .destroy() or .grid_forget()


# OTHER USEFUL STYLIZATION DOCUMENTATION
# bd=1 creates a border of 1

# RELIEF
# styles widgets by providing certain 3D effects around the outside of the widget
# NOTE: you will need to import each of relief stylization you would like to use
# default is flat
# relief=SUNKEN creates the opposite effect of a button
# relief=RAISED creates a button like appearance
# e.g.
B1 = tk.Button(text="FLAT", relief=FLAT)
B2 = tk.Button(text="RAISED", relief=RAISED)
B3 = tk.Button(text="SUNKEN", relief=SUNKEN)
B4 = tk.Button(text="GROOVE", relief=GROOVE)
B5 = tk.Button(text="RIDGE", relief=RIDGE)

# STICKY
# follow N,S,E,W navigational sys
# sticky=W+E stretches the widget from W to E


# ANCHOR
# follow N,S,E,W navigational sys
# "anchors" widget in given direction

# FRAMES
# a box that has a border
# is another widget to help organize other widgets, acts likes a container in html/css
# frames can have a different layout than the widgets inside the frame  ????
# e.g.
frame = tk.LabelFrame(wn, text="This is my Frame", padx=50, pady=30)
frame.grid(padx=10, pady=10)

b1 = tk.Button(frame, text="Hello")
b2 = tk.Button(frame, text="Bye")
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)

# PADDING
# when you create the widget the padding in the parameter is for padding inside widget
# when you call teh widget  the padding in the parameter is for padding outside widget

wn.mainloop()
