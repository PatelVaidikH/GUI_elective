from tkinter import Tk, Label, Button

window = Tk()
window.title('Various Buttons')
window.geometry('800x800')
window.iconbitmap('icon.ico')

my_label = Label(window, text='Creating different buttons')
my_label.pack(pady=10)

button_1 = Button(window, text='Button 1')
button_1.pack(pady=10)

button_2 = Button(window, text='Button 2', width=20)
button_2.pack(pady=10)

button_3 = Button(window, text='Button 3', height=3)
button_3.pack(pady=10)

button_4 = Button(window, text='Button 4', fg='red')
button_4.pack()

button_5 = Button(window, text='Button 5', bg='cyan')
button_5.pack()

button_6 = Button(window, text='Button 6', fg='orange', bg='green')
button_6.pack()

button_7 = Button(window, text='Button 7', bd = 10)
button_7.pack()

button_8 = Button(window, text='Button 8', font=('Arial',25))
button_8.pack()

button_9 = Button(window, text='Button 9', activeforeground = 'orange',
                  activebackground='blue')
button_9.pack()

button_10 = Button(window, text='Button 10', relief='ridge')
button_10.pack()

window.mainloop()
