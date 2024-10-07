import pytesseract
import numpy as np
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


def extract_text(image_path) -> str:
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)

    # remove symbols and split lines for better display

    characters_to_remove = "!()@—*“>+-/,'|£#%$&^_~"
    text = ''.join(char for char in text if char not in characters_to_remove)
    text_lines = text.split("\n")
    return text_lines


# test
"""
image_path = "./app/static/uploads/215831_1296528.jpg"
extracted_text = extract_text(image_path)
print(f"Extracted text: \n {extracted_text}")
"""
