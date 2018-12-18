# coding = zip([1000, 500, 100, 50, 10, 5, 1], ['M', 'D', 'C', 'L', 'X', 'V', 'I'])
#
# def get_romans(number):
#     result = []
#     for d, k in coding:
#         while number >= d:
#             result.append(k)
#             number -= d
#     return ''.join(result)
#
# print(get_romans(1999))



a = [(1, 4), (5,3), (7,2)]        # [1,1,1,1,5,5,5,7,7]
b = [(2,1), (4,3), (8,2), (0, 3)] # [2,4,4,4,8,8,0,0,0]
                                  # [2,4,4,4,40,40,0,0,0] - произведения
                                  # 94 - сумма произведений

def unpack(vector):
    for i in vector:
        for k in range(i[1]):
            yield i[0]

def mul_vectors(a, b):
    for i, j in zip(a, b):
        yield i * j



print(sum(mul_vectors(unpack(a), unpack(b))))