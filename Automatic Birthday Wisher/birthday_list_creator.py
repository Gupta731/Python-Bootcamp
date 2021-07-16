from tkinter import *
from tkinter import messagebox
import csv

FONT = ("HP Simplified", 15, 'normal')
window = Tk()


# ---------------------------- SIZE LIMIT FUNCTIONS ------------------------------- #
def limit_day(*args):
    value = day_value.get()
    if len(value) > 2:
        day_value.set(value[:2])


day_value = StringVar()
day_value.trace('w', limit_day)


def limit_month(*args):
    value = month_value.get()
    if len(value) > 2:
        month_value.set(value[:2])


month_value = StringVar()
month_value.trace('w', limit_month)


def limit_year(*args):
    value = year_value.get()
    if len(value) > 4:
        year_value.set(value[:4])


year_value = StringVar()
year_value.trace('w', limit_year)


# ---------------------------- ADD BUTTON ------------------------------- #
def add_friend():
    name = (name_entry.get())
    email = email_entry.get()
    day = day_entry.get()
    month = month_entry.get()
    year = year_entry.get()
    if (name == '') or (email == '') or (day == '') or (month == '') or (year == ''):
        messagebox.showwarning(title='Invalid Data', message="Don't leave any fields empty")
    elif not day.isnumeric() or not month.isnumeric() or not year.isnumeric():
        messagebox.showwarning(title='Invalid Data', message="Please enter only numeric value in date fields")
    elif int(day) > 31 or int(month) > 12 or int(year) > 2025:
        messagebox.showwarning(title='Invalid Data', message="Please enter valid date")
    else:
        is_ok = messagebox.askokcancel(title="Birthday Details", message=f"Here are the details: \n"
                                                                         f"Name: {name}\n"
                                                                         f"Email: {email}\n"
                                                                         f"Date of Birth: {day}/{month}/{year}\n"
                                                                         f"Is it ok to save?")
        if is_ok:
            with open('birthdays.csv', 'a', newline='') as birthday_file:
                birthday = csv.writer(birthday_file, delimiter=',')
                birthday.writerow([name, email, year, month, day])
                reset()


# ---------------------------- RESET FUNCTION ------------------------------- #
def reset():
    """Resets all entry fields"""
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    day_entry.delete(0, END)
    month_entry.delete(0, END)
    year_entry.delete(0, END)
    name_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window.title('Add Birthday Details')
window.resizable(width=False, height=False)

# Canvas
canvas = Canvas(width=660, height=476, highlightthickness=0)
background_image = PhotoImage(file='cake.png')
canvas_image = canvas.create_image(330, 238, image=background_image)
canvas.grid(column=0, row=0)

# Labels
name_label = canvas.create_text(100, 100, text='Name: ', fill='black', font=FONT)
email_label = canvas.create_text(100, 150, text='Email: ', fill='black', font=FONT)
day_label = canvas.create_text(100, 200, text='Day: ', fill='black', font=FONT)
month_label = canvas.create_text(100, 250, text='Month: ', fill='black', font=FONT)
year_label = canvas.create_text(100, 300, text='Year: ', fill='black', font=FONT)

# Entries
name_entry = Entry(width=30, font=FONT, bg='LightGoldenrodYellow')
name_entry.focus()
name_entry.place(x=200, y=90)

email_entry = Entry(width=30, font=FONT, bg='LightGoldenrodYellow')
email_entry.place(x=200, y=135)

day_entry = Entry(width=15, font=FONT, bg='LightGoldenrodYellow', textvariable=day_value)
day_entry.place(x=200, y=185)

month_entry = Entry(width=15, font=FONT, bg='LightGoldenrodYellow', textvariable=month_value)
month_entry.place(x=200, y=235)

year_entry = Entry(width=15, font=FONT, bg='LightGoldenrodYellow', textvariable=year_value)
year_entry.place(x=200, y=285)

# Add Button
add_button = Button(text='ADD', font=FONT, width=32, bg='plum2', highlightthickness=0, activebackground='plum3',
                    command=add_friend)
add_button.place(x=200, y=350)

window.mainloop()
