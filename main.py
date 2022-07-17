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
reps = 0
check = ''
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global check
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check = ''
    timer_title.config(text="Timer")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_title.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_title.config(text='Break', fg=PINK)
    else:
        countdown(work_sec)
        timer_title.config(text='WORK', fg=GREEN)

def start():
    if reps > 0:
        pass
    elif reps == 0:
        start_count()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global check
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f'0{count_min}'
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start()
        work_sessions = floor(reps/2)
        for _ in range(work_sessions):
            check += "✔"
        check_mark.config(text=f'{check}')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=60, bg=YELLOW)


canvas = Canvas(width=200, height=222, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 110, image=tomato_img)

timer_text = canvas.create_text(102, 135, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


timer_title = Label(text="Timer", font=(FONT_NAME, 50, 'bold'), fg=GREEN, bg=YELLOW)
timer_title.grid(column=1, row=0)

check_mark = Label(fg=GREEN, bg=YELLOW, font=10)
check_mark.grid(column=1, row=3)

start_button = Button(text='Start', font=(FONT_NAME, 8, 'normal'), bg='white', command=start)
start_button.grid(column=0, row=2)

end_button = Button(text='Reset', font=(FONT_NAME, 8, 'normal'), bg='white', command=reset)
end_button.grid(column=2, row=2)







window.mainloop()