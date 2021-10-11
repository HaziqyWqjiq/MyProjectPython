# text to pdf

# pip install fpdf / sudo pip3 install fpdf

from fpdf import FPDF

pdf= FPDF()
pdf.add_page()
pdf.set_font("Arial",size=20)
pdf.cell(50,100,txt="Hello EPELY ONE")
pdf.output("pdftext.pdf")
print("Done! You can check it now")