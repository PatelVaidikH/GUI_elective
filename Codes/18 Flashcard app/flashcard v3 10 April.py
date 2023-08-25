from tkinter import Tk, Menu, Frame, Label, Entry, Button, IntVar
from random import randint

w = Tk()
w.title('My Flashcard App')
w.geometry('400x400')
w.iconbitmap('bird.ico')

def check_addition(x, y):
    true_addition = x + y

    if int(addition_answer.get()) == true_addition:
        addition_message.config(text='Correct: '+str(x)+' + '+str(y)+' = '+str(true_addition))
    else:
        addition_message.config(text='Incorrect: '+str(x)+' + '+str(y)+' = '+str(true_addition)+', Not '+str(addition_answer.get()))

def check_subtraction(x, y):
    true_subtraction = x - y

    if int(subtraction_answer.get()) == true_subtraction:
        subtraction_message.config(text='Correct: '+str(x)+' - '+str(y)+' = '+str(true_subtraction))
    else:
        subtraction_message.config(text='Incorrect: '+str(x)+' - '+str(y)+' = '+str(true_subtraction)+', Not '+str(subtraction_answer.get()))

def check_multiplication(x, y):
    true_multiplication = x * y

    if int(multiplication_answer.get()) == true_multiplication:
        multiplication_message.config(text='Correct: '+str(x)+' x '+str(y)+' = '+str(true_multiplication))
    else:
        multiplication_message.config(text='Incorrect: '+str(x)+' x '+str(y)+' = '+str(true_multiplication)+', Not '+str(multiplication_answer.get()))

def check_division(x, y):
    true_division = int(x / y)

    if int(division_answer.get()) == true_division:
        division_message.config(text='Correct: '+str(x)+' ÷ '+str(y)+' = '+str(true_division))
    else:
        division_message.config(text='Incorrect: '+str(x)+' ÷ '+str(y)+' = '+str(true_division)+', Not '+str(division_answer.get()))

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
    addition_message = Label(frame_1, text=" ", font=('Calibri',12))
    addition_message.pack(pady=10)

def subtraction():
    hide_frame()
    frame_2.pack(fill='both', expand=1)

    global n1, n2
    n1 = IntVar()
    n2 = IntVar()

    n1.set(randint(0,10))
    n2.set(randint(0,10))

    subtraction_label = Label(frame_2, text=str(n1.get())+" - "+str(n2.get()), font=('Calibri',32))
    subtraction_label.pack(pady=10)

    global subtraction_answer
    subtraction_answer = Entry(frame_2, font=('Calibri',16))
    subtraction_answer.pack(pady=10)

    subtraction_button = Button(frame_2,
                             text='Check Answer',
                             font=('Calibri',14),
                             command = lambda: check_subtraction(n1.get(),n2.get()))
    subtraction_button.pack(pady=10)

    global subtraction_message
    subtraction_message = Label(frame_2, text=" ", font=('Calibri',12))
    subtraction_message.pack(pady=10)

def multiplication():
    hide_frame()
    frame_3.pack(fill='both', expand=1)

    global n1, n2
    n1 = IntVar()
    n2 = IntVar()

    n1.set(randint(0,10))
    n2.set(randint(0,10))

    multiplication_label = Label(frame_3, text=str(n1.get())+" x "+str(n2.get()), font=('Calibri',32))
    multiplication_label.pack(pady=10)

    global multiplication_answer
    multiplication_answer = Entry(frame_3, font=('Calibri',16))
    multiplication_answer.pack(pady=10)

    multiplication_button = Button(frame_3,
                             text='Check Answer',
                             font=('Calibri',14),
                             command = lambda: check_multiplication(n1.get(),n2.get()))
    multiplication_button.pack(pady=10)

    global multiplication_message
    multiplication_message = Label(frame_3, text=" ", font=('Calibri',12))
    multiplication_message.pack(pady=10)

def division():
    hide_frame()
    frame_4.pack(fill='both', expand=1)

    global n1, n2
    n1 = IntVar()
    n2 = IntVar()

    n2.set(randint(1,10))
    n1.set(n2.get()*randint(1,10))

    division_label = Label(frame_4, text=str(n1.get())+" ÷ "+str(n2.get()), font=('Calibri',32))
    division_label.pack(pady=10)

    global division_answer
    division_answer = Entry(frame_4, font=('Calibri',16))
    division_answer.pack(pady=10)

    division_button = Button(frame_4,
                             text='Check Answer',
                             font=('Calibri',14),
                             command = lambda: check_division(n1.get(),n2.get()))
    division_button.pack(pady=10)

    global division_message
    division_message = Label(frame_4, text=" ", font=('Calibri',12))
    division_message.pack(pady=10)

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

frame_1 = Frame(w, width=400, height=400)
frame_2 = Frame(w, width=400, height=400)
frame_3 = Frame(w, width=400, height=400)
frame_4 = Frame(w, width=400, height=400)

w.mainloop()
