'''
Sowndharya Kangasabai
TASK-1:
Create a Digital Clock Interface using Python’s Tkinter Lib. and strftime method from time module.
'''
from tkinter import Tk
from tkinter import Label
import time

root = Tk()
root.title('Clock')

def present_time():
    display_time = time.strftime("%H:%M:%S %p")
    digi_clock.config(text=display_time)
    digi_clock.after(200, present_time)

digi_clock = Label(root, font=("arial",150), bg="black", fg="yellow")
digi_clock .pack()

present_time()
root.mainloop()
