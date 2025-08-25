from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✓"
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():
    global REPS
    REPS = 0
    window.after_cancel(timer)
    canvas.itemconfig(count_down_text,text="00:00")
    title_label.config(text="Timer")
    check_marks_label.config(text="")



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    REPS += 1
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    work_seconds = WORK_MIN * 60
    if REPS % 8 == 0:
        rep_min = LONG_BREAK_MIN
        title_label.config(text="Break",fg=RED)
        check = check_marks_label.cget("text") + CHECK_MARK
        check_marks_label.config(text=check)
    elif (REPS % 2) > 0:
        rep_min=WORK_MIN
        title_label.config(text="Work",fg=GREEN)
    else:
        rep_min = SHORT_BREAK_MIN
        title_label.config(text="Break",fg=PINK)
        check = check_marks_label.cget("text") + CHECK_MARK
        check_marks_label.config(text=check)
    count_down(rep_min*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    min = math.floor(count/60)
    sec = count % 60

    canvas.itemconfig(count_down_text,text=f"{min}:{sec:02d}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
canvas.grid(row=1,column=1)


count_down_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME,35, "bold"))
title_label = Label(text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
title_label.grid(row=0,column=1)

start_button = Button(text="Start",font=(FONT_NAME,12,"bold"),highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",font=(FONT_NAME,12,"bold"),highlightthickness=0,command=timer_reset)
reset_button.grid(row=2,column=2)

check_marks_label = Label(text="",fg=GREEN,bg=YELLOW,font=(FONT_NAME,12,"bold"))
check_marks_label.grid(row=3,column=1)



window.mainloop()