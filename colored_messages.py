import os
from colorama import Fore


def print_warning(txt):
    print(Fore.YELLOW + txt + Fore.WHITE)


def print_err(txt):
    print(Fore.RED + txt + Fore.WHITE)
    input()
    os._exit(1)
