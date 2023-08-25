from tkinter import Tk, Label, W, E

my_win = Tk()
my_win.title('Using Grid for label')
my_win.geometry('500x500')
my_win.iconbitmap('cricket.ico')

my_label_1 = Label(my_win, text='This is a really long sentence. This is a really long sentence.', fg='blue')
my_label_1.grid(row=0, column=0, columnspan=2)

my_label_2 = Label(my_win, text='Short word 1', fg='red')
my_label_2.grid(row=1, column=0, sticky = W)

my_label_3 = Label(my_win, text='Short word 2', fg='green')
my_label_3.grid(row=1, column=1, sticky = E)


my_win.mainloop()
