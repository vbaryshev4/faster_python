# ПЕРВОЕ ЗНАКОМСТВО
'''
1) Проанализировть цикл на биг О
2) Ознакомиться с основными принципами профеллирования

'''


import timeit

A = '''
def make_str(n):
    a = u'е'
    for i in range(n):
        a += str(i)
    return a
make_str(n)
'''

N = [100, 1000, 10000, 100000]
for i in N:
    print('Res=', timeit.timeit(stmt=A, number=100, setup='n={0}'.format(i)), 'Val=', i)