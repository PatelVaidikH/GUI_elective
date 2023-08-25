from tkinter import Tk, Menu, Frame, Label, Entry, Button, IntVar
from random import randint

w = Tk()
w.title('My Flashcard App')
w.geometry('400x400')
w.iconbitmap('icon.ico')

def home():
    
    hide_menu_frame()
    
    frame_5.pack(fil='both', expand=1)
    
    start_label = Label(frame_5, text='Welcome to Flashcard App!', font=('Calibri',16))
    start_label.pack(pady=5)
    
    button_1 = Button(frame_5, text='Addition Flashcard!', font=('Calibri',14), command=add)
    button_1.pack(pady=5)
    
    button_2 = Button(frame_5, text='Subtraction Flashcard!', font=('Calibri',14), command=subtract)
    button_2.pack(pady=5)
    
    button_3 = Button(frame_5, text='Multiplication Flashcard!', font=('Calibri',14), command=multiply)
    button_3.pack(pady=5)
    
    button_4 = Button(frame_5, text='Division Flashcard!', font=('Calibri',14), command=divide)
    button_4.pack(pady=5)

def check_addition(x, y):
    true_addition = x + y
    
    if int(add_answer.get()) == true_addition:
        add_answer_label.config(text='Correct: ' + str(x) +' + '+str(y)+' = '+str(true_addition))
    else:
        add_answer_label.config(text='Incorrect: ' + str(x) +' + '+str(y)+' = '+str(true_addition)+'. Not '+str(add_answer.get()))

    add_answer.delete(0, 'end')  
    n1.set(randint(0, 10))
    n2.set(randint(0, 10))
    add_label.config(text=str(n1.get())+" + "+str(n2.get()), font=('Calibri',32))
    
def check_sub(x, y):
    true_sub = x - y
    
    if int(sub_answer.get()) == true_sub:
        sub_answer_label.config(text='Correct: ' + str(x) +' - '+str(y)+' = '+str(true_sub))
    else:
        sub_answer_label.config(text='Incorrect: ' + str(x) +' - '+str(y)+' = '+str(true_sub)+'. Not '+str(sub_answer.get()))

    sub_answer.delete(0, 'end')  
    n1.set(randint(0, 10))
    n2.set(randint(0, 10))
    sub_label.config(text=str(n1.get())+" - "+str(n2.get()), font=('Calibri',32))
    
def check_multi(x, y):
    true_multi = x * y
    
    if int(multi_answer.get()) == true_multi:
        multi_answer_label.config(text='Correct: ' + str(x) +' x '+str(y)+' = '+str(true_multi))
    else:
        multi_answer_label.config(text='Incorrect: ' + str(x) +' x '+str(y)+' = '+str(true_multi)+'. Not '+str(multi_answer.get()))

    multi_answer.delete(0, 'end')  
    n1.set(randint(0, 10))
    n2.set(randint(0, 10))
    multi_label.config(text=str(n1.get())+" x "+str(n2.get()), font=('Calibri',32))
    
def check_div(x, y):
    true_div = int(x / y)
    
    if int(div_answer.get()) == true_div:
        div_answer_label.config(text='Correct: ' + str(x) +' ÷ '+str(y)+' = '+str(true_div))
    else:
        div_answer_label.config(text='Incorrect: ' + str(x) +' ÷ '+str(y)+' = '+str(true_div)+'. Not '+str(div_answer.get()))

    div_answer.delete(0, 'end')  
    n2.set(randint(1, 10))
    n1.set(n2.get()*randint(0,10))
    div_label.config(text=str(n1.get())+" ÷ "+str(n2.get()), font=('Calibri',32))
    
def add():
    hide_menu_frame()
    frame_1.pack(fill='both', expand=1)
    
    global n1, n2
    
    n1 = IntVar()
    n2 = IntVar()
    
    n1.set(randint(0,10))
    n2.set(randint(0,10))
    
    global add_label
    add_label = Label(frame_1, text=str(n1.get())+" + "+str(n2.get()), font=('Calibri',32))
    add_label.pack(pady=10)
    
    global add_answer
    add_answer = Entry(frame_1)
    add_answer.pack(pady=5)
    
    add_button = Button(frame_1, text='Answer', command = lambda: check_addition(n1.get(),n2.get()))
    add_button.pack(pady=5) 
    
    global add_answer_label
    add_answer_label = Label(frame_1, text='')
    add_answer_label.pack(pady=5)
    
