import pandas
import requests
from tkinter import *
import random

#response = requests.get(url="http://api.open-notify.org/iss-now.json")
#response.raise_for_status()

#data = response.json()

#longitude = data["iss_position"]["longitude"]
#latitude = data["iss_position"]["latitude"]

#iss_position = (longitude,latitude)
#print(iss_position)

def new_quote():
    response = requests.get(url="https://thequoteshub.com/api/")
    response.raise_for_status()

    quotes = response.json()
    quote_text = quotes['text']
    quote_author = quotes['author']
    canvas.itemconfig(text_id,text=f"{quote_text}\n -{quote_author}")

window = Tk()
window.title("Quote Machine")
window.config(pady=50)
canvas = Canvas(width=1000,height=400)
text_id = canvas.create_text(500,200,text="",width=600,font=("Ariel",15,"italic"))
canvas.grid(row=0,column=0)
new_quote()

quote_button = Button(text="New Quote",command=new_quote)
quote_button.grid(row=1,column=0)
scroll = Scrollbar(orient="vertical",command=canvas.yview)
scroll.grid(row=0,column=1,sticky='ns')

window.mainloop()