from tkinter import *
from tkinter import messagebox

root =Tk()
root.geometry("400x200")
def msg():
    messagebox.showwarning("Alert Box","Hey, you just got an error message.......finish your homework now!!")
but= Button(root,text="Press Here To Show Up Alert Button",command=msg)
but.place(x=100,y=100)
root.mainloop()
