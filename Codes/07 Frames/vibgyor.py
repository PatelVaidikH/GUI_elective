from tkinter import Tk, Frame, Label

W = Tk()
W.geometry('700x100')
W.iconbitmap('icon.ico')
W.title('A GUI window with frame')

F1 = Frame(W, width=100, height=100, bd=5, relief='raised', bg = 'violet')
F1.grid(row=0, column=0)
L1 = Label(F1, text='V', font=('Times New Roman',50), bg = 'violet')
L1.pack()

F2 = Frame(W, width=100, height=100, bd=5, relief='raised', bg = 'indigo')
F2.grid(row=0, column=1)
L2 = Label(F2, text='I', font=('Times New Roman',50), bg = 'indigo')
L2.pack()

F3 = Frame(W, width=100, height=100, bd=5, relief='raised', bg = 'blue')
F3.grid(row=0, column=2)
L3 = Label(F3, text='B', font=('Times New Roman',50), bg = 'blue')
L3.pack()

F4 = Frame(W, width=100, height=100, bd=5, relief='raised', bg = 'green')
F4.grid(row=0, column=4)
L4 = Label(F4, text='G', font=('Times New Roman',50), bg = 'Green')
L4.pack()

F5 = Frame(W, width=100, height=100, bd=5, relief='raised', bg = 'yellow')
F5.grid(row=0, column=5)
L5 = Label(F5, text='Y', font=('Times New Roman',50), bg = 'Yellow')
L5.pack()

F6 = Frame(W, width=100, height=100, bd=5, relief='raised', bg = 'orange')
F6.grid(row=0, column=6)
L6 = Label(F6, text='O', font=('Times New Roman',50), bg = 'Orange')
L6.pack()

F7 = Frame(W, width=100, height=100, bd=5, relief='raised', bg = 'red')
F7.grid(row=0, column=7)
L7 = Label(F7, text='R', font=('Times New Roman',50), bg = 'Red')
L7.pack()

W.mainloop()