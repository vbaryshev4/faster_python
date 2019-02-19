import sys
from itertools import groupby


def get_max_sublist(l):
    m = max(l)
    r = (len(list(i[1])) for i in groupby(l) if i[0] == m)
    return max(r)


if len(sys.argv) > 1 and sys.argv[1] == 'test':
    tests = [
        [[1], 1],
        [[1, 2, 2, 3], 1],
        [[1, 2, 2, 1], 2],
        [[1, 2, 3], 1],
        [[1, 1, 4, 4], 2],
        [[4, 1, 4, 4, 4], 3],
        [[4, 1, 4, 5, 4], 1]
    ]
    for t in tests:
        print(get_max_sublist(t[0]), t[1])

else:
    first_line = input()
    second_line = input()
    l = (list(map(int, second_line.split())))
    print(get_max_sublist(l))