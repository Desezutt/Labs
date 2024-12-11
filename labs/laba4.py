from utils import LabException


header = '''   ┌─────────────────────────────────────┐
 1 │ y = { x + 2 * x * sin 3 * x, x <= π │
   │       cos x + 2,             x > π  │
   └─────────────────────────────────────┘

   ┌─────────────────────────────────────────────────────────────┐
 2 │ Программа определит какое из трёх вводимых чисел наибольшее │
   └─────────────────────────────────────────────────────────────┘

 3 [code]

- - - - - - - -
1-3 or b
'''


def exer1():
    pop = 0
    fio = input()
    for i in range(len(fio)):
        if fio[i] == fio[2]:
            i += 1
            pop = i

    fio2 = fio.split()[0]

    if 'а' in fio2:
        fio2.replace('а', '')
    elif 'о' in fio2:
        fio2.replace('о', '')

    print(fio2)
    print(len(fio))
    print(pop)


def exer2():
    print('e')


exers = {
    1: exer1,
    2: exer2,
}
