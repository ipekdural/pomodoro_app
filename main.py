from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK="✔"
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    reps=0
    window.after_cancel(timer)
    label_timer.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    check_mark.config(text="")
    button_start.config(state="normal")
#add stop and reset button
# ---------------------------- TIMER MECHANISM ------------------------------- #
def button_start_clicked():
    button_start.config(state="disabled")
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps %2==1 or reps==1:
        label_timer.config(text="WORK TİME")
        count_down(work_sec)
    elif reps %8 ==0:
        label_timer.config(text="  BREAK  ",fg="#B0578D")
        print("hello1")
        count_down(long_break_sec)
        print("hello2")
    elif reps %2==0:
        label_timer.config(text="  BREAK  ",fg="#D988B9")
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    second = count % 60
    minute = (floor(count / 60))
    if minute<10 and second<10:
        canvas.itemconfig(timer_text, text=f"0{minute}:0{second}")
    elif minute < 10 :
        canvas.itemconfig(timer_text, text=f"0{minute}:{second}")
    elif second < 10 :
        canvas.itemconfig(timer_text, text=f"{minute}:0{second}")
    else:
        canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer=window.after(10, count_down, count - 1)
    else:
        if reps % 2 == 0:
            check_mark.config(text=f"{CHECK_MARK}" * int(reps / 2), bg=YELLOW, fg="GreeN",
                               font=(FONT_NAME, 10, "bold"))


        button_start_clicked()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.iconbitmap(default='favicon.ico')
window.title("Pomodoro \U0001F47B ")
window.config(padx=100, pady=100, bg=YELLOW)
# Canvas Widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 30, "bold"))  # fill keyword arg is for changing color of text
canvas.grid(column=1, row=1)

label_timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "normal"), bg=YELLOW)
label_timer.grid(column=1, row=0)

button_start = Button(text="Start", bg=GREEN, fg="white", font=(FONT_NAME, 11, "bold"), relief="groove", borderwidth=2,
                      highlightthickness=2, command=button_start_clicked)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", bg=RED, fg="white", font=(FONT_NAME, 11, "bold"), relief="groove", borderwidth=2,
                      highlightthickness=2,command=reset)
button_reset.grid(column=2, row=2)

check_mark=Label(text="")
check_mark.grid(column=1, row=3)


window.mainloop()
