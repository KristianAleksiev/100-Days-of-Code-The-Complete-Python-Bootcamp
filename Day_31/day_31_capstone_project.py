### Day 31 - Capstone project - Flash card program

import random
from tkinter import *
import pandas


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("words_to_learn.csv") #As a dataframe
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records") #=> The data becomes a list of dictionaries


def next_card():

    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back) ### N.B.-Not inside the function!


def is_known():

    to_learn.remove(current_card) # Removing the known card
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False) # So that it doesnt add the index
    next_card()

#Window
window = Tk()
window.title("Flash card learning")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

#Canvas
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 20, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


#Buttons
x_image = PhotoImage(file="right.png")
right_button = Button(image=x_image, command=next_card)
right_button.grid(row=1, column=0)

tick_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=tick_image, command=is_known)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()
