from tkinter import Tk, Entry

window = Tk()
window.geometry('500x500')
window.title('Input entry box')
window.iconbitmap('globe.ico')

E = Entry()
E.pack(pady=10)

E1 = Entry(width=50)
E1.pack(pady=10)

E2 = Entry(font=('Times new roman',30))
E2.pack(pady=10)

window.mainloop()
