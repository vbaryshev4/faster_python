from random import randint

def if_num(lst, value):
    s = set(lst)
    for num in s:
        b = value - num
        if b in s and num != b:
            return True, b, num
    return False

if __name__ == '__main__':

    value = randint(0,1999)
    lst = [randint(0,999) for i in range(100)]
    lst = [1, 2]
    value = 4
    result = if_num(lst, value)
    print('value =', value)
    print('list with nums =', lst)
    print(result)