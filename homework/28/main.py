import sys


def count_wind(k, wind):
    n = len(wind)
    full_x = sum(x for (x, y) in wind)
    full_y = sum(y for (x, y) in wind)
    full = k // n

    part = k % n
    part_x = sum(x for (x, y) in wind[:part])
    part_y = sum(y for (x, y) in wind[:part])

    r = ((full * full_x + part_x), (full * full_y + part_y))
    # print(r)
    return r


def f(k, start, fin, wind):  # k - параметр бинарного поиска
    '''
        Формула из фото в приложении
    '''
    vector_sum = count_wind(k, wind)
    x_i = start[0] + vector_sum[0] - fin[0]
    y_i = start[1] + vector_sum[1] - fin[1]
    #print((abs(x_i) + abs(y_i)) - k, k)
    return (abs(x_i) + abs(y_i)) <= k


def run_ship(start, fin, wind):  # бинарный поиск
    '''
    Область поиска от 0 до 2*10^14
    Перебераем k. В бинарном поиске.
    '''

    coords = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    wind = [coords[i] for i in wind]

    left = 1
    right = 2*10**15+1
    while left != right:
        middle = (left + right) // 2
        # print(middle)
        # middle is k
        if f(middle, start, fin, wind) < 1:
            left = middle + 1
        else:
            right = middle
    if left == 2*10**15+1:
        return -1
    return left


if len(sys.argv) > 1 and sys.argv[1] == 'test':
    tests = [
        #[(0, 0), (4, 6), 'UUU', [5]],
        #[(3, 0), (0, 0), 'UDD', [4]],
        [(0, 3), (0, 0), 'UUD', [6]],
        [(0, 0), (0, 1), 'UDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD', [1]],
        #[(0, 3), (0, 0), 'UDD', [3]],
        #[(0, 0), (0, 1), 'L', [-1]],
    ]
    for t in tests:
        print(run_ship(t[0], t[1], t[2]), t[3][0], run_ship(t[0], t[1], t[2]) == t[3][0])

else:
    first_line = input()
    start = tuple(map(int, first_line.split()))
    second_line = input()
    fin = tuple(map(int, second_line.split()))
    n = input()  # lenght of wind
    wind = input()
    print(run_ship(start, fin, wind))