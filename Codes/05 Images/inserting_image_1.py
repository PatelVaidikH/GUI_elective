from tkinter import Tk, Label
from PIL import Image, ImageTk

W = Tk()
W.title('A window with an image and title')
W.geometry('500x500')
W.iconbitmap('icon.ico')

file = Image.open('ground.jpg')
my_image = ImageTk.PhotoImage(file)
my_label = Label(W, text = 'Cricket Stadium', image = my_image, compound='top')
my_label.pack()

W.mainloop()
