import sys
from itertools import islice


def get_two_max(lst):
    max_1 = max(islice(lst, 2))
    max_2 = min(islice(lst, 2))
    for i in islice(lst, 2, len(lst)):
        if i > max_2:
            if i > max_1:
                max_2 = max_1
                max_1 = i
            else:
                max_2 = i
    return max_1, max_2


def get_max_emotions(vals, n, m, k):
    max_1, max_2 = get_two_max(vals)
    alpha = m // (k + 1)
    rest_vals = m % (k + 1)
    return (alpha * (max_1 * k + max_2)) + (rest_vals * max_1)


if len(sys.argv) > 1 and sys.argv[1] == 'test':
    tests = [
        [(6, 9, 2), [1, 3, 3, 7, 4, 2], 54],
        [(3, 1000000000, 1), [1000000000, 987654321, 1000000000], 1000000000000000000],
        [(4, 3, 3), [1, 2, 3, 4], 12],
        [(4, 3, 2), [1, 2, 3, 4], 11],
        [(4, 3, 1), [1, 2, 3, 4], 11],
        [(4, 10, 3), [1, 2, 3, 4], 38]
    ]
    for t in tests:
        print(get_max_emotions(t[1], *t[0]), t[2])

else:
    first_line = input()
    n, m, k = map(int, first_line.split())
    second_line = input()
    l = list(map(int, second_line.split()))
    print(get_max_emotions(l, n, m, k))