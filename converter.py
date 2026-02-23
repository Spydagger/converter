import img2pdf
from fpdf import FPDF
from PIL import Image
import os

def images_to_pdf(image_paths, output_path):
    """
    Convert a list of image paths to a single PDF.
    """
    try:
        # img2pdf writes directly to a file or file-like object
        with open(output_path, "wb") as f:
            f.write(img2pdf.convert(image_paths))
        return True, "Successfully converted images to PDF."
    except Exception as e:
        return False, str(e)

def text_to_pdf(text_path, output_path):
    """
    Convert a text file to a PDF.
    """
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        with open(text_path, "r", encoding="utf-8") as f:
            for line in f:
                # encode/decode to handle utf-8 properly in basic fpdf if needed, 
                # but fpdf2 handles unicode better. 
                # We'll stick to basic implementation for now.
                pdf.cell(200, 10, txt=line, ln=1, align='L')
        
        pdf.output(output_path)
        return True, "Successfully converted text to PDF."
    except Exception as e:
        return False, str(e)
