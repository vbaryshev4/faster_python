"""
    Дана матрица из 0 и 1.
    В каждой строке сначала иду только единицы,
    потом только нули.
    Вернуть индекс первого столбца,
    состоящего только из нулей.

    Асимтотическая сложность по времени O(N log M),
    где N - число строк и
    M - количество столбцов

    Асимтотическая сложность по памяти O(1).
"""


def binary_search(lst, searching_digit):
    left = 0
    right = len(lst)
    while left != right:
        middle = (left + right) // 2
        if lst[middle] == searching_digit:
            right = middle
        else:
            left = middle + 1
    return left


if __name__ == '__main__':
    matrix = [
                [1, 1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1],
            ]

    print(max(binary_search(i, 0) for i in matrix))