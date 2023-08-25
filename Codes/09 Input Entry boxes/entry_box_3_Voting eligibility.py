from tkinter import Tk, Label, Button, Entry, Radiobutton, IntVar, W

window = Tk()
window.title('Check your eligbilty of voting:')
window.iconbitmap('globe.ico')
window.geometry('800x400')

def check_eligibilty():
    age = int(E.get())

    if age>=18 and v.get()==1:
        L2 = Label(window, text='You are eligible to vote.', font=('Cambria',25))
        L2.grid(row=5, column=0, sticky='W', columnspan=2)
    else:
        L3 = Label(window, text='You are not eligible to vote.', font=('Cambria',25))
        L3.grid(row=5, column=0, sticky='W', columnspan=2)

    B.config(state='disabled')
    R1.config(state='disabled')
    R2.config(state='disabled')
    E.config(state='disabled')
        
L = Label(window, text='1. What is your age?', font=('Cambria',25))
L.grid(row=0, column=0, sticky='W')

E = Entry(font=('Cambria',25))
E.grid(row=0, column=1, sticky='W')

L1 = Label(window, text='2. Do you have voter ID card?', font=('Cambria',25))
L1.grid(row=1, column=0, sticky='W', columnspan = 2)

v = IntVar()

R1 = Radiobutton(window, text='Yes', variable=v, value=1, font=('Cambria',25))
R1.grid(row=2, column=0)

R2 = Radiobutton(window, text='No', variable=v, value=2, font=('Cambria',25))
R2.grid(row=2, column=1)

B = Button(window, text='Check eligibilty', command = check_eligibilty, font=('Cambria',25))
B.grid(row=4, column=0, columnspan=2)

window.mainloop()
