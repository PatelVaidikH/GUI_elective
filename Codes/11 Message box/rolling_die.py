from tkinter import Tk, Button, messagebox, Label
from numpy.random import randint

w = Tk()
w.title('Rolling a die')
w.geometry('500x500')
w.iconbitmap('globe.ico')

def action():
    response = messagebox.askyesno('Rolling a die','Are you sure you want to roll a die?')

    if response == True:
        n = randint(1,7)
        L1 = Label(w, text='You got number %d'%n, font=('Arial',15))
    else:
        L1 = Label(w, text='You do not want to roll a die', font=('Arial',15))
    L1.pack()

L = Label(w, text='Rolling a die game', font=('Arial',25))
L.pack()

B = Button(w, text='Roll', font=('Arial',20), command = action)
B.pack()

w.mainloop()
