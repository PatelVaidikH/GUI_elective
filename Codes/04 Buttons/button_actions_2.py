from tkinter import Tk, Label, Button

def printmessage():
    global d
    d = Label(w, text='Hello, Good Morning, You are in NUV.')
    d.pack()

def clearmessage():
    d.destroy()

w = Tk()
w.title('Print and hide message using buttons')
w.iconbitmap('icon.ico')
w.geometry('800x500')

a = Label(w,text='Demonstrate buttons to print or hide the message', font=('Arial',20))
a.pack(pady=10)

b = Button(w, text='Print Message', font=('Arial',20), command = printmessage)
b.pack(pady=10)

c = Button(w, text='Clear Message', font=('Arial',20), command = clearmessage)
c.pack(pady=10)

w.mainloop()
