import os
import sys
from datetime import datetime
from math import *
from time import sleep


def exitlol():
    print('[LABS] goodbye :>')
    quit()


def banner():
    print('\n██╗       ███╗  ██████╗  ██████╗  '
          '\n██║      ██╝██╗ ██╔═╝██╗██╔════╝  '
          '\n██║     ██╝  ██╗██████╔╝  ███╗    '
          '\n██║     ███████║██╔═╝██╗     ██╗  ''       ''v0.14.4'
          '\n███████╗██╔══██║██████╔╝██████╔╝  '
          '\n╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝   '
          '\n[+]', datetime.now(),
          '\n[+]', sys.platform, 'OS'
          '\n[+]', 'labs =', 20,
          '\n[+]', 'by den :3'
                   '\n---------------------------------'
          )


def lads():
    print('|00|  |> exit'
          '\n|01|..|> линейные программы и математические функции'
          '\n|02|::|> ветвящиеся алгоритмы и программы'
          '\n|03|  |> '
          '\n|04|  |>'
          '\n|05|  |>'
          '\n|06|  |> '
          '\n|07|  |> '
          '\n|08|  |> '
          '\n|09|  |> '
          '\n|10|  |> '
          '\n|11|  |> '
          '\n|12|  |> '
          '\n|13|  |> '
          '\n|14|  |> '
          '\n|15|  |> '
          '\n|16|  |> '
          '\n|17|  |> '
          '\n|18|  |> '
          '\n|19|  |> '
          '\n|20|  |> '
          )


numlab = 1984


def main():
    os.system('cls||clear')
    banner()
    lads()
    labstart()


def labstart():
    global numlab
    numlab = (input('\nselect number\n> '))
    if (numlab == 'c') or (numlab == 'clear'):
        main()
    if numlab.isdigit():
        numlab = int(numlab)
        if numlab in functions:
            os.system('cls||clear')
            functions[numlab]()
    else:
        print('[-] invalid value')
        sleep(0.5)
        main()


def backmain():
    print('back/restart = b/r')
    backmainper = input('> ')
    if backmainper == 'r':
        os.system('cls||clear')
        functions[numlab]()
    elif backmainper == 'b':
        main()
    else:
        print('[-] invalid value\n')
        backmain()


def error():
    print('[-] invalid value')
    sleep(0.5)
    functions[numlab]()


def laba1():
    os.system('clr||clear')
    unlab = input('   |---------------------------------------------------|\n'
                  ' 1 |a = cos^4 * x + sin^2 * y + 1/4 * sin^2 * 2 * x - 1|\n'
                  '   |---------------------------------------------------|\n'
                  '                                                       \n'
                  '   |------------------------------------------------|\n'
                  ' 2 |Вывод уравнения прямой, проходящей через 2 точки|\n'
                  '   |------------------------------------------------|\n'
                  '\n'
                  '1-2 or b\n'
                  '> ')
    if unlab == '1':
        laba1_1()
    elif unlab == '2':
        laba1_2()
    elif unlab == 'b':
        os.system('cls||clear')
        main()
    else:
        error()


def laba1_1():
    global numlab
    numlab = 1.1
    os.system('cls||clear')
    print('a = cos^4 * x + sin^2 * y + 1/4 * sin^2 * 2 * x - 1\n----------------------------------------------------')
    la11 = (input('число 1 (x)\n> '))
    if la11.replace('.', '', 1).isdigit():
        la11 = float(la11)
        la12 = (input('\nчисло 2 (y)\n> '))
        if la12.replace('.', '', 1).isdigit():
            la12 = float(la12)
            la1fin = pow(cos(la11), 4) + pow(sin(la12), 2) + 1 / 4 * pow(sin(2 * la11), 2) - 1
            print('\n[+]', la1fin)
            print('----------------------------------------------------')
            backmain()
        else:
            error()
    else:
        error()


def laba1_2():
    global numlab
    numlab = 1.2
    os.system('cls||clear')
    print('Вывод уравнения прямой, проходящей через 2 точки (введите '
          'координаты)\n------------------------------------------------')
    x1 = (input('x1 > '))
    if x1.replace('.', '', 1).isdigit():
        x1 = float(x1)
        y1 = (input('y1 > '))
        if y1.replace('.', '', 1).isdigit():
            y1 = float(y1)
            x2 = (input('\nx2 > '))
            if x2.replace('.', '', 1).isdigit():
                x2 = float(x2)
                y2 = (input('y2 > '))
                if y2.replace('.', '', 1).isdigit():
                    y2 = float(y2)
                    if x1 == x2:
                        print(f'\nx = {x1}')
                        print('--------------------------------------------------')
                        backmain()
                    else:
                        koef = (y2 - y1) / (x2 - x1)
                        svch = y1 - koef * x1
                        print(f'\ny = {koef}x + {svch}')
                        print('--------------------------------------------------')
                        backmain()
                else:
                    error()
            else:
                error()
        else:
            error()
    else:
        error()
