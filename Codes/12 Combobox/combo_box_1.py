from tkinter import Tk, Label, Button
from tkinter.ttk import Combobox

w = Tk()
w.title('Demonstrating combobox')
w.iconbitmap('globe.ico')
w.geometry('500x500')

def select():
    L1 = Label(w, text='You selected '+my_combo_box.get(), font=('Times new roman',15))
    L1.pack()

L = Label(w, text='Select any one option from below:', font=('Times new roman',20))
L.pack()

options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5']

my_combo_box = Combobox(w, value=options)
my_combo_box.current(3)
my_combo_box.pack()

B = Button(w, text='Submit', font=('Times new roman',15), command = select)
B.pack()

w.mainloop()
