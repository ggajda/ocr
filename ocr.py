from PIL import Image
import pytesseract
from colorama import Fore
from colored_messages import print_err
from find_in_text import find_in_ocr


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def get_ocr(file):
    print(f"Trwa odczyt pliku {Fore.GREEN}{file}{Fore.WHITE}...\n")
    try:
        ocr_data = pytesseract.image_to_string(
            Image.open(file), lang='pol')

        with open("ocr.txt", "w") as f:
            f.write(ocr_data)
        find_in_ocr(ocr_data, file)
    except AttributeError as err:
        print_err(str(err))
