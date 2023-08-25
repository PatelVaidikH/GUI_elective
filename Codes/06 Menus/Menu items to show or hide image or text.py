from tkinter import Tk, Menu, Label, Button
from PIL import Image, ImageTk

def quit_gui():
    W.destroy()

def file_new_text():
    L.pack()

def file_new_image():
    I.pack()

def edit_delete_image():
    I.pack_forget()

def edit_delete_text():
    L.pack_forget()

W = Tk()
W.title('Creating menu in Tkinter')
W.geometry('500x500')
W.iconbitmap('icon.ico')

L = Label(W, text='Hello, Good Morning!', font=('Arial',20))

B = Button(W, text='Quit', command=quit_gui, font=('Arial',20))
B.pack()

file = Image.open('ground.jpg')
my_image = ImageTk.PhotoImage(file)
I = Label(W, text='Image information', image = my_image, compound='bottom')


my_menu = Menu(W)
W.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Image", command = file_new_image)
file_menu.add_command(label="New Text", command = file_new_text)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Delete image", command = edit_delete_image)
edit_menu.add_command(label="Delete text", command = edit_delete_text)

W.mainloop()