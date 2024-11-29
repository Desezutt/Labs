from utils import LabException

header = '''   ┌───────────────────────────────┐
 1 │ Сумма четных чисел на отрезке │
   └───────────────────────────────┘

   ┌─────────────────────────┐
 2 │ Элементы ряда Фибоначчи │
   └─────────────────────────┘

 3 [code]

- - - - - - - -
1-2 or b
'''


def exer1():
    a = 0
    print('вычисляет сумму четных чисел на указаном отрезке\n'
          '─────────────────────────────────────────────────')
    x1 = (input('от\n> '))
    if not x1.isdigit():
        raise LabException('invalid value')
    x1 = int(x1)
    x2 = (input('до\n> '))
    if not x2.isdigit():
        raise LabException('invalid value')
    x2 = int(x2)
    if x1 > x2:
        raise LabException('invalid value')
    for i in range(x1, x2):
        if i % 2 == 0:
            a += i
    print(f'\n[+] {a}\n'
          '─────────────────────────────────────────────────')


def exer2():
    print('элементы ряда Фибоначчи\n'
          '────────────────────────')
    x = input('count\n> ')
    if not x.isdigit():
        raise LabException('invalid value')
    x = int(x)
    print()

    fib = [1, 1]
    while len(fib) < x:
        fib.append(fib[-2] + fib[-1])
    for i in range(x):
        print(f'[+] {fib[i]}')
    print('────────────────────────')


exers = {
    1: exer1,
    2: exer2,
}
