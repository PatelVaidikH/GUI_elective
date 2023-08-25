
from tkinter import Tk, filedialog

w = Tk()
w.title('File dialog box')
w.geometry('500x500')
w.iconbitmap('bird.ico')

filedialog.askopenfilename (initialdir = "C:/Users/Shardav.Bhatt/Pictures",
                            title = 'Open an image file',
                            filetypes = (("PNG Files","*.png"), ("JPG Files","*.jpg"), ("All files","*.*")))
                            

w.mainloop()
