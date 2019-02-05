def grow_hair(hairs, l, p, d):
    hairs[hair] = hairs[hair] + add_to_hair
    ...
    return k, hairs


def count_k(hairs, l):
    k = 0
    for i in range(len(hairs)):
        if i == 0:
            if hairs[i] > l:
                k += 1
        else:
            if hairs[i] > l:
                if hairs[i-1] <= l:
                    k += 1
    return k


def count_barber_work(log):
    n, m, l = map(int, log[0].split())
    '''
        количество волос, 
        количество запросов,
        любимое число Алисы (любимая длинна волоса)
    '''
    hairs = list(map(int, log[1].split()))
    k = count_k(hairs, l)
    for i in log[2:]:
        if i == 0:
            print(k)
        else:
            _, hair_index, add_to_hair = map(int, i.split())
            k, hairs = grow_hair(hairs, l, hair_index, add_to_hair)


if __name__ == '__main__':
    test = ['4 7 3',
            '1 2 3 4',
            '0',
            '1 2 3',
            '0',
            '1 1 3',
            '0',
            '1 3 1',
            '0']
    print(test)