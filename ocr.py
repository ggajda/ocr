from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'


def get_ocr():
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
                    out_data += ' --> '
                if (index == fwi + len(find_word)):
                    out_data += ' <-- '
            out_data += data

    print(out_data)


def get_config():
    print(pytesseract.get_languages(config=''))
