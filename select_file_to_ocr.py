import os
import imghdr
from pdf_to_jpg import convert_pdfs_to_images
from colored_messages import print_warning, print_err
from ocr import get_ocr


def run_ocr():
    print("OCR ver. 1.1.0\n")
    get_images()


def get_images():
    files = [f for f in os.listdir(
        ".") if os.path.isfile(f) if imghdr.what(f) or f.split('.')[1] == "pdf"]
    cnt = len(files)

    if cnt == 0:
        print_err("Brak pliku do odczytu OCR!\n")
    else:
        set_image(files, cnt)


def set_image(files, cnt):
    print(files)
    file_number = input(f'Wybierz numer pliku (od 1 do {
        cnt}): lub "q" aby wyjść z programu: ')
    if file_number == "q":
        os._exit(0)

    try:
        file = files[int(file_number)-1]
    except:
        print_warning("Zostały wprowadzone nieprawidłowe dane!\n")
        set_image(files, cnt)

    if file.split('.')[1] == "pdf":
        convert_pdfs_to_images(file)
    else:
        get_ocr(file)
