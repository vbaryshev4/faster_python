from second import Spiral
'''
    Если матрица:
    1 2 3
    4 5 6
    7 8 9

    То результат:
    5 4 7 8 9 6 3 2 1
'''

if __name__ == '__main__':
    
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    result = Spiral(matrix)
    # center = result.center
    # print(matrix[center[0]][center[1]])
    # print(result.head)
    print(result.unspiral_matrix())
    print(result.result)
