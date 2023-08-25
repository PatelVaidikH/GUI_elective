# Option 1 (Try it in CMD or IDLE)
# pip install Pillow

# Option 2 (Try it in CMD or IDLE)
# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade Pillow

from tkinter import Tk, Label
from PIL import Image, ImageTk

W = Tk()
W.title('A window with an image')
W.geometry('500x500')
W.iconbitmap('icon.ico')

file = Image.open('ground.jpg')
my_image = ImageTk.PhotoImage(file)
my_label = Label(W, image = my_image)
my_label.pack()

W.mainloop()
