from tkinter import Tk, Frame, Text, Scrollbar, Menu, Label, filedialog

w = Tk()
w.title('My Text editor')
w.state('zoomed')

global open_status_name
open_status_name = False

def app_exit():
    w.destroy()

def new_file():

    global open_status_name
    open_status_name = False
    
    t.delete('1.0','end')
    w.title('New File')
    status_bar.config(text='New file Opened       ')
    
def open_file():
    t.delete('1.0','end')
    file = filedialog.askopenfilename(title='Open file',
                                      filetypes=(('Text files','*.txt'),('Python file','*.py')))

    if file:
        global open_status_name
        open_status_name = file

    status_bar.config(text=file)
    file_name = file.split(sep='/')[-1]
    w.title(f'{file_name}')

    file = open(file, 'r')
    text = file.read()
    t.insert('end',text)
    file.close()

def save_as_file():
    file = filedialog.asksaveasfilename(defaultextension='*.',
                                        title='Save as file',
                                        filetypes=(('Text files','*.txt'),('Python file','*.py')))

    if file:
        status_bar.config(text=f'Saved: {file}')
        file_name = file.split(sep='/')[-1]
        w.title(f'{file_name}')

        file = open(file, 'w')
        file.write(t.get(1.0, 'end'))
        file.close()

def save_file():
    global open_status_name
    if open_status_name:
        file = open(open_status_name, 'w')
        file.write(t.get(1.0, 'end'))
        file.close()
        status_bar.config(text=f'Saved: {open_status_name}')
    else:
        save_as_file()

def undo():
    t.edit_undo()

def redo():
    t.edit_redo()

def cut(args):
    global selection

    if args:
        selection = w.clipboard_get()

    if t.selection_get():
        selection = t.selection_get()
        t.delete('sel.first', 'sel.last')
        w.clipboard_clear()
        w.clipboard_append(selection)

def copy(args):
    global selection

    if args:
        selection = w.clipboard_get()

    if t.selection_get():
        selection = t.selection_get()
        w.clipboard_clear()
        w.clipboard_append(selection)

def paste(args):
    global selection

    if args:
        selection = w.clipboard_get()
    else:
        if selection:
            position = t.index('insert')
            t.insert(position, selection)

f = Frame(w)
f.pack(pady=5)

s = Scrollbar(f)
s.pack(side='right', fill='y')

s2 = Scrollbar(f, orient='horizontal')
s2.pack(side='bottom', fill='x')

t = Text(f, width=90, height=19,
         font=('Helvetica',16),
         selectbackground='yellow',
         selectforeground='black',
         undo=True,
         yscrollcommand = s.set,
         xscrollcommand = s2.set,
         wrap = 'none')
t.pack()

s.config(command = t.yview)
s2.config(command = t.xview)

app_menu = Menu(w)
w.config(menu=app_menu)

file_menu = Menu(app_menu, tearoff=False)
app_menu.add_cascade(label="File", menu = file_menu)
file_menu.add_command(label='New', command = new_file)
file_menu.add_command(label='Open', command = open_file)
file_menu.add_separator()
file_menu.add_command(label='Save', command = save_file)
file_menu.add_command(label='Save As', command = save_as_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command = app_exit)

edit_menu = Menu(app_menu, tearoff=False)
app_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label='Undo', command = undo)
edit_menu.add_command(label='Redo', command = redo)
file_menu.add_separator()
edit_menu.add_command(label='Cut', command = lambda: cut(False))
edit_menu.add_command(label='Copy', command = lambda: copy(False))
edit_menu.add_command(label='Paste', command = lambda: paste(False))

status_bar = Label(w, text='Ready       ', anchor='e')
status_bar.pack(fill='x', side='bottom', ipady=5)

w.mainloop()
