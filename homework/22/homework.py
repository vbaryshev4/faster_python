from bisect import bisect_left


def find_index(lst, elem):
    index = bisect_left(lst, elem)
    if len(lst) != 0:
        if lst[index] == elem:
            return index
    else:
        return None


if __name__ == '__main__':
    tests = {
                1: {
                    'input': ([0, 10, 20, 500, 700], 500),
                    'output': 3
                },
                2: {
                    'input': ([0, 10, 20, 500, 700], 0),
                    'output': 0
                },
                3: {
                    'input': ([0, 10, 20, 500, 700], 1),
                    'output': None
                },
                4: {
                    'input': ([], 1),
                    'output': None
                }
    }

print(tests, '\n')
for key in tests.keys():
    lst, val = tests[key]['input']
    expected = tests[key]['output']
    result = find_index(lst, val)
    print('Result:', result, 'Expected', expected)
    print('\n')