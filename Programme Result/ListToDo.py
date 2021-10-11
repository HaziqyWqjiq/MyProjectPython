from tkinter import *
windows = Tk()

label= Label(windows,text = "TO-DO-LIST")
label.pack()

list = Listbox(windows,bg = 'yellow')
list.insert(1,'Make your homework')
list.pack()
windows.config(bg='black')
windows.geometry("300x300")
windows.title('LIST')
windows.mainloop()