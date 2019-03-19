import sys


def f(k): # k - параметр бинарного поиска
          # взят из задачаи с находждением единичного столбца в матрице
    '''
        Формула из фото в приложении
    '''

    ...

def run_ship(start, fin, wind): # бинарный поиск
    '''
    Область поиска от 0 до 2*10^14
    Перебераем k. В бинарном поиске.
    f(k) должен вернуть ноль. тогда возвращаем k как ответ.
    Если левая и правая часть станет одинаковой то возвращаем -1
    возвращаем  k если f(k) == 0 и левая и правая часть не одинаковы.
    '''
    ...




if len(sys.argv) > 1 and sys.argv[1] == 'test':
    tests = [
        [(0, 0), (4, 6), 'UUU', [5]],
        [(3, 0), (0, 0), 'UDD', [4]],
        [(0, 3), (0, 0), 'UUD', [6]],
        [(0, 3), (0, 0), 'UDD', [3]],
        [(0, 0), (0, 1), 'L', [-1]],
    ]
    for t in tests:
        print(run_ship(...))

else:
    first_line = input()
    start = tuple(map(int, first_line.split()))
    second_line = input()
    fin = tuple(map(int, second_line.split()))
    _ = input()
    fourth = input()
    coords = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    wind = (coords[i] for i in fourth)

