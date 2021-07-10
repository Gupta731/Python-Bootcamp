import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.bell()
    start_button['state'] = 'active'
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer', fg=GREEN)
    checkmark.config(text='')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    window.bell()
    start_button['state'] = 'disabled'
    start_button["disabledforeground"] = start_button["foreground"]
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_label.config(text='Break', fg=RED)
        count_down(LONG_BREAK_MIN)
    elif reps % 2 == 0:
        timer_label.config(text='Break', fg=PINK)
        count_down(SHORT_BREAK_MIN)
    else:
        timer_label.config(text='Work', fg=GREEN)
        count_down(WORK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_text = checkmark.cget('text') + '✔'
            checkmark.config(text=check_text)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable(width=False, height=False)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column='1', row=1)

# Timer Label
timer_label = tkinter.Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
timer_label.grid(column=1, row=0)

# Start Button
start_button = tkinter.Button(text='Start', font=(FONT_NAME, 10, 'normal'), command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = tkinter.Button(text='Reset', font=(FONT_NAME, 10, 'normal'), command=reset_timer)
reset_button.grid(column=2, row=2)

# checkmark label
checkmark = tkinter.Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, 'normal'))
checkmark.grid(column=1, row=3)

# mainloop keeps the window open and makes the program event driven
window.mainloop()
