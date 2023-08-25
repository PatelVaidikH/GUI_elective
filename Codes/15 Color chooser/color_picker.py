from tkinter import Tk, Label, Button, colorchooser

w = Tk()
w.title('Color selector')
w.geometry('500x500')
w.iconbitmap('globe.ico')

def action():
    c = colorchooser.askcolor()[1]
    L2 = Label(w, text=c, font=('Calibri',15))
    L2.pack()

    L3 = Label(w, text='You have selected this color.',fg=c, font=('Times',20))
    L3.pack()

L1 = Label(w, text='Click following button to select a color:', font=('Calibri',15))
L1.pack()

B1 = Button(w, text='Select', command=action, font=('Calibri',15))
B1.pack()

w.mainloop()
