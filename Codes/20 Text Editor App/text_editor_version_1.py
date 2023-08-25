from tkinter import Tk, Frame, Text, Scrollbar, Menu, Label, filedialog

w = Tk()
w.title('My Text editor')
w.state('zoomed')

def app_exit():
    w.destroy()

f = Frame(w)
f.pack(pady=5)

s = Scrollbar(f)
s.pack(side='right', fill='y')

t = Text(f, width=90, height=19,
          font=('Helvetica',16),
          selectbackground='yellow',
          selectforeground='black',
          undo=True,
          yscrollcommand = s.set)
t.pack()

s.config(command = t.yview)

app_menu = Menu(w)
w.config(menu=app_menu)

file_menu = Menu(app_menu, tearoff=False)
app_menu.add_cascade(label="File", menu = file_menu)
file_menu.add_command(label='New')
file_menu.add_command(label='Open')
file_menu.add_separator()
file_menu.add_command(label='Save')
file_menu.add_command(label='Save As')
file_menu.add_separator()
file_menu.add_command(label='Exit', command = app_exit)

edit_menu = Menu(app_menu, tearoff=False)
app_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label='Undo')
edit_menu.add_command(label='Redo')
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')

status_bar = Label(w, text='Ready       ', anchor='e')
status_bar.pack(fill='x', side='bottom', ipady=5)

w.mainloop()
