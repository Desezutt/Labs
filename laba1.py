from math import sin, cos
from utils import LabException


header = '''   ┌─────────────────────────────────────────────────────┐
 1 │ a = cos^4 * x + sin^2 * y + 1/4 * sin^2 * 2 * x - 1 │
   └─────────────────────────────────────────────────────┘

   ┌──────────────────────────────────────────────────┐
 2 │ Вывод уравнения прямой, проходящей через 2 точки │
   └──────────────────────────────────────────────────┘

1-2 or b
'''


def exer1():
    print('a = cos^4 * x + sin^2 * y + 1/4 * sin^2 * 2 * x - 1\n'
          '───────────────────────────────────────────────────')
    la11 = input('x > ')
    if not la11.replace('.', '', 1).isdigit():
        raise LabException('invalid value')
    la11 = float(la11)
    la12 = input('y > ')
    if not la12.replace('.', '', 1).isdigit():
        raise LabException('invalid value')
    la12 = float(la12)
    la1fin = pow(cos(la11), 4) + pow(sin(la12), 2) + 1 / 4 * pow(sin(2 * la11), 2) - 1
    print(f'\n[+] {la1fin}')
    print('────────────────────────────────────────────────────')


def exer2():
    print('Вывод уравнения прямой, проходящей через 2 точки (введите '
          'координаты)')
    print('──────────────────────────────────────────────────────────')
    x1 = input('x1 > ')
    if not x1.replace('.', '', 1).isdigit():
        raise LabException('invalid value')
    x1 = float(x1)
    y1 = (input('y1 > '))
    if not y1.replace('.', '', 1).isdigit():
        raise LabException('invalid value')
    y1 = float(y1)
    x2 = (input('\nx2 > '))
    if not x2.replace('.', '', 1).isdigit():
        raise LabException('invalid value')
    x2 = float(x2)
    y2 = (input('y2 > '))
    if not y2.replace('.', '', 1).isdigit():
        raise LabException('invalid value')
    y2 = float(y2)
    if x1 == x2:
        print(f'\nx = {x1}')
    else:
        koef = (y2 - y1) / (x2 - x1)
        svch = y1 - koef * x1
        print(f'\ny = {koef}x + {svch}')
    print('──────────────────────────────────────────────────')
#d блять...  что я написал -_-
#a менавіта..


exers = {
    1: exer1,
    2: exer2,
}
