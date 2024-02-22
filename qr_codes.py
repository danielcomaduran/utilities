"""
    Functions to generate and save QR codes
"""

# Import libraries
import pyqrcode

def generate_qr_svg(string:str, color:str):
    """ 
        Generate and save a QR code as an SVG file with the specified color

        Parameters
        ----------
        string : str
    """
    # Create a QR code object from the string
    qr = pyqrcode.create(string)
    
    # Save the QR code as an svg file with the specified color
    qr.svg(r"outputs\\qr.svg", scale=8, module_color=color)
    print("The QR code is saved successfully")
    

# Example usage
generate_qr_svg("https://forms.office.com/r/jTnqgz1x4E", "#FFFFFF")
