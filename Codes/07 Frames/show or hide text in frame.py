from tkinter import Tk, Frame, Label, Button

W = Tk()
W.geometry('800x600')
W.iconbitmap('icon.ico')
W.title('A GUI window with frame')

def show_frame():
    F.grid(row=5, column=0, columnspan=6, pady=10)

def show_text():
    L1.pack()

def quit_window():
    W.destroy()

L = Label(W, text='A button to show or hide text in frame', font=('Cambria',20))
L.grid(row=1, column=0, columnspan=6, pady=10)

F = Frame(W, width=400, height=100, bd=10, relief='ridge')
L1 = Label(F, text='Navrachana University', font=('Times new roman',20))

B1 = Button(W, text='Show Frame', width=10, font=('Cambria',15), command = show_frame)
B1.grid(row=3, column=1, pady=10)

B2 = Button(W, text='Show Text', width=10, font=('Cambria',15), command = show_text)
B2.grid(row=3, column=3, pady=10)

B3 = Button(W, text='Quit', width=10, font=('Cambria',15), command = quit_window)
B3.grid(row=3, column=5, pady=10)

W.mainloop()