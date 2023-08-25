from tkinter import Tk, Checkbutton, IntVar, Button, Label

window = Tk()
window.title('Various OTT monthly budget')
window.geometry('600x600')
window.iconbitmap('globe.ico')

def checkprice():
    price=v1.get() + v2.get() + v3.get() + v4.get() + v5.get() + v6.get()

    c1.config(state='disabled')
    c2.config(state='disabled')
    c3.config(state='disabled')
    c4.config(state='disabled')
    c5.config(state='disabled')
    c6.config(state='disabled')
    B1.config(state='disabled')

    global L2
    
    L2 = Label(window, text='Total monthly subsciption = Rs. %d'%price, font=('Cambria',15))
    L2.grid(row=8, column=0, columnspan=3, padx=20, pady=10)

def new():
    c1.config(state='normal')
    c2.config(state='normal')
    c3.config(state='normal')
    c4.config(state='normal')
    c5.config(state='normal')
    c6.config(state='normal')
    B1.config(state='normal')
    L2.grid_remove()

def exit_win():
    window.destroy()
               
L1 = Label(window, text='Which OTT do you want to subscribe?', font=('Cambria',15))
L1.grid(row=0, column=0, columnspan=3, padx=20, pady=10)

v1 = IntVar()
c1 = Checkbutton(window, text='Hotstar', font=('Cambria',15), variable=v1, onvalue=75, offvalue=0)
c1.grid(row=1, column=0, padx=20, pady=10, sticky='W')

v2 = IntVar()
c2 = Checkbutton(window, text='SonyLiv', font=('Cambria',15), variable=v2, onvalue=83, offvalue=0)
c2.grid(row=2, column=0, padx=20, pady=10, sticky='W')

v3 = IntVar()
c3 = Checkbutton(window, text='Zee5', font=('Cambria',15), variable=v3, onvalue=58, offvalue=0)
c3.grid(row=3, column=0, padx=20, pady=10, sticky='W')

v4 = IntVar()
c4 = Checkbutton(window, text='Netflix', font=('Cambria',15), variable=v4, onvalue=149, offvalue=0)
c4.grid(row=4, column=0, padx=20, pady=10, sticky='W')

v5 = IntVar()
c5 = Checkbutton(window, text='Amazon Prime Videos', font=('Cambria',15), variable=v5, onvalue=125, offvalue=0)
c5.grid(row=5, column=0, padx=20, pady=10, sticky='W')

v6 = IntVar()
c6 = Checkbutton(window, text='ShemarooMe', font=('Cambria',15), variable=v6, onvalue=62, offvalue=0)
c6.grid(row=6, column=0, padx=20, pady=10, sticky='W')

B1 = Button(window, text='Check price', font=('Cambria',15), command = checkprice)
B1.grid(row=7, column=0, padx=20, pady=10)

B2 = Button(window, text='New', font=('Cambria',15), command = new)
B2.grid(row=7, column=1, padx=20, pady=10)

B3 = Button(window, text='Exit', font=('Cambria',15), command = exit_win)
B3.grid(row=7, column=2, padx=20, pady=10)

window.mainloop()
