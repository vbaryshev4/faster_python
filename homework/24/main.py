# k, hairs = grow_hair(k, hairs, l, hair_index, add_to_hair)

def grow_hair(k, hairs, length, hair_index, add_to_hair):
    old_hair_length = hairs[hair_index]
    hairs[hair_index] = hairs[hair_index] + add_to_hair
    if old_hair_length <= length < hairs[hair_index]:
        if 0 < hair_index < len(hairs)-1 and hairs[hair_index - 1] > length \
           and hairs[hair_index + 1] > length:
            k -= 1
        elif (hair_index == 0 or hairs[hair_index - 1] <= length) \
                and (len(hairs)-1 == hair_index or hairs[hair_index + 1] <= length):
            k += 1
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


def count_barber_work():
    n, m, l = map(int, input().split())
    '''
        количество волос, 
        количество запросов,
        любимое число Алисы (любимая длинна волоса)
    '''
    hairs = list(map(int, input().split()))
    k = count_k(hairs, l)
    for _ in range(m):
        i = input()
        if i == '0':
            print(k)
        else:
            _, hair_index, add_to_hair = map(int, i.split())
            k, hairs = grow_hair(k, hairs, l, hair_index-1, add_to_hair)


# def count_barber_work(log):
#     n, m, l = map(int, log[0].split())
#     '''
#         количество волос,
#         количество запросов,
#         любимое число Алисы (любимая длина волоса)
#     '''
#     hairs = list(map(int, log[1].split()))
#     k = count_k(hairs, l)
#     for i in log[2:]:
#         if i == '0':
#             print(k)
#         else:
#             _, hair_index, add_to_hair = map(int, i.split())
#             print(hairs)
#             k, hairs = grow_hair(k, hairs, l, hair_index-1, add_to_hair)
#             print(hairs)


count_barber_work()

# if __name__ == '__main__':
#     test = ['4 7 3',
#             '1 2 3 4',
#             '0',
#             '1 2 3',
#             '0',
#             '1 1 3',
#             '0',
#             '1 3 1',
#             '0']
#     test = ['3 3 1',
#             '1 1 3',
#             '0',
#             '1 1 3',
#             '0']
#     count_barber_work(test)
