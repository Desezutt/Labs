from math import sin, cos, pi
from utils import clear, LabException


header = '''
   ┌──────────────────────────────────────────────────┐
 1 |y = { x + 2 * x * sin 3 * x, x <= π|
   |      cos x + 2,             x > π |
   └──────────────────────────────────────────────────┘

   ┌──────────────────────────────────────────────────┐
 2 |программа определит какое из трёх вводимых чисел наибольшее|
   └──────────────────────────────────────────────────┘

   ┌──────────────────────────────────────────────────┐
 3 |                                                |
   └──────────────────────────────────────────────────┘

   ┌──────────────────────────────────────────────────┐
 4 |                                           |
   └──────────────────────────────────────────────────┘

1-4 or b
'''


def exer1():
    clear()
    print('y = { x + 2 * x * sin 3 * x, x <= π\n'
          '      cos x + 2,             x > π\n'
          '--------------------------------------')
    x = input('x > ')
    if not x.replace('.', '', 1).isdigit():
        raise LabException('invalid value')
    x = float(x)
    if x <= pi:
        y = x + 2 * x * sin(3 * x)
    else:
        y = cos(x) + 2
    print(f'\nx = {x}\ny = {y}\n--------------------------------------')


def exer2():
    clear()
    print('программа определит какое из трёх вводимых чисел наибольшее\n'
          '-----------------------------------------------------------')
    x1 = input("[1]\n> ")
    if not x1.isdigit():
        raise LabException('invalid value')
    x1 = int(x1)
    x2 = input("[2]\n> ")
    if not x2.isdigit():
        raise LabException('invalid value')
    x2 = int(x2)
    x3 = (input("[3]\n> "))
    if not x3.isdigit():
        raise LabException('invalid value')
    x3 = int(x3)

    if (x1 > x2) and (x1 > x3):
        print(x1, ">", x2, ",", x3)
    elif (x2 > x1) and (x2 > x3):
        print(x2, ">", x1, ",", x3)
    elif (x3 > x1) and (x3 > x2):
        print(x3, ">", x1, ",", x2)
    print('-----------------------------------------------------------')
# не ну...


def exer3():
    a = 0
    print('вычисляет сумму четных чисел на указаном отрезке\n'
          '-------------------------------------------------')
    x1 = (input("от\n> "))
    if not x1.isdigit():
        raise LabException('invalid value')
    x1 = int(x1)
    x2 = (input("до\n> "))
    if not x2.isdigit():
        raise LabException('invalid value')
    x2 = int(x2)
    if x1 > x2:
        raise LabException('invalid value')
    for i in range(x1, x2):
        if i % 2 == 0:
            a += i
    print(f'\n[+] {a}\n'
          '-------------------------------------------------')


def exer4():
    fb1 = 1
    fb2 = 1

    x = input("введите число")
    if not x.isdigit():
        raise LabException('invalid value')
    x = int(x)
    i = 0
    while i < x:
        fbs = fb1 + fb2
        fb1 = fb2
        print(fb2)
        fb2 = fbs

        i = i + 1


exers = {
    1: exer1,
    2: exer2,
    3: exer3,
    4: exer4,
}
