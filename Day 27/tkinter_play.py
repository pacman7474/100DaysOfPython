import tkinter
#from tkinter import *  //imports all classes

window = tkinter.Tk()
window.title("My First Window")
window.minsize(width=500,height=300)
window.config(padx=100, pady=100)
window.geometry('500x300+1500+600')
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

#Label
my_label = tkinter.Label(text="I am a label",font=("Arial",24,"bold"))
#my_label.pack()
#my_label.place(x=100,y=200)
my_label.grid(row=0,column=0)
my_label.config(text="New Text")

def button_clicked():
    my_label.config(text="Button was clicked")
    input_string = input.get()
    print(input_string)

#button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(row=1,column=1)
#button.pack()

button2 = tkinter.Button(text="Button 2")
button2.grid(row=0,column=2)

#Entry class
input = tkinter.Entry(width=10)
input.grid(row=2,column=3)
#input.pack()


window.mainloop()