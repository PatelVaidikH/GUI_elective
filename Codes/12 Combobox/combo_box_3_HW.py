from tkinter import Tk, Label, Button
from tkinter.ttk import Combobox

w = Tk()
w.state('zoomed')
w.title('Navrachana Restaurant')
w.iconbitmap('hotel.ico')

def order():
    p = 0

    if c_1.get() == 'Clear Soup':
        p = p + 100
    if c_1.get() == 'Tomato Soup':
        p = p + 110
    if c_1.get() == 'Sweet Corn Soup':
        p = p + 115
    if c_1.get() == 'Hot & Sour Soup':
        p = p + 120
    if c_1.get() == 'Manchaw Soup':
        p = p + 130

    if c_2.get() == 'Harabhara Kabab':
        p = p + 140
    if c_2.get() == 'Paneer Chilly':
        p = p + 160
    if c_2.get() == 'Manchurian':
        p = p + 180
    if c_2.get() == 'Veg 365':
        p = p + 150
    if c_2.get() == 'Paneer Tikka':
        p = p + 170

    ## Homework: Add if condition of more item prices here

    global p_label, gst_label, total_label
    p_label = Label(w, text='Total: Rs. %d'%p, font=('Arial',15))
    p_label.grid(row=5, column=0, padx=10, pady=10)

    gst_p = p*0.18
    gst_label = Label(w, text='GST: Rs. %d'%gst_p, font=('Arial',15))
    gst_label.grid(row=5, column=1, padx=10, pady=10)

    total = p + gst_p
    total_label = Label(w, text='Total Bill: Rs. %d'%total, font=('Arial',15))
    total_label.grid(row=5, column=2, padx=10, pady=10)

    b_1.config(state='disabled')
    c_1.config(state='disabled')
    c_2.config(state='disabled')
    ## Homework: Add more combo boxes here
    
def new():
    b_1.config(state='normal')
    
    c_1.config(state='normal')
    c_2.config(state='normal')
    ## Homework: Add more combo boxes here
    
    p_label.grid_forget()
    gst_label.grid_forget()
    total_label.grid_forget()
    
    
def exit_w():
    w.destroy()
    
L1 = Label(w, text = 'Navrachana Restaurant Menu', font=('Arial',30) )
L1.grid(padx=20, pady=10, row=0, column=0, columnspan=3)

L2 = Label(w, text = 'Select items from the following menu', font=('Arial',20) )
L2.grid(padx=10, pady=10, row=1, column=0, columnspan=3, sticky='W')

L3 = Label(w, text = '1. Soups:', font=('Arial',20))
L3.grid(padx=10, pady=10, row=2, column=0, sticky='W' )

o_1 = ['None','Clear Soup', 'Tomato Soup', 'Sweet Corn Soup', 'Hot & Sour Soup', 'Manchaw Soup']
c_1 = Combobox(w, value=o_1, font=('Arial',20))
c_1.grid(padx=10, pady=10, row=2, column=1)

L4 = Label(w, text = '2. Starters:', font=('Arial',20))
L4.grid(padx=10, pady=10, row=3, column=0, sticky='W' )

o_2 = ['None','Harabhara Kabab', 'Manchurian', 'Paneer Chilly', 'Veg 365', 'Paneer Tikka']
c_2 = Combobox(w, value=o_2, font=('Arial',20))
c_2.grid(padx=10, pady=10, row=3, column=1)

## Homework: Add more items and catagories here

b_1 = Button(w, text='Order', command = order, font=('Arial',20))
b_1.grid(row=4, column=0)

b_2 = Button(w, text='New', command = new, font=('Arial',20))
b_2.grid(row=4, column=1)

b_3 = Button(w, text='Exit', command = exit_w, font=('Arial',20))
b_3.grid(row=4, column=2)

w.mainloop()
