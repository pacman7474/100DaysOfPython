from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=40,pady=40)

def convert():
    miles_input = float(input.get())
    km_answer = miles_input * 1.609
    answer.config(text=f"{km_answer}")

calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(row=2,column=1)

miles = Label(text="Miles")
miles.grid(row=0,column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1,column=0)

input = Entry(width=10)
input.grid(row=0, column=1)

answer = Label()
answer.grid(row=1,column=1)

km = Label(text="Km")
km.grid(row=1, column=2)

window.mainloop()