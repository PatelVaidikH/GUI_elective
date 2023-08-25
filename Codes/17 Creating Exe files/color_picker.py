from tkinter import Tk, Label, Button, colorchooser

w = Tk()
w.title('Color picker')
w.geometry('300x300')

def action():
    c = colorchooser.askcolor()[1]
    L = Label(w, text=c)
    L.pack()
    L1 = Label(w, text='You choose this color.',bg=c)
    L1.pack()

L1 = Label(w, text='Click the button to select a color:')
L1.pack()

B1 = Button(w, text='Select', command = action)
B1.pack()

w.mainloop()

##pyinstaller --onefile --windowed color_picker.py