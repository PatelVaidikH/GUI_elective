from tkinter import *

W = Tk()
W.geometry('1000x600')
W.title('Temperature converter')
W.iconbitmap('icon.ico')

def interest():
    P = float(E1.get())
    R = float(E2.get())
    N = float(E3.get())
    SI = (P*R*N)/100
    L5 = Label(W, text='Interest = %2f'%SI, font=('Calibri',20))
    L5.grid(row=5, column=0, columnspan=2, padx=20, pady=20)
    E1.config(state='disabled')
    E2.config(state='disabled')
    E3.config(state='disabled')
    B1.config(state='disabled')
    
L1 = Label(W, text='Simple Interest Calculator', font=('Calibri',20,'bold'))
L1.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

L2 = Label(W, text='Enter amount invested:', font=('Calibri',20))
L2.grid(row=1, column=0, padx=20, pady=20)

E1 = Entry(font=('Calibri',20))
E1.grid(row=1, column=1)

L3 = Label(W, text='Enter rate of interest:', font=('Calibri',20))
L3.grid(row=2, column=0, padx=20, pady=20)

E2 = Entry(font=('Calibri',20))
E2.grid(row=2, column=1)

L4 = Label(W, text='Enter duration (in years):', font=('Calibri',20))
L4.grid(row=3, column=0, padx=20, pady=20)

E3 = Entry(font=('Calibri',20))
E3.grid(row=3, column=1)

B1 = Button(W, text='Calculate interest', font=('Calibri',20), command=interest)
B1.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

W.mainloop()