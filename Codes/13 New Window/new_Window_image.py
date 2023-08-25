from tkinter import Tk, Label, Button, Toplevel
from PIL import ImageTk, Image

w = Tk()
w.title('Main window')
w.geometry('700x300')
w.iconbitmap('bird.ico')

def openimage():
    new = Toplevel()
    new.geometry('400x150')
    new.title('Navrachana University Logo')
    new.iconbitmap('globe.ico')

    my_image = ImageTk.PhotoImage(Image.open('nuv.png'))
    L1 = Label(new, image=my_image)
    L1.pack()

    new.mainloop()

L = Label(w, text='Click button below to open an image', font=('Consolas',20))
L.pack()

B = Button(w, text='Open image', font=('Consolas',20), command = openimage)
B.pack()

w.mainloop()
