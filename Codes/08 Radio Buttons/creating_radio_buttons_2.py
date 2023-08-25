from tkinter import Tk, Label, IntVar, Radiobutton, W, Button

my_win = Tk()
my_win.geometry('600x500')
my_win.iconbitmap('icon.ico')
my_win.title('Question')

def submit():
    if v.get() == 3:
        L2 = Label(my_win, text='Your answer is correct.', font=('Calibri',12))
        L2.grid(row=6, column=0, sticky='W', padx=50, pady=5)
    else:
        L3 = Label(my_win, text='Your answer is wrong.', font=('Calibri',12))
        L3.grid(row=6, column=0, sticky='W', padx=50, pady=5)
    
L = Label(my_win, text='Who is captain of India T20 Cricket?', font=('Calibri',12))
L.grid(row=0, column=0, padx=50, pady=5)

v = IntVar()

R1 = Radiobutton(my_win, text='Rohit Sharma', variable=v, value=1, font=('Calibri',12))
R1.grid(row=1, column=0, sticky='W', padx=50, pady=5)

R2 = Radiobutton(my_win, text='Virat Kohli', variable=v, value=2, font=('Calibri',12))
R2.grid(row=2, column=0, sticky='W', padx=50, pady=5)

R3 = Radiobutton(my_win, text='Hardik Pandya', variable=v, value=3, font=('Calibri',12))
R3.grid(row=3, column=0, sticky='W', padx=50, pady=5)

R4 = Radiobutton(my_win, text='KL Rahul', variable=v, value=4, font=('Calibri',12))
R4.grid(row=4, column=0, sticky='W', padx=50, pady=5)

B = Button(my_win, text='Submit', font=('Calibri',12), command=submit)
B.grid(row=5, column=0, padx=50, pady=5)

my_win.mainloop()