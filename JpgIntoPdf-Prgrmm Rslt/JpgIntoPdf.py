from PIL import Image

path = 'K:\Programe(software)\JpgIntoPdf-Prgrmm Rslt\IMG_20200731_093044_190.jpg'
pdf = Image.open(path)
pdf.save('K:\Programe(software)\JpgIntoPdf-Prgrmm Rslt\IMG_20200731_093044_190.pdf')