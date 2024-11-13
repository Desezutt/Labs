#!/usr/bin/env python
import sys
from datetime import datetime
from time import sleep
from utils import clear, LabException

import laba1
import laba2


banner = f'''██╗       ███╗  ██████╗  ██████╗
██║      ██╝██╗ ██╔═╝██╗██╔════╝
██║     ██╝  ██╗██████╔╝  ███╗
██║     ███████║██╔═╝██╗     ██╗         v0.14.4
███████╗██╔══██║██████╔╝██████╔╝
╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝
[+] {datetime.now()}
[+] {sys.platform} OS
[+] labs = 20
[+] by den :3
─────────────────────────────────

00│   |> exit
01│.. |> линейные программы и математические функции
02│:: |> ветвящиеся алгоритмы и программы
03│   |>
04│   |>
05│   |>
06│   |>
07│   |>
08│   |>
09│   |>
10│   |>
11│   |>
12│   |>
13│   |>
14│   |>
15│   |>
16│   |>
17│   |>
18│   |>
19│   |>
20│   |>
'''


def main():
    while True:
        clear()
        print(banner)
        lab_num = input('select lab > ')
        if not lab_num.isdigit():
            print('[-] invalid value')
            sleep(1)
            continue
        lab_num = int(lab_num)
        if lab_num == 0:
            break
        elif lab_num in labs:
            run_lab(lab_num)
        else:
            print('[-] invalid value')
            sleep(1)
            continue
    print('[LABS] goodbye :>')


def run_lab(lab_num: int):
    while True:
        clear()
        print(labs[lab_num].header, end='')
        exer_num = input('> ')
        if exer_num == 'b':
            return
        elif not exer_num.isnumeric():
            print('[-] invalid value')
            sleep(1)
            continue
        elif int(exer_num) in labs[lab_num].exers:
            run_exer(lab_num, int(exer_num))
            return
        else:
            print('[-] invalid value')
            sleep(1)
            continue


def run_exer(lab_num: int, exer_num: int):
    while True:
        try:
            labs[lab_num].exers[exer_num]()
        except LabException as exception:
            print(f'[-] {' '.join(exception.args)}')
            sleep(1)
            continue
        if not ask_run_again():
            return


def ask_run_again() -> bool:
    while True:
        print('back/restart = b/r')
        match input('> '):
            case 'r':
                clear()
                return True
            case 'b':
                return False
            case _:
                print('[-] invalid value\n')
                sleep(1)
                continue


labs = {
    1: laba1,
    2: laba2,
}


if __name__ == "__main__":
    main()
