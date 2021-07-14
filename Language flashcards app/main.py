from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Arial', 40, 'italic')
WORD_FONT = ('Arial', 50, 'bold')

# ---------------------------- READING DATA ------------------------------- #
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')

data_list = data.to_dict(orient="records")
word = {}


def next_card():
    global word, timer
    window.after_cancel(timer)
    word = choice(data_list)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(language_label, text='French', fill='black')
    canvas.itemconfig(word_label, text=word['French'], fill='black')
    timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(language_label, text='English', fill='white')
    canvas.itemconfig(word_label, text=word['English'], fill='white')


def known_card():
    data_list.remove(word)
    dataframe = pandas.DataFrame(data_list, columns=['French', 'English'])
    dataframe.to_csv('data/words_to_learn.csv')
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.resizable(width=False, height=False)
timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')

# Canvas Image
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# Language text
language_label = canvas.create_text(400, 150, text='Title', fill='black', font=LANGUAGE_FONT)
word_label = canvas.create_text(400, 263, text='word', fill='black', font=WORD_FONT)

# Cross Button
cross_image = PhotoImage(file='images/wrong.png')
cross_button = Button(image=cross_image, bd=0, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)

# Tick Button
tick_image = PhotoImage(file='images/right.png')
tick_button = Button(image=tick_image, bd=0, highlightthickness=0, command=known_card)
tick_button.grid(column=1, row=1)

next_card()

window.mainloop()
