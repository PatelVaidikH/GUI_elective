from tkinter import Tk, Checkbutton, IntVar, Button

window = Tk()
window.title('Various Check boxes')
window.geometry('500x500')
window.iconbitmap('globe.ico')

def checkstatus():
    print(v.get())

v = IntVar()

c1 = Checkbutton(window)
c1.pack()

c2 = Checkbutton(window, text='Good morning', variable=v, onvalue=1, offvalue=0)
c2.pack()

B = Button(window, text='Check status', command=checkstatus)
B.pack()

window.mainloop()
