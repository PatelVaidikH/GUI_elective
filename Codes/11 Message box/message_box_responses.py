from tkinter import Tk, Button, messagebox, Label

w = Tk()
w.title('Response of messagebox')
w.geometry('500x500')
w.iconbitmap('globe.ico')

def action1():
    response_1 = messagebox.showinfo('Information messagebox','This messagebox prints information')
    L1 = Label(w, text='You clicked '+response_1, font=('Arial',15))
    L1.grid(padx=20, pady=10, row=6, column=0)

def action2():
    response_2 = messagebox.askquestion('Ask question message box','This messagebox asks question')
    if response_2 == 'yes':
        L2 = Label(w, text='You clicked Yes', font=('Arial',15))
        L2.grid(padx=20, pady=10, row=6, column=0)
    if response_2 == 'no':
        L2 = Label(w, text='You clicked No.', font=('Arial',15))
        L2.grid(padx=20, pady=10, row=6, column=0)

def action3():
    response_3 = messagebox.askokcancel('Ask ok cancel message box','This message box asks question.')
    if response_3 == True:
        L3 = Label(w, text='You clicked ok.', font=('Arial',15))
        L3.grid(padx=20, pady=10, row=6, column=0)   
    if response_3 == False:
        L3 = Label(w, text='You clicked cancel.', font=('Arial',15))
        L3.grid(padx=20, pady=10, row=6, column=0)   
    
def action4():
    response_4 = messagebox.askyesno('Ask yes no message box','This message box asks question.')
    if response_4 == True:
        L4 = Label(w, text='You clicked YES.', font=('Arial',15))
        L4.grid(padx=20, pady=10, row=6, column=0)   
    if response_4 == False:
        L4 = Label(w, text='You clicked NO.', font=('Arial',15))
        L4.grid(padx=20, pady=10, row=6, column=0)   

def action5():
    response_5 = messagebox.askyesnocancel('Ask ok cancel messagebox','This message box asks a question')
    if response_5 == True:
        L5 = Label(w, text='You clicked YES.', font=('Arial',15))
        L5.grid(padx=20, pady=10, row=6, column=0)   
    if response_5 == False:
        L5 = Label(w, text='You clicked NO.', font=('Arial',15))
        L5.grid(padx=20, pady=10, row=6, column=0) 
    if response_5 == None:
        L5 = Label(w, text='You clicked CANCEL.', font=('Arial',15))
        L5.grid(padx=20, pady=10, row=6, column=0)
        
def action6():
    response_6 = messagebox.askretrycancel('Ask retry cancel messagebox', 'This messagebox gives option to retry')
    if response_6 == True:
        L5 = Label(w, text='You clicked RETRY.', font=('Arial',15))
        L5.grid(padx=20, pady=10, row=6, column=0)   
    if response_6 == False:
        L5 = Label(w, text='You clicked CANCEL.', font=('Arial',15))
        L5.grid(padx=20, pady=10, row=6, column=0) 

B1 = Button(w, text='Show info message box', font=('Arial',15), command = action1)
B1.grid(padx=20, pady=10, row=0, column=0)

B2 = Button(w, text='Ask question message box', font=('Arial',15), command = action2)
B2.grid(padx=20, pady=10, row=1, column=0)

B3 = Button(w, text='Ask ok cancel message box', font=('Arial',15), command = action3)
B3.grid(padx=20, pady=10, row=2, column=0)

B4 = Button(w, text='Ask yes no message box', font=('Arial',15), command = action4)
B4.grid(padx=20, pady=10, row=3, column=0)

B5 = Button(w, text='Ask yes no cancel message box', font=('Arial',15), command = action5)
B5.grid(padx=20, pady=10, row=4, column=0)

B6 = Button(w, text='Ask retry cancel message box', font=('Arial',15), command = action6)
B6.grid(padx=20, pady=10, row=5, column=0)

w.mainloop()
