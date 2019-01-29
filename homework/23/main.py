def transform_to_dict(pairs):
    result = dict()
    count = 0
    for i, j in pairs:
        if i not in result.keys() and j not in result.keys():
            result[i] = count
            result[j] = count
            count += 1

        if i in result.keys() or j in result.keys():
            if i in result.keys():
                result[j] = result[i]
            else:
                result[i] = result[j]
    return result


def compare_strings(s1, s2, dct):
    s1 = s1.split()
    s2 = s2.split()
    s1 = [dct.get(i, i) for i in s1]
    s2 = [dct.get(i, i) for i in s2]
    return s1 == s2

if __name__ == '__main__':
    pairs = [
        ['rating', 'popularity'],
        ['stats', 'statistics'],
        ['stats', 'percentage'],
        ['pop', 'popularity'],
        ['polls', 'votes']
    ]

    dct = transform_to_dict(pairs)
    s1 = 'Obama rating stats'
    s2 = 'Obama popularity statistics'
    print(compare_strings(s1, s2, dct))