from tkinter import *
from tkinter.ttk import *
from time import strftime

root= Tk()
root.title("Clock")


lable= Label(root,font=("ds-digital",80),background ="black",foreground ="white")
label.pack(anchor='center')

def time():
    s= strftime('%H:%M:%S %p')
    label.config(text=s)
    label.after(1000, time)

time()

mainloop()