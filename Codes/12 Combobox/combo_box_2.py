from tkinter import Tk, Label, Button
from tkinter.ttk import Combobox

w = Tk()
w.title('Movie ticket price')
w.iconbitmap('globe.ico')
w.geometry('500x500')

def select():
    price = 0
    if my_combo_box_1.get() == 'Monday' or my_combo_box_1.get() == 'Tuesday' or my_combo_box_1.get() == 'Wednesday':
        price = price + 100
    if my_combo_box_1.get() == 'Thursday':
        price = price + 80
    if my_combo_box_1.get() == 'Friday' or my_combo_box_1.get() == 'Saturday':
        price = price + 125
    if my_combo_box_1.get() == 'Sunday':
        price = price + 150

    if my_combo_box_2.get() == 'Front 5 rows':
        price = price-20
    if my_combo_box_2.get() == 'Middle rows':
        price = price + 0
    if my_combo_box_2.get() == 'Last 2 rows':
        price = price + 20
    if my_combo_box_2.get() == 'Premium':
        price = price + 50

    L = Label(w, text='Price for one ticket would be Rs. %d'%price, font=('Times new roman',15))
    L.pack()
    
L1 = Label(w, text='Select a day you want to watch this movie:', font=('Times new roman',20))
L1.pack()
options1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
my_combo_box_1 = Combobox(w, value=options1)
my_combo_box_1.current(4)
my_combo_box_1.pack()

L2 = Label(w, text='Select a type of seat:', font=('Times new roman',20))
L2.pack()
options2 = ['Front 5 rows', 'Middle rows', 'Last 2 rows', 'Premium']
my_combo_box_2 = Combobox(w, value=options2)
my_combo_box_2.current(2)
my_combo_box_2.pack()

B = Button(w, text='Submit', font=('Times new roman',15), command = select)
B.pack()

w.mainloop()
