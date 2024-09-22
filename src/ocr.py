from PIL import Image
# from translator import translate

import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/opt/tesseract/bin/tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'


# Simple image to string
def image_ocr_bengali(image_path: str):
    return pytesseract.image_to_string(Image.open(image_path), lang='ben')


def image_ocr_english(image_path: str):
    return pytesseract.image_to_string(Image.open(image_path), lang='eng')


lang_func_map = {'English': image_ocr_english, 'Bengali': image_ocr_bengali}


def image_ocr(image_path: str, language='eng'):
    return lang_func_map[language](image_path)

