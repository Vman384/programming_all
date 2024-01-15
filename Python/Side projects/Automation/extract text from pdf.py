import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from docx import Document



pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
poppler_path = r"D:\poppler-23.08.0\Library\bin"

images = convert_from_path(r"C:\Users\monic\OneDrive\programming\Python\Side projects\Automation\case study acuform.pdf",poppler_path=poppler_path)

text = ''

for image in images:
    text+= pytesseract.image_to_string(image)


document = Document()
document.add_paragraph(text)
document.save('test.docx')