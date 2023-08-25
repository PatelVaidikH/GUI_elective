from tkinter import Tk, Menu, Label

W = Tk()
W.iconbitmap('icon.ico')
W.geometry('700x400')
W.title('A GUI with different menus')

def file_new():
    L.pack(pady=20)

def file_exit():
    W.destroy()

def edit_cut():
    L.pack_forget()

def edit_paste():
    L.pack(pady=20)

L = Label(W, text='Hello, Good Morning!', font=('Arial',20))

my_menu = Menu(W)
W.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label='File', menu = file_menu)
file_menu.add_command(label='New', command = file_new)
file_menu.add_command(label='Open')
file_menu.add_separator()
file_menu.add_command(label='Save')
file_menu.add_command(label='Save as')
file_menu.add_separator()
file_menu.add_command(label='Exit', command = file_exit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Undo')
edit_menu.add_command(label='Redo')
edit_menu.add_separator()
edit_menu.add_command(label='Cut', command = edit_cut)
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste', command = edit_paste)

help_menu = Menu(my_menu)
my_menu.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='Help')
help_menu.add_command(label='About')

W.mainloop()