def subtract():
    hide_menu_frame()
    frame_2.pack(fill='both', expand=1)
    
    global n1, n2
    
    n1 = IntVar()
    n2 = IntVar()
    
    n1.set(randint(0,10))
    n2.set(randint(0,10))
    
    global sub_label
    sub_label = Label(frame_2, text=str(n1.get())+" - "+str(n2.get()), font=('Calibri',32))
    sub_label.pack(pady=10)
    
    global sub_answer
    sub_answer = Entry(frame_2)
    sub_answer.pack(pady=5)
    
    sub_button = Button(frame_2, text='Answer', command = lambda: check_sub(n1.get(),n2.get()))
    sub_button.pack(pady=5) 
    
    global sub_answer_label
    sub_answer_label = Label(frame_2, text='')
    sub_answer_label.pack(pady=5)
    
def multiply():
    hide_menu_frame()
    frame_3.pack(fill='both', expand=1)
    
    global n1, n2
    
    n1 = IntVar()
    n2 = IntVar()
    
    n1.set(randint(0,10))
    n2.set(randint(0,10))
    
    global multi_label
    multi_label = Label(frame_3, text=str(n1.get())+" x "+str(n2.get()), font=('Calibri',32))
    multi_label.pack(pady=10)
    
    global multi_answer
    multi_answer = Entry(frame_3)
    multi_answer.pack(pady=5)
    
    multi_button = Button(frame_3, text='Answer', command = lambda: check_multi(n1.get(),n2.get()))
    multi_button.pack(pady=5) 
    
    global multi_answer_label
    multi_answer_label = Label(frame_3, text='')
    multi_answer_label.pack(pady=5)
    
def divide():
    hide_menu_frame()
    frame_4.pack(fill='both', expand=1)
    
    global n1, n2
    
    n1 = IntVar()
    n2 = IntVar()
    
    n2.set(randint(1, 10))
    n1.set(n2.get()*randint(0,10))
                         
    global div_label
    div_label = Label(frame_4, text=str(n1.get())+" ÷ "+str(n2.get()), font=('Calibri',32))
    div_label.pack(pady=10)
    
    global div_answer
    div_answer = Entry(frame_4)
    div_answer.pack(pady=5)
    
    div_button = Button(frame_4, text='Answer', command = lambda: check_div(n1.get(),n2.get()))
    div_button.pack(pady=5) 
    
    global div_answer_label
    div_answer_label = Label(frame_4, text='')
    div_answer_label.pack(pady=5)

def exit_w():
    w.destroy()
    
def hide_menu_frame():
    
    for widget in frame_1.winfo_children():
        widget.destroy()
        
    for widget in frame_2.winfo_children():
        widget.destroy()
    
    for widget in frame_3.winfo_children():
        widget.destroy()
    
    for widget in frame_4.winfo_children():
        widget.destroy()
    
    for widget in frame_5.winfo_children():
        widget.destroy()
        
    frame_1.pack_forget()
    frame_2.pack_forget()
    frame_3.pack_forget()
    frame_4.pack_forget()
    frame_5.pack_forget()
    
my_menu = Menu(w)
w.config(menu=my_menu)

math_menu = Menu(w)
my_menu.add_cascade(label="MathCards", menu = math_menu)

math_menu.add_command(label="Home", command = home)
math_menu.add_separator()
math_menu.add_command(label="Add", command = add)
math_menu.add_command(label="Subtract", command = subtract)
math_menu.add_command(label="Multiply", command = multiply)
math_menu.add_command(label="Divide", command = divide)
math_menu.add_separator()
math_menu.add_command(label="Exit", command=exit_w)

frame_1 = Frame(w, width=400, height=400)
frame_2 = Frame(w, width=400, height=400)
frame_3 = Frame(w, width=400, height=400)
frame_4 = Frame(w, width=400, height=400)
frame_5 = Frame(w, width=400, height=400)

home()

w.mainloop()