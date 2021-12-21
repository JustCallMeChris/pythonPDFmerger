import os
import tkinter as tk
import tkinter.filedialog as fd
from PyPDF2 import PdfFileMerger

root = tk.Tk()
selectedFiles = fd.askopenfilenames(parent=root, title='Choose a pdf files')

pdfArray = [a for a in selectedFiles if a.endswith(".pdf")]

merger = PdfFileMerger()

for pdf in pdfArray:
    merger.append(open(pdf, 'rb'))

with open("result.pdf", "wb") as fout:
    merger.write(fout)
