from tkinter import Tk, Label, Entry, Button, W, E

window = Tk()
window.geometry('800x500')
window.title('Temperature converter')
window.iconbitmap('temp.ico')

def c2f():
    C = float(E.get())
    F = C*(9/5)+32
    L3 = Label(window, text='%4.1f °C = %4.1f °F'%(C,F), font=('Calibiri',20))
    L3.grid(row=3, column=0, columnspan=2, padx=20, pady=20)
    E.config(state='disabled')
    B1.config(state='disabled')
    B2.config(state='disabled')

def f2c():
    F = float(E.get())
    C = (F-32)*(5/9)
    L4 = Label(window, text='%4.1f °F = %4.1f °C'%(F,C), font=('Calibri',20))
    L4.grid(row=3, column=0, columnspan=2, padx=20, pady=20)
    E.config(state='disabled')
    B1.config(state='disabled')
    B2.config(state='disabled')

L1 = Label(window, text='Temperature Converter Version 1.0', font=('Calibri',25,'bold'))
L1.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

L2 = Label(window, text='Enter temperature in °C or °F:', font=('Calibri',20))
L2.grid(row=1, column=0, padx=20, pady=20, sticky='W')

E = Entry(font=('Calibri',20), width=10)
E.grid(row=1, column=1, padx=20, pady=20, sticky='E')

B1 = Button(window, text='Celcius to Farhrenheit', font=('Calibri',20), command=c2f)
B1.grid(row=2, column=0, padx=20, pady=20)

B2 = Button(window, text='Farhrenheit to Celcius', font=('Calibri',20), command=f2c)
B2.grid(row=2, column=1, padx=20, pady=20)

window.mainloop()
