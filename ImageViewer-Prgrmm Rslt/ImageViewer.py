from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Image viewer By Haziq")
root.resizable(0, 0)
# create frame
frame=Frame(root, width=600, height=500, bg='white', relief=GROOVE, bd=2)
frame.pack(padx=10, pady=10)
# create thumbanials of all images  
img1 = Image.open('IMG_20200731_092812_464.jpg')
img1.thumbnail((550, 450))
img2 = Image.open('IMG_20200731_093044_190.jpg')
img2.thumbnail((550, 450))
img3 = Image.open('TamanMerak.jpg')
img3.thumbnail((550, 450))
# open images to use with labels
image1 = ImageTk.PhotoImage(img1)
image2 = ImageTk.PhotoImage(img2)
image3 = ImageTk.PhotoImage(img3)
# create list of images
images = [image1, image2, image3]
# configure the image to the Label in frame
i = 0
image_label = Label(frame, image=images[i])
image_label.pack()
# create functions to display
# previous an next images
def previous():
    global i
    i = i - 1
    try:
        image_label.config(image=images[i])
    except:
        i = 0
        previous()
def next():
    global i
    i = i + 1
    try:
        image_label.config(image=images[i])
    except:
        i = -1
        next()
# create buttons    
btn1 = Button(root, text="Previous", bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=previous)
btn1.pack(side=LEFT, padx=60, pady=5)
btn2 = Button(root, text="Next", width=8, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=next)
btn2.pack(side=LEFT, padx=60, pady=5)
btn3 = Button(root, text="Exit", width=8, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=root.destroy)
btn3.pack(side=LEFT, padx=60, pady=5)
root.mainloop()