from tkinter import *

my_win = Tk()
my_win.geometry('600x600')
my_win.iconbitmap('globe.ico')
my_win.title('Quiz')

def checkscore():
    score = 0
    if a.get() == 2:
        score = score + 1
    if b.get() == 3:
        score = score + 1
    if c.get() == 2:
        score = score + 1
    
    score_label = Label(my_win, text='You scored %d/3 in quiz.'%score, font=('Calibri',20))
    score_label.grid(row = 14, column = 0)

    B.config(state='disabled')
    
L1 = Label(my_win, text='Quiz about India', font=('Calibri',25))
L1.grid(row = 0, column = 0)
        
L2 = Label(my_win, text='Question 1: What is capital of India?', font=('Calibri',20))
L2.grid(row = 1, column = 0, sticky='w')

a = IntVar()

R1 = Radiobutton(my_win, text='Mumbai', value=1, variable=a, font=('Calibri',15))
R1.grid(row = 2, column = 0, sticky='w')
R2 = Radiobutton(my_win, text='New Delhi', value=2, variable=a, font=('Calibri',15))
R2.grid(row = 3, column = 0, sticky='w')
R3 = Radiobutton(my_win, text='Chennai', value=3, variable=a, font=('Calibri',15))
R3.grid(row = 4, column = 0, sticky='w')

L3 = Label(my_win, text='Question 2: Who is prime minister of India?', font=('Calibri',20))
L3.grid(row = 5, column = 0, sticky='w')

b = IntVar()

R4 = Radiobutton(my_win, text='Rajnath Singh', value=1, variable=b, font=('Calibri',15))
R4.grid(row = 6, column = 0, sticky='w')
R5 = Radiobutton(my_win, text='Droupadi Murmuru', value=2, variable=b, font=('Calibri',15))
R5.grid(row = 7, column = 0, sticky='w')
R6 = Radiobutton(my_win, text='Narendra Modi', value=3, variable=b, font=('Calibri',15))
R6.grid(row = 8, column = 0, sticky='w')

L4 = Label(my_win, text='Question 3: Which animal is national animal of India?', font=('Calibri',20))
L4.grid(row = 9, column = 0, sticky='w')

c = IntVar()

R7 = Radiobutton(my_win, text='Lion', value=1, variable=c, font=('Calibri',15))
R7.grid(row = 10, column = 0, sticky='w')
R8 = Radiobutton(my_win, text='Tiger', value=2, variable=c, font=('Calibri',15))
R8.grid(row = 11, column = 0, sticky='w')
R9 = Radiobutton(my_win, text='Leopard', value=3, variable=c, font=('Calibri',15))
R9.grid(row = 12, column = 0, sticky='w')

B = Button(my_win, text='Check score', command = checkscore, font=('Calibri',15))
B.grid(row = 13, column = 0)

my_win.mainloop()
