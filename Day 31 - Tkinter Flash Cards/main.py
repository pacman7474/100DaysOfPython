import random
import time

from pandas.core.interchange.dataframe_protocol import DataFrame

BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import json
import pandas
data_dict = {}

def change_word():
    global word,flip_id
    window.after_cancel(flip_id)
    canvas.itemconfig(canvas_image,image=card_image)
    word = random.choice(data_dict)
    canvas.itemconfig(card_word,text=word["French"],fill="Black")
    canvas.itemconfig(card_title,text="French",fill="Black")
    flip_id = window.after(3000, func=flip_card)

def flip_card():
    global word
    canvas.itemconfig(card_word,text=word["English"],fill="White")
    canvas.itemconfig(card_title,text="English",fill="White")
    canvas.itemconfig(canvas_image,image=back_card_image)


def check_button_press():
    global word
    data_dict.remove(word)
    to_learn = pandas.DataFrame(data_dict)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    change_word()


def x_button_press():
    change_word()



word = {}
window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR,padx=50,pady=50)
canvas = Canvas(width=800,height=600)
card_image = PhotoImage(file="./images/card_front.png")
back_card_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400,263,image=card_image)
canvas.grid(row=0,column=0,columnspan=2)
canvas.config(background=BACKGROUND_COLOR,borderwidth=0,highlightthickness=0)

card_title = canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"))

card_word = canvas.create_text(400,263,text="trouve", font=("Ariel",60,"bold"))

x_image = PhotoImage(file="./images/wrong.png")
check_image = PhotoImage(file="./images/right.png")
x_button = Button(image=x_image,highlightthickness=0,borderwidth=0,command=x_button_press)
x_button.grid(row=1,column=0)
check_button = Button(image=check_image,highlightthickness=0,borderwidth=0,command=check_button_press)
check_button.grid(row=1,column=1)

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    data_dict = data.to_dict(orient='records')

flip_id = window.after(3000,flip_card)
change_word()

window.mainloop()
