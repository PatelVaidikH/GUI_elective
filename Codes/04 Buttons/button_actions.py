from tkinter import Tk, Button, Label

def clicked():
    message = Label(window, text='You have clicked a button', font=('Arial',15))
    message.pack()

def exitwindow():
    window.destroy()

window = Tk()
window.geometry('1000x500')
window.title('Button actions')
window.iconbitmap('icon.ico')

a = Label(window, text='Click the buttons and observe what happen', font=('Arial',20))
a.pack(pady=15)

b = Button(window, text='Print Message', font=('Arial',20), command = clicked)
b.pack(pady=15)

c = Button(window, text='Exit', font=('Arial',20), command = exitwindow)
c.pack(pady=15)

window.mainloop()
