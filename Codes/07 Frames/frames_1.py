from tkinter import Tk, Frame, Label

W = Tk()
W.geometry('500x500')
W.iconbitmap('icon.ico')
W.title('A GUI window with frame')

my_frame = Frame(W, width=200, height=100, bd=5, relief='sunken', bg = 'cyan')
my_frame.grid(row=0, column=0, padx=20, pady=20)

L1 = Label(W, text='Text 1', font=('Arial',20), bg = 'blue', fg='white')
L1.grid(padx=20, pady=20)

L2 = Label(my_frame, text='Text 2', font=('Arial',20), bg = 'blue', fg='white')
L2.grid(padx=20, pady=20)

W.mainloop()