from tkinter import Tk, Radiobutton, Label, Button, IntVar, W

my_win = Tk()
my_win.geometry('500x500')
my_win.title('A window with radiobuttons')
my_win.iconbitmap('globe.ico')

def showprice():
    if v.get() == 1:
        L1 = Label(my_win, text='The price of First Class ticket is Rs. 1000', font=('Calibri',15))
        L1.grid(row=6, column=0, padx=50, pady=10)
    if v.get() == 2:
        L2 = Label(my_win, text='The price of Second Class ticket is Rs. 800', font=('Calibri',15))
        L2.grid(row=6, column=0, padx=50, pady=10)
    if v.get() == 3:
        L3 = Label(my_win, text='The price of Chair Car ticket is Rs. 500', font=('Calibri',15))
        L3.grid(row=6, column=0, padx=50, pady=10)
    if v.get() == 4:
        L4 = Label(my_win, text='The price of Sleeper class is Rs. 200', font=('Calibri',15))
        L4.grid(row=6, column=0, padx=50, pady=10)

L = Label(my_win, text='Select the class of your train ticket', font=('Calibri',15))
L.grid(row=0, column=0, padx=50, pady=10)

v = IntVar()

R1 = Radiobutton(my_win, text='FC', value=1, variable=v, font=('Calibri',15))
R1.grid(row=1, column=0, sticky='W', padx=50, pady=10)

R2 = Radiobutton(my_win, text='SC', value=2, variable=v, font=('Calibri',15))
R2.grid(row=2, column=0, sticky='W', padx=50, pady=10)

R3 = Radiobutton(my_win, text='CC', value=3, variable=v, font=('Calibri',15))
R3.grid(row=3, column=0, sticky='W', padx=50, pady=10)

R4 = Radiobutton(my_win, text='Sleeper', value=4, variable=v, font=('Calibri',15))
R4.grid(row=4, column=0, sticky='W', padx=50, pady=10)

B = Button(my_win, text='Show price', command=showprice, font=('Calibri',15))
B.grid(row=5, column=0, padx=50, pady=10)

my_win.mainloop()