# блять...  что я написал -_-


def laba2():
    os.system('cls||clear')
    unlab = input('   |-----------------------------------|\n'
                  ' 1 |y = { x + 2 * x * sin 3 * x, x <= π|\n'
                  '   |      cos x + 2,             x > π |\n'
                  '   |-----------------------------------|\n'
                  '                                                        \n'
                  '   |-----------------------------------------------------------|   \n'
                  ' 2 |программа определит какое из трёх вводимых чисел наибольшее|   \n'
                  '   |-----------------------------------------------------------|   \n'
                  '                                                        \n'
                  '   |---------------------------------------------------|\n'
                  ' 3 |                                                |\n'
                  '   |---------------------------------------------------|\n'
                  '                                                        \n'
                  '   |---------------------------------------------------|\n'
                  ' 4 |                                           |\n'
                  '   |---------------------------------------------------|\n'
                  '                                                        \n'
                  '1-4 or b\n'
                  '> ')
    if unlab == '1':
        laba2_1()
    elif unlab == '2':
        laba2_2()
    elif unlab == '3':
        laba2_3()
    elif unlab == '4':
        laba2_4()
    elif unlab == 'b':
        os.system('cls||clear')
        main()
    else:
        error()


def laba2_1():
    global numlab
    numlab = 2.1
    os.system('cls||clear')
    print('y = { x + 2 * x * sin 3 * x, x <= π\n'
          '      cos x + 2,             x > π'
          '\n--------------------------------------')
    x = (input('x > '))
    if x.replace('.', '', 1).isdigit():
        x = float(x)
        if x <= pi:
            y = x + 2 * x * sin(3 * x)
        else:
            y = cos(x) + 2

        print(f"\nx = {x}\ny = {y}\n--------------------------------------")
        backmain()
    else:
        error()


def laba2_2():
    global numlab
    numlab = 2.2
    os.system('cls||clear')
    print('программа определит какое из трёх вводимых чисел наибольшее'
          '\n-----------------------------------------------------------')
    x1 = (input("[1]\n> "))
    if x1.isdigit():
        x1 = int(x1)
        x2 = (input("[2]\n> "))
        if x2.isdigit():
            x2 = int(x2)
            x3 = (input("[3]\n> "))
            if x3.isdigit():
                x3 = int(x3)

                if (x1 > x2) and (x1 > x3):
                    print(x1, ">", x2, ",", x3)
                elif (x2 > x1) and (x2 > x3):
                    print(x2, ">", x1, ",", x3)
                elif (x3 > x1) and (x3 > x2):
                    print(x3, ">", x1, ",", x2)

                print('-----------------------------------------------------------')
                backmain()

            else:
                error()
        else:
            error()
    else:
        error()
# не ну...


def laba2_3():
    global numlab
    numlab = 2.3
    a = 0
    print('вычисляет сумму четных чисел на указаном отрезке\n'
          '-------------------------------------------------')
    x1 = (input("от\n> "))
    if x1.isdigit():
        x1 = int(x1)
        x2 = (input("до\n> "))
        if x2.isdigit():
            x2 = int(x2)
            if x1 > x2:
                error()
            for i in range(x1, x2):
                if i % 2 == 0:
                    a += i
            print(f'\n[+] {a}\n'
                  '-------------------------------------------------')
            backmain()
        else:
            error()
    else:
        error()


def laba2_4():
    global numlab
    numlab = 2.4
    fb1 = 1
    fb2 = 1

    x = (input("введите число"))
    if x.isdigit():
        x = int(x)
        i = 0
        while i < x:
            fbs = fb1 + fb2
            fb1 = fb2
            print(fb2)
            fb2 = fbs

            i = i + 1
        backmain()
    else:
        error()


functions = {
    0: exitlol,
    1: laba1,
    1.1: laba1_1,
    1.2: laba1_2,
    2: laba2,
    2.1: laba2_1,
    2.2: laba2_2,
}

if __name__ == "__main__":
    main()
