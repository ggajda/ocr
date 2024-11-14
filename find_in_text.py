from os import name, system, _exit
from colorama import Fore, Back
from colored_messages import print_warning


def clear_screen():
    if name == "nt":
        system('cls')
    else:
        system('clear')


def find_in_ocr():
    ocr_data = None
    with open("ocr.txt", "r") as f:
        ocr_data = f.read()

    find_word = input(
        f'Wpisz słowo które chcesz wyszukać lub "{Fore.YELLOW}q{Fore.WHITE}" aby wyjść z programu: ').lower()
    clear_screen()

    if find_word == "q":
        _exit(0)

    find_word_idx = [idx for idx in range(
        len(ocr_data)) if ocr_data.lower().startswith(find_word, idx)]

    out_data = ""

    idx_len = len(find_word_idx)

    if idx_len > 0:
        for index, data in enumerate(ocr_data):
            for f_index, fwi in enumerate(find_word_idx):
                if (index == fwi):
                    out_data += f'{Back.YELLOW}{Fore.BLACK}({f_index+1})'
                if (index == fwi + len(find_word)):
                    out_data += Back.BLACK + Fore.WHITE
            out_data += data
        out_data += f'{Fore.GREEN}\nZnaleziono {
            idx_len}x frazę {Back.YELLOW}{Fore.BLACK}{find_word}{Back.BLACK}{Fore.WHITE}'
    else:
        print_warning(f'Nie znaleziono frazy "{find_word}"')

    print(out_data)
    find_in_ocr()
