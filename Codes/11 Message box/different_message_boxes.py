from tkinter import Tk, Button, messagebox

window = Tk()
window.title('Different types of messageboxes')
window.geometry('800x500')
window.iconbitmap('globe.ico')

def message_box_1():
    messagebox.showinfo('Simple message box','This messagebox gives information.')

def message_box_2():
    messagebox.showwarning('Warning message box','This messagebox gives warning.')

def message_box_3():
    messagebox.showerror('Error message box','This messagebox shows an error.')

def message_box_4():
    messagebox.askquestion('Question message box','This messagebox asks a question.')

def message_box_5():
    messagebox.askokcancel('Question message box','This messagebox asks a question with option of ok and cancel.')

def message_box_6():
    messagebox.askyesno('Question message box','This messagebox asks a question with option of yes and no.')

# try askyesnocancel, askretrycancel
    
B1 = Button(window, text='Button 1', font=('Arial',20), command=message_box_1)
B1.grid(row=0, column=0, padx=20, pady=20)

B2 = Button(window, text='Button 2', font=('Arial',20), command=message_box_2)
B2.grid(row=0, column=1, padx=20, pady=20)

B3 = Button(window, text='Button 3', font=('Arial',20), command=message_box_3)
B3.grid(row=0, column=2, padx=20, pady=20)

B4 = Button(window, text='Button 4', font=('Arial',20), command=message_box_4)
B4.grid(row=1, column=0, padx=20, pady=20)

B5 = Button(window, text='Button 5', font=('Arial',20), command=message_box_5)
B5.grid(row=1, column=1, padx=20, pady=20)

B6 = Button(window, text='Button 6', font=('Arial',20), command=message_box_6)
B6.grid(row=1, column=2, padx=20, pady=20)

window.mainloop()
