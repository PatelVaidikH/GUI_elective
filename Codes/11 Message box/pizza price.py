from tkinter import Tk, Button, messagebox, Label, Entry
from numpy.random import randint

window = Tk()

window.title('Demonstating various message boxes')
window.geometry('400x400')
window.iconbitmap('cricket.ico')

def action1():
    messagebox.showinfo('Pizza base', 'Your pizza base contains pizza sauce and chees. Cost is Rs. 100. Select more toppings')
    price = 100
    m1 = messagebox.askyesno('Tomato','Do you want to add Tomatoes?')
    if m1 == True:
        price = price + 20
    m2 = messagebox.askyesno('Capcicum','Do you want to add Capcicum?')
    if m2 == True:
        price = price + 25
    m3 = messagebox.askyesno('Tomato','Do you want to add Corns?')
    if m3 == True:
        price = price + 30
    messagebox.showinfo('Final price', 'Text final price of your pizza is Rs. %d'%price)
L1 = Label(window, text='Select your pizza toppings.')
L1.pack()

B1 = Button(window, text='Check price', command = action1)
B1.pack()

window.mainloop()