from tkinter import Tk, Menu, Label

def file_new():
    global L
    L = Label(W, text='Hello, Good Morning!', font=('Arial',20))
    L.pack()
    
def file_exit():
    W.destroy()
    
def edit_cut():
    L.pack_forget()

def edit_copy():
    pass

def edit_paste():
    L.pack()

W = Tk()
W.title('Creating menu in Tkinter')
W.geometry('500x500')
W.iconbitmap('icon.ico')

my_menu = Menu(W)
W.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command = file_new)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save as")
file_menu.add_command(label="Close")
file_menu.add_separator()
file_menu.add_command(label="Exit", command = file_exit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command = edit_cut)
edit_menu.add_command(label="Copy", command = edit_copy)
edit_menu.add_command(label="Paste", command = edit_paste)

W.mainloop()