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
reps = 0
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="BREAK", fg= RED, font=(FONT_NAME, 50))
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="BREAK", fg=PINK, font=(FONT_NAME, 50))
    else:
        countdown(work_sec)
        title_label.config(text="WORK", fg=GREEN, font=(FONT_NAME, 50))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000,countdown,count-1 )
    else:
        start_countdown()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Studying")
window.config(padx=100, pady=50, bg= YELLOW)

title_label = Label(text= "TIMER", fg = GREEN, bg = YELLOW, font= (FONT_NAME, 50))

start_button = Button(text= "Start", command=start_countdown)
reset_button = Button(text= "Reset")
check_label = Label(text= "✔", fg= GREEN, bg= YELLOW, font= (FONT_NAME, 20, "bold"))
canvas = Canvas(width=200, height=224, background= YELLOW, highlightthickness= 0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image = tomato_image)
timer_text = canvas.create_text(100,130, text="00:00", fill = "white",
                                font= (FONT_NAME, 35, "bold"))

title_label.grid(column = 1, row= 0)
canvas.grid(column = 1, row = 1)
start_button.grid(column = 0 , row = 2)
reset_button.grid(column = 2, row = 2)
check_label.grid(column = 1, row = 3)


window.mainloop()