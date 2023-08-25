from tkinter import Tk, Entry, Label, Button 

window = Tk()
window.geometry('800x300')
window.title('Input entry box with Button and Label')
window.iconbitmap('globe.ico')

def print_message():
    name = E.get()
    L1 = Label(window, text='Good morning, '+name+' !', font=('Arial',20))
    L1.grid(row=4, column=0, padx=10, pady=5, columnspan=2)

def exit_window():
    window.destroy()

L = Label(window, text='Enter you name:', font=('Arial',20))
L.grid(row=0, column=0, padx=10, pady=5)

E = Entry(font=('Arial',20))
E.grid(row=0, column=1, padx=10, pady=5)

B = Button(window, text='Print', command=print_message, font=('Arial',20))
B.grid(row=2, column=0, padx=10, pady=5)

B1 = Button(window, text='Exit', command=exit_window, font=('Arial',20))
B1.grid(row=2, column=1, padx=10, pady=5)

window.mainloop()
