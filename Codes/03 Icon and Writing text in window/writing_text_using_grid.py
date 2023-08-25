from tkinter import Tk, Label

my_win = Tk()
my_win.title('Using Grid for label')
my_win.geometry('500x500')
my_win.iconbitmap('cricket.ico')

my_label_1 = Label(my_win, text='First label', fg='blue')
my_label_1.grid(row=2, column=0)

my_label_2 = Label(my_win, text='Second label', fg='red')
my_label_2.grid(row=1, column=1)

my_label_3 = Label(my_win, text='Third label', fg='green')
my_label_3.grid(row=0, column=2)


my_win.mainloop()
