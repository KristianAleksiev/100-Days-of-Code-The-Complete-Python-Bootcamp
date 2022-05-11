### Day 27 - Graphical user interface with Tkinter and function arguments

import tkinter ## from tkinter import *


def button_click ():
    print("The button got clicked")
    label["text"] = input.get() #=> Changing the label text to be the input

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  #=> Adding more space between the visual elements

###Creating a label

label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
label["text"] = "New label text"
# label.place(x=50, y=50) # => pack(), grid(), place()
label.grid(column=0, row=0) #=> Starting from the item wanted in the top left
#label.config(text="My new text")

second_button = tkinter.Button(text="New button")
second_button.grid(column=3, row=0)


### Creating a button

button = tkinter.Button(text="Click me", command=button_click) #=> Calling a function name when clicked
button.grid(column=1, row=1)

### Entry component

input = tkinter.Entry(width= 10)
input.grid(column=4, row=1)




window.mainloop()

