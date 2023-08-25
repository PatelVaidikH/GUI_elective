from tkinter import Tk, Label

my_win = Tk()
my_win.title('My Windows with texts')
my_win.geometry('500x500')
my_win.iconbitmap('cricket.ico')

label_1 = Label(my_win, text="Hello, Good Morning, It is Tuesday!")
label_1.pack()

label_2 = Label(my_win, text="I love Navrachana University!")
label_2.pack()

label_3 = Label(my_win, text="This text is red coloured", fg='red')
label_3.pack()

label_4 = Label(my_win, text="This text has yellow background", bg='yellow')
label_4.pack()

label_5 = Label(my_win, text="Cyan in blue", fg='cyan', bg='blue')
label_5.pack()

label_6 = Label(my_win, text="Large Text", font = ('Arial',48))
label_6.pack()

label_7 = Label(my_win, text="Sunken text", relief='sunken')
label_7.pack()

label_8 = Label(my_win, text="Raised text", relief='raised')
label_8.pack()

label_9 = Label(my_win, text="Ridge text", relief='ridge')
label_9.pack()

label_10 = Label(my_win, text="Groove text", relief='groove')
label_10.pack()

label_11 = Label(my_win, text="Disabled text", state='disable')
label_11.pack()

label_12 = Label(my_win, text="Bold text", font = ('Arial 15 bold'))
label_12.pack()

label_13 = Label(my_win, text="Italic text", font = ('Arial 8 italic'))
label_13.pack()

label_14 = Label(my_win, text="Underline text", font = ('Times 10 underline'))
label_14.pack()

label_15 = Label(my_win, text="Heighed text", height = 3, bg='green')
label_15.pack()

label_16 = Label(my_win, text="Heighed text", height = 5, bg='blue', fg='white')
label_16.pack()

my_win.mainloop()
