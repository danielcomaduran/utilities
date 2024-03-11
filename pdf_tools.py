"""
    Functions to modify PDF files
"""
# Import libraries
import os
import fitz
import tkinter as tk
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from tkinter import filedialog
import fitz


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

def flip_pdf(file_path:str) -> str:
    """
    Flip a PDF file upside down

    Parameters
    ----------
    file_path : str
        Path to the PDF file

    Returns
    ----------
    str
        Path to the flipped PDF file
    """
    file_name = file_path.split("\\")[-1].split(".")[0]
    print(file_name)

    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)        
        pdf_writer = PdfWriter()

        # Loop through all the pages
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page.rotate(180)
            pdf_writer.add_page(page)

        # Define the output file path
        output_file_path = 'flipped_' + file_path

        # Write the output file
        with open(fr"outputs\\{file_name}_flipped.pdf", 'wb') as output_file:
            pdf_writer.write(output_file)

    return output_file_path


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
# sign_pdf("Cover letter.pdf", "Firma Karla 2.jpg")
flip_pdf(f"inputs\image2024-03-11-141912.pdf")

