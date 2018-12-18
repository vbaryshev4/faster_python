case = [2, 2, 1, 2]

def from_bin(lst):
    s = ''.join([str(i) for i in lst])
    return int(s, 2)

def to_bin(integer):
    result = bin(integer)[2:]
    result = [int(i) for i in result]
    result = [0] * (64 - len(result)) + result
    return result

def summ(t, k):
    return [i+j if i+j < 3 else 0 for i, j in zip(t, k)]

def get_unique(lst):
    t = [0]*64
    for i in lst:
        k = to_bin(i)
        t = summ(t, k)
    return from_bin(t)


if __name__ == "__main__":
    result = get_unique(case)
    print(result)