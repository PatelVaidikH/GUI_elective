# This 3 lines creates a default Tkinter window
# from tkinter import Tk
# my_window = Tk()
# my_window.mainloop()

# Adding a title in window
# from tkinter import Tk
# my_window = Tk()
# my_window.title('Hello!')
# my_window.mainloop()

# Change the size of window
# from tkinter import Tk
# my_window = Tk()
# my_window.title('Different size window')
# H = input('Enter height:')
# W = input('Enter width:')
# a = input('Enter distance from left:')
# b = input('Enter distance from top:')
# my_window.geometry(f'{W}x{H}+{a}+{b}')
# my_window.mainloop()

# Making largest possible window
# from tkinter import Tk
# my_window = Tk()
# my_window.title('Large size window')

# print('Maximum width of screen is:',my_window.winfo_screenwidth())
# print('Maximum height of screen is:',my_window.winfo_screenheight())

# a = my_window.winfo_screenwidth()
# b = my_window.winfo_screenheight()

# my_window.geometry(f'{a}x{b}')
# my_window.mainloop()

# For a full screened window
# from tkinter import Tk
# my_win = Tk()
# my_win.title('Maximized window')
# my_win.state('zoomed')
# my_win.mainloop()

# For a central window
from tkinter import Tk
my_win = Tk()
my_win.title('Central window')

win_width = 500
win_height = 500

screen_width = my_win.winfo_screenwidth()
screen_height = my_win.winfo_screenheight()

center_x = int(screen_width/2 - win_width/2)
center_y = int(screen_height/2 - win_height/2)

my_win.geometry(f'{win_width}x{win_height}+{center_x}+{center_y}')

my_win.mainloop()












