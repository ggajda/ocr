import os
from colorama import Fore, Back
from colored_messages import print_warning


def find_in_ocr(ocr_data, file):
    find_word = input(
        'Wpisz słowo które chcesz wyszukać lub "q" aby wyjść z programu: ').lower()
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
        out_data += f'{Fore.GREEN}\nZnaleziono w {file} {
            idx_len}x frazę {Back.WHITE}{Fore.BLACK}{find_word}{Back.BLACK}{Fore.WHITE}'
    else:
        print_warning(f'Nie znaleziono frazy "{
                      find_word}". Wpisz "r" aby powtórzyć wyszukiwanie')

    print(out_data)
    if find_word == "q":
        os._exit(0)
    elif find_word == "r":
        find_in_ocr(ocr_data, file)
    else:
        input()
