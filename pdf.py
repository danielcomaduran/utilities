"""
    Functions to modify PDF files
"""
# Import libraries
import os
from PyPDF2 import PdfMerger


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


# Example usage
merge_pdfs()