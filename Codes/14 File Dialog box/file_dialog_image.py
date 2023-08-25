from tkinter import Tk, Label, Button, filedialog
from PIL import ImageTk, Image

w = Tk()
w.title('Image viewver')
w.state('zoomed')
w.iconbitmap('globe.ico')

def openimage():
    w.filename = filedialog.askopenfilename ( initialdir = "C:/Users/Shardav.Bhatt/Documents",
                                              title = 'Select an image',
                                              filetypes = ( ("PNG Files","*.png"), ("JPG Files","*.jpg")) )

    L1 = Label(w, text=w.filename, font=('Arial',15))
    L1.pack()

    global my_image
    my_image = ImageTk.PhotoImage(Image.open(w.filename))

    L2 = Label(w, image=my_image)
    L2.pack()
    
L = Label(w, text='Image viewer', font=('Arial',20))
L.pack()

B = Button(w, text='Open image', font=('Arial',15), command = openimage)
B.pack()

## Homework: Add buttons NEW and CLOSE IMAGE to close exisiting image and open another image

w.mainloop()
