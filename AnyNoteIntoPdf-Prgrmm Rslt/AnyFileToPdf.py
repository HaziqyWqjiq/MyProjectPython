#import library
from fpdf import FPDF
from tkinter import*
from tkinter import filedialog
#converting textfile into pdf
def convert():
 #creating variable of PDF
 pdf = FPDF()
 #Adding pages
 pdf.add_page()
 #setting fon family and Textsize
 pdf.set_font("Arial", size=15)
 #open file in read mode
 f = open(fname, "r")
 #reading file content
 for x in f:
    #placing file content into pdf
    pdf.cell(200, 10, txt=x, ln=1, align='L')
 #generating a complete pdf file with name Convert.pdf
 pdf.output("Convert.pdf")
 #showing success message
 msgForGenerate.set("Convert.pdf is generated successfully")
#uploading Textfile
def UploadAction():
    #uploading file
    filename = filedialog.askopenfilename(filetypes =[('Text Files', '*.txt')])
    #showing message for uploaded file
    msgForUpload.set("Uploaded:"+filename)
    #declaring global variable
    global fname
    #passing uploaded filename into fname
    fname=filename
#creating GUI for Converter
root =Tk()
#setting window height and width
root.geometry("600x200")
#setting window background color
root["bg"]="#20325B"
#setting title of window
root.title("Krazy:Text File to PDF Converter")
#creating variable for messages
global msgForUpload
global msgForGenerate
msgForUpload=StringVar()
msgForGenerate=StringVar()
#label for uploading message
Label(root,text="Hello",textvariable=msgForUpload,font="Arial 12",bg="#20325B",fg="white").place(x=80,y=30)
#button for upload file
Button(root, text='Open', command=UploadAction,font="Arial 12 bold",width="10",bg="orange").place(x=80,y=70)
#button for convert
Button(root,text="Convert",font="Arial 12 bold",width="10",command=convert,bg="orange").place(x=350,y=70)
#label for generated/success message
Label(root,text="Hello",textvariable=msgForGenerate,font="Arial 12",bg="#20325B",fg="white").place(x=80,y=120)
root.mainloop()