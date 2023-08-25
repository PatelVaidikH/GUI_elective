from tkinter import Tk, Entry, Button

calc = Tk()
calc.geometry('350x350')
calc.title('Calculator')
calc.iconbitmap('calculator.ico')
    
E = Entry(font=('Calibri',20), borderwidth=5)
E.grid(row=0, column=0, columnspan=4)

def number(n):
    current = E.get()
    E.delete(0, 'end')
    E.insert(0,str(current) + str(n))
    
def clear():
    E.delete(0, 'end')
    
def add():
    n1 = E.get()
    global N1
    N1 = int(n1)
    global operation
    operation = 'addition'
    E.delete(0, 'end')
    
def ans():
    n2 = E.get()
    E.delete(0, 'end')
    N2 = int(n2)
    if operation == 'addition':
        E.insert(0, N1 + N2)
    if operation == 'subtraction':
        E.insert(0, N1 - N2)
    if operation == 'multiplication':
        E.insert(0, N1 * N2)
    if operation == 'division':
        try:
            E.insert(0, N1 / N2)
        except:
            pass
        
def subtract():
    n1 = E.get()
    global N1
    N1 = int(n1)
    global operation
    operation = 'subtraction'
    E.delete(0, 'end')

def multiply():
    n1 = E.get()
    global N1
    N1 = int(n1)
    global operation
    operation = 'multiplication'
    E.delete(0, 'end')

def divide():
    n1 = E.get()
    global N1
    N1 = int(n1)
    global operation
    operation = 'division'
    E.delete(0, 'end')

B0 = Button(calc, text='0', font=('Calibri',20), width=4, command = lambda: number(0))
B0.grid(row=4, column=0)

B1 = Button(calc, text='1', font=('Calibri',20), width=4, command = lambda: number(1))
B1.grid(row=3, column=0)

B2 = Button(calc, text='2', font=('Calibri',20), width=4, command = lambda: number(2))
B2.grid(row=3, column=1)

B3 = Button(calc, text='3', font=('Calibri',20), width=4, command = lambda: number(3))
B3.grid(row=3, column=2)

B4 = Button(calc, text='4', font=('Calibri',20), width=4, command = lambda: number(4))
B4.grid(row=2, column=0)

B5 = Button(calc, text='5', font=('Calibri',20), width=4, command = lambda: number(5))
B5.grid(row=2, column=1)

B6 = Button(calc, text='6', font=('Calibri',20), width=4, command = lambda: number(6))
B6.grid(row=2, column=2)

B7 = Button(calc, text='7', font=('Calibri',20), width=4, command = lambda: number(7))
B7.grid(row=1, column=0)

B8 = Button(calc, text='8', font=('Calibri',20), width=4, command = lambda: number(8))
B8.grid(row=1, column=1)

B9 = Button(calc, text='9', font=('Calibri',20), width=4, command = lambda: number(9))
B9.grid(row=1, column=2)

B10 = Button(calc, text='+', font=('Calibri',20), width=4, command = add)
B10.grid(row=1, column=3)

B11 = Button(calc, text='-', font=('Calibri',20), width=4, command = subtract)
B11.grid(row=2, column=3)

B12 = Button(calc, text='x', font=('Calibri',20), width=4, command = multiply)
B12.grid(row=3, column=3)

B13 = Button(calc, text='÷', font=('Calibri',20), width=4, command = divide)
B13.grid(row=4, column=3)

B14 = Button(calc, text='=', font=('Calibri',20), width=4, command = ans)
B14.grid(row=4, column=2)

B15 = Button(calc, text='C', font=('Calibri',20), width=4, command = clear)
B15.grid(row=4, column=1)

calc.mainloop()