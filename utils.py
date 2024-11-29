import sys
import os


class LabException(Exception):
    ...


def clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        print('\033[H\033[2J\033[3J', end='')
        # d    ^^^^^^^^^^^^^^^^^^^^   НЕ НОРМИСЫ!!!
