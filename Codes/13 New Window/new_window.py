from tkinter import Tk, Label, Toplevel, Button

w = Tk()
w.title('Main window')
w.iconbitmap('globe.ico')
w.geometry('500x500')

def open_new_win():
    new_win = Toplevel()
    new_win.title('New window')
    new_win.geometry('300x300')
    new_win.iconbitmap('bird.ico')

    L2 = Label(new_win, text='This is a Toplevel window')
    L2.pack()

##    B2 = Button(new_win, text='Hide main window', command = w.iconify)
##    B2.pack()
##    B3 = Button(new_win, text='Show main window', command = w.deiconify)
##    B3.pack()

    B2 = Button(new_win, text='Hide main window', command = w.withdraw)
    B2.pack()
    B3 = Button(new_win, text='Show main window', command = w.deiconify)
    B3.pack()

    B4 = Button(new_win, text='Exit main window', command = w.destroy)
    B4.pack()

    close_new_win = Button(new_win, text='Close this window', command = new_win.destroy)
    close_new_win.pack()

    new_win.mainloop()
    
L1 = Label(w, text='This is a main window')
L1.pack()

B1 = Button(w, text='Open new window', command = open_new_win)
B1.pack()

w.mainloop()
