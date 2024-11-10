import os
import imghdr
from PIL import Image
import pytesseract
from colorama import Fore, Back, Style
from pdf_to_jpg import convert_pdfs_to_images


pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'


def run_ocr():
    print("OCR ver. 1.1.0\n")
    check_pdfs()


def check_pdfs():
    pdfs = [f for f in os.listdir(
        ".") if os.path.isfile(f) if f.split('.')[1] == 'pdf']
    cnt = len(pdfs)

    if cnt > 0:
        convert_pdfs_to_images(pdfs)
    else:
        get_images()


def get_images():
    images = [f for f in os.listdir(
        ".") if os.path.isfile(f) if imghdr.what(f)]
    cnt = len(images)

    print(images)

    if cnt == 0:
        print_err("Brak pliku do odczytu OCR!\n")


def get_ocr(images, cnt):

    print(images)
    lp = input(f"Wybierz numer pliku (od 1 do {cnt}): ")
    try:
        img = images[int(lp)-1]
        print(img)
        if img.split('.')[1] == "pdf":
            convert_to_jpg()

        print("\nCzekaj, trwa oczyt pliku...\n")
        try:
            ocr_data = pytesseract.image_to_string(
                Image.open(img), lang='pol')
        except AttributeError as err:
            print_err(str(err))
    except:
        print_err("Błedna wrtość!!!")

    find_word = input('Wpisz słowo które chcesz wyszukać: ').lower()
    find_word_idx = [idx for idx in range(
        len(ocr_data)) if ocr_data.lower().startswith(find_word, idx)]

    out_data = ""

    idx_len = len(find_word_idx)

    if idx_len > 0:
        for index, data in enumerate(ocr_data):
            for fwi in find_word_idx:
                if (index == fwi):
                    out_data += Back.WHITE + Fore.BLACK
                if (index == fwi + len(find_word)):
                    out_data += Back.BLACK + Fore.WHITE
            out_data += data
        out_data += f'\nZnaleziono {
            idx_len} x frazę {Back.WHITE}{Fore.BLACK}{find_word}{Back.BLACK}{Fore.WHITE}'
    else:
        print(f'Nie znaleziono frazy "{find_word}"')

    print(out_data)
    input()
    with open("ocr.txt", "w") as f:
        f.write(ocr_data)


def print_err(txt):
    print(Fore.RED + txt + Fore.WHITE)
    input()
    os._exit(1)
