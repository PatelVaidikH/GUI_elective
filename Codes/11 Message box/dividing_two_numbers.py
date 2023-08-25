from tkinter import Tk, Button, messagebox, Label, Entry

w = Tk()
w.title('Dividing two numbers')
w.geometry('500x500')
w.iconbitmap('globe.ico')

def action1():
    if E2.get()=='0':
        messagebox.showerror('Error','Denominator cannot be zero, try again!')
    else:
        messagebox.showinfo('Success','Your input is valid for division')
        B1.pack_forget()
        B2.pack()

def action2():
    result = float(E1.get()) / float(E2.get())
    messagebox.showinfo('Resul+t','%f / %f = %f'%(float(E1.get()), float(E2.get()), result))

L1 = Label(w, text='Enter first number:',font=('Arial',20))
L1.pack()

E1 = Entry()
E1.pack()

L2 = Label(w, text='Enter second number:',font=('Arial',20))
L2.pack()

E2 = Entry()
E2.pack()

B1 = Button(w, text='Check validity',font=('Arial',20), command=action1)
B1.pack()

B2 = Button(w, text='Divide',font=('Arial',20), command=action2)


w.mainloop()
