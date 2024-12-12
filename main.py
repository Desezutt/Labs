#!/usr/bin/env python

import colorama
import sys
from datetime import datetime
from time import sleep
from utils import clear, LabException
import subprocess
import os

from labs import labs_list


def get_commit_count() -> int:
    result = subprocess.run(['git', 'rev-list', '--count', 'HEAD'], capture_output=True, text=True)
    return int(result.stdout.strip())


gitcom: int = get_commit_count()
keylabs: int = len(labs_list)
version: int = gitcom // 100


banner = f'''██╗       ███╗  ██████╗  ██████╗
██║      ██╝██╗ ██╔═╝██╗███╔═══╝
██║     ██╝  ██╗██████╔╝  ███╗
██║     ███████║██╔═╝██╗    ███╗         v{version}.{keylabs}.{gitcom}
███████╗██╔══██║██████╔╝██████╔╝
╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝
[+] {datetime.now()}
[+] {sys.platform} OS
[+] by Den and Alis :3
─────────────────────────────────
00 |> [exit]
01 |> линейные программы и математические функции
02 |> ветвящиеся алгоритмы
03 |> циклы с известным и неизвестным числом повторений
*04 |> обработка строк
*05 |> списки
*06 |> многомерные списки
*07 |> кортежи и множества
*08 |> работы со словари
*09 |> модули и функции
*10 |> файлы и каталоги
*11 |> разработка и проектирование
*12 |> создание классов и экземпляров классов
*13 |> статические и абстрактные методы
*14 |> наследования классов
*15 |> свойства классов
*16 |> декораторы методов
*17 |> создание изображений
*18 |> обработка изображений и получение информации об изображении
*19 |> бибиотека pillow
*20 |> взаимодействие с URL - адресами
*21 |> получение данных по протоколу http
*22 |> модуль urllib.request
*23 |> фреймворк kivy
*24 |> виджеты image
*25 |> разметка boxlayout и floatlayout
*26 |> разметка gridlayout
*27 |> события
*28 |> apk - приложения
*29 |> ios - приложения
*30 |> exe - приложения
*31 |> macos - приложения
99 |> [code]
'''


def main() -> None:
    if os_platform() != 'bat':
        clear()
        print('[LABS] download \'bat\' for syntax highlighting')
        sleep(7)
    while True:
        clear()
        print(banner)
        lab_num = input('select lab\n> ')
        if not lab_num.isdigit():
            print('[-] invalid value')
            sleep(1)
            continue
        lab_num = int(lab_num)
        if lab_num == 0:
            break
        elif lab_num == 99:
            os.system(f'{os_platform()} main.py')
            print(banner)
        elif lab_num in labs_list:
            run_lab(lab_num)
        else:
            print('[-] invalid value')
            sleep(1)
            continue
    clear()
    print('[LABS] goodbye <3')


def run_lab(lab_num: int) -> None:
    while True:
        clear()
        print(labs_list[lab_num].header, end='')
        exer_num = input('> ')
        if exer_num == 'b':
            return
        elif not exer_num.isnumeric():
            print('[-] invalid value')
            sleep(1)
            continue
        elif int(exer_num) == len(labs_list[lab_num].exers) + 1:
            os.system(f'{os_platform()} labs/laba{lab_num}.py')
            print(labs_list[lab_num].header, end='')
        elif int(exer_num) in labs_list[lab_num].exers:
            clear()
            run_exer(lab_num, int(exer_num))
            return
        else:
            print('[-] invalid value')
            sleep(1)
            continue


def run_exer(lab_num: int, exer_num: int) -> None:
    while True:
        try:
            labs_list[lab_num].exers[exer_num]()
        except LabException as exception:
            print(f'[-] {' '.join(exception.args)}')
            sleep(1)
            continue
        if not ask_run_again():
            return


def os_platform() -> str:
    if sys.platform == 'win32':
        return 'notepad'
    else:
        result = subprocess.run(['which', 'bat']).returncode
        if result == 0:
            return 'bat'
        else:
            return 'less'


def ask_run_again() -> bool:
    while True:
        print('back/restart = b/r')
        match input('> '):
            case 'r':
                return True
            case 'b':
                return False
            case _:
                print('[-] invalid value\n')
                sleep(1)
                continue


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print('[LABS] goodbye <3')
