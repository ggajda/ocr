from PIL import Image
import pytesseract
from colorama import Fore
from colored_messages import print_err
from find_in_text import find_in_ocr


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def write_to_file(ocr_data):
    try:
        with open("ocr.txt", "a") as f:
            f.write(ocr_data)
    except Exception as e:
        _ = e


def get_ocr(file):
    print(f"Trwa odczyt {Fore.GREEN}{file}{Fore.WHITE}...")
    try:
        ocr_data = pytesseract.image_to_string(
            Image.open(file), lang='pol')

        write_to_file(ocr_data)
    except AttributeError as err:
        print_err(str(err))
