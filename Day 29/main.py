from random import randint, choice, shuffle
import string
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    password_input.delete(0,END)
    special_chars_available = ['!','@','#','$','%','^','&']

    password_letters = [choice(string.ascii_letters) for _ in range(randint(8,10))]
    password_symbols = [randint(0,9) for _ in range(randint(2,4))]
    password_numbers = [choice(special_chars_available) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)
#    password_input.clipboard_clear()
#    password_input.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if len(website_input.get()) == 0:
        messagebox.showerror(title="Missing Website", message="Please enter a website name")
    elif len(password_input.get()) == 0:
        messagebox.showerror(title="Missing Password", message="Please enter a password")
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f"These are the details entered: \nEmail: {username_input.get()} "
                           f"\nPassword: {password_input.get()} \nIs it ok to save?")
        if is_ok:
            with open("data.txt","a") as file:
                file.write(website_input.get() + " | " + username_input.get() + " | " + password_input.get() + "\n")
            website_input.delete(0,END)
            password_input.delete(0,END)
            website_input.focus()

def handle_enter_key(event):
    save_password()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200)
my_pass_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=my_pass_image)

canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)


username_label = Label(text="Email/Username:")
username_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)


website_input = Entry(width=48)
website_input.grid(row=1,column=1,columnspan=2,stick='w')
website_input.focus()

username_input = Entry(width=48)
username_input.grid(row=2, column=1,columnspan=2,stick='w')
username_input.insert(END,"pac_man7474@yahoo.com")

password_input = Entry(width=28)
password_input.grid(row=3, column=1,stick='w')
password_input.bind("<Return>",handle_enter_key)

generate_button = Button(text="Generate Password",command=gen_password)
generate_button.grid(row=3,column=2,pady=0,stick='w')

add_button = Button(text="Add",width=44,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)




window.mainloop()
