from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

W = Tk()
W.title('Buttons to show/hide images')
W.geometry('500x500')
W.iconbitmap('icon.ico')

def show_text():
    L.pack(pady=10)

def show_image():
    my_label.pack(pady=10)

def hide_text():
    L.pack_forget()

def hide_image():
    my_label.pack_forget()

B1 = Button(W, text = 'Show text', command = show_text)
B1.pack(pady=10)

B2 = Button(W, text = 'Show Image', command = show_image)
B2.pack(pady=10)

B3 = Button(W, text = 'Hide text', command = hide_text)
B3.pack(pady=10)

B4 = Button(W, text = 'Hide Image', command = hide_image)
B4.pack(pady=10)

L = Label(W, text = 'Lucknow Cricket Stadium', font=('Arial',30))

file = Image.open('ground.jpg')
my_image = ImageTk.PhotoImage(file)
my_label = Label(W, text = 'Cricket Stadium', image = my_image, compound='top')

W.mainloop()
