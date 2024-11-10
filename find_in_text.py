from colorama import Fore, Back
from colored_messages import print_warning


def find_in_ocr():
    f = open('ocr.txt', 'r')
    ocr_data = f.read()

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
            idx_len}x frazę {Back.WHITE}{Fore.BLACK}{find_word}{Back.BLACK}{Fore.WHITE}'
    else:
        print_warning(f'Nie znaleziono frazy "{find_word}"')

    print(out_data)
    input()
    with open("ocr_out.txt", "w") as f:
        f.write(ocr_data)
