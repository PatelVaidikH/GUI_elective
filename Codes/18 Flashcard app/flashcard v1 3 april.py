from tkinter import Tk, Menu, Frame

w = Tk()
w.title('My Flashcard App')
w.geometry('400x400')
w.iconbitmap('bird.ico')

def addition():
    hide_frame()
    frame_1.pack(fill='both', expand=1)

def subtraction():
    hide_frame()
    frame_2.pack(fill='both', expand=1)

def multiplication():
    hide_frame()
    frame_3.pack(fill='both', expand=1)

def division():
    hide_frame()
    frame_4.pack(fill='both', expand=1)

def hide_frame():
    frame_1.pack_forget()
    frame_2.pack_forget()
    frame_3.pack_forget()
    frame_4.pack_forget()
    
app_menu = Menu(w)
w.config(menu=app_menu)

menu_1 = Menu(w)
app_menu.add_cascade(label='Flash cards', menu=menu_1)

menu_1.add_command(label='Addition', command = addition)
menu_1.add_command(label='Subtraction', command = subtraction)
menu_1.add_command(label='Multiplication', command = multiplication)
menu_1.add_command(label='Division', command = division)

frame_1 = Frame(w, width=400, height=400, bg='blue')
frame_2 = Frame(w, width=400, height=400, bg='red')
frame_3 = Frame(w, width=400, height=400, bg='yellow')
frame_4 = Frame(w, width=400, height=400, bg='green')

w.mainloop()
