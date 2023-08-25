from tkinter import Tk, Menu, Frame, Label, Entry, Button, IntVar
from random import randint

w = Tk()
w.title('My Flashcard App')
w.geometry('400x400')
w.iconbitmap('bird.ico')

def check_addition(x, y):
    true_addition = x + y

    if int(addition_answer.get()) == true_addition:
        addition_message.config(text='Correct')
    else:
        addition_message.config(text='Incorrect, Try again!')

def addition():
    hide_frame()
    frame_1.pack(fill='both', expand=1)

    global n1, n2
    n1 = IntVar()
    n2 = IntVar()

    n1.set(randint(0,10))
    n2.set(randint(0,10))

    addition_label = Label(frame_1, text=str(n1.get())+" + "+str(n2.get()), font=('Calibri',32))
    addition_label.pack(pady=10)

    global addition_answer
    addition_answer = Entry(frame_1, font=('Calibri',16))
    addition_answer.pack(pady=10)

    addition_button = Button(frame_1,
                             text='Check Answer',
                             font=('Calibri',14),
                             command = lambda: check_addition(n1.get(),n2.get()))
    addition_button.pack(pady=10)

    global addition_message
    addition_message = Label(frame_1, text="Click button to check your answer", font=('Calibri',12))
    addition_message.pack(pady=10)

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
