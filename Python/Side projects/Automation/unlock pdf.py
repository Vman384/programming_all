import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from docx import Document

FILE_PATH = 'case study acuform.pdf'

pytesseract.pytesseract.tesseract_cmd = r