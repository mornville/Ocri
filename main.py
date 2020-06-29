try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from docx import Document
document = Document()


# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
ans =''
ans+= str(pytesseract.image_to_string(Image.open('a.jpg')))
print(ans)

document.add_paragraph(ans)
document.save('anss.docx')