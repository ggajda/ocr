from PIL import Image
import pytesseract
from colorama import Fore, Back, Style
import os


pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'


def get_image():
    files = [f for f in os.listdir(".") if os.path.isfile(f)]

    images = []

    for f in files:
        ext = f.split('.')[1]

        match ext:
            case "png":
                images.append(f)
            case "jpg":
                images.append(f)
            case "jpeg":
                images.append(f)
            case "gif":
                images.append(f)
            case "tif":
                images.append(f)

    return images


def get_ocr():

    img = get_image()
    cnt = len(img)

    def print_err(txt):
        print(Fore.RED + txt + Fore.WHITE)
        input()
        os._exit(1)

    if cnt == 0:
        print_err("Brak pliku obrazu!!!")
    elif cnt == 1:
        img = img[0]
    else:
        print(img)
        lp = input(f"Wybierz numer pliku (od 1 do {cnt}): ")
        try:
            img[int(lp)-1]
        except:
            print_err("Błedna wrtość!!!")

    ocr_data = pytesseract.image_to_string(
        Image.open('image.png'), lang='pol')
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

    print(out_data)
    input()
    with open("ocr.txt", "w") as f:
        f.write(ocr_data)
