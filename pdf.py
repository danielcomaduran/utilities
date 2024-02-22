"""
    Functions to modify PDF files
"""
# Import libraries
import os
import fitz
import tkinter as tk
from PyPDF2 import PdfMerger
from tkinter import filedialog


def merge_pdfs():
    """
        Merge multiple PDF files stored in `inputs` folder into one

        Parameters
        ----------
        pdf_list : list
            List of PDF files to merge
    """

    pdf_list = [file for file in os.listdir('inputs') if file.endswith('.pdf')]

    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(fr"inputs\\{pdf}")
    merger.write(r'outputs\\merged.pdf')
    merger.close()

    print("Merged PDF files successfully")

#TODO: Fix this function
def sign_pdf(file_path:str, signature:str):
    """
        Sign a PDF file with the specified signature

        Parameters
        ----------
        pdf_file : str
            Path to the PDF file, must be inside the `inputs` folder

        signature : str
            Path to the signature image, must be inside the `inputs` folder
    """   
    
    root = tk.Tk()
    root.withdraw()
    file_path = fr'inputs\\{file_path}'
    file_path = filedialog.askopenfilename(title="Select PDF file")

    pdf_document = fitz.open(file_path)
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        annot = page.add_stamp(fr"inputs\\{signature}")
        page.insert_annot(annot)
    pdf_document.save(r"outputs\\signed_document.pdf")
    pdf_document.close()


# Example usage
sign_pdf("Cover letter.pdf", "Firma Karla 2.jpg")