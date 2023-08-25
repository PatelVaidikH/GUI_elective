from tkinter import Tk, Label, Button
from tkcalendar import Calendar

## To install it, type "pip install tkcalendar in CMD / Andaconda Prompt"
## https://pypi.org/project/tkcalendar/#:~:text=tkcalendar%20is%20a%20python%20module,Calendar%20to%20select%20a%20date.

w = Tk()
w.geometry('500x500')
w.title('Date Picker')
w.iconbitmap('globe.ico')

def action():
    L2.config(text='Selected date is '+c.get_date())

L1 = Label(w, text='Select a date:', font=('Cambria',20))
L1.pack()

c = Calendar(w, selectmode="day", year=2023, month=4, day=4)
c.pack()

B1 = Button(w, text='Select', font=('Cambria',20), command = action)
B1.pack()

L2 = Label(w, text='')
L2.pack()

w.mainloop()
