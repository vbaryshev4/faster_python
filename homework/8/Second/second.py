'''
    Есть матрица 2n-1 x 2n-1, заполненная случайными значениями.
    Надо вывести их на экран в ряд, начиная из центра по спирали: 
    влево - вниз - вправо - вверх и т.д.

    Если матрица:
     1  2  3  4  5
     6  7  8  9 10
    11 12 13 14 15
    16 17 18 19 20
    21 22 23 24 25

    1 2 3
    4 5 6
    7 8 9

    То результат:
    5 4 7 8 9 6 3 2 1

    Решение должно быть для общего случая с любым n.
'''

class Spiral(object):
    """docstring for Spiral"""
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        self.center = [self.rows//2, self.columns//2]
        self.head = self.center
        self.result = []


    def unspiral_matrix(self):

        def get_value(self):
            r = self.matrix[self.head[0]][self.head[1]]
            self.result.append(r)

        def left(self):
            self.head[1] = self.head[1] - 1
            
        def right(self):
            self.head[1] = self.head[1] + 1

        def down(self):
            self.head[0] = self.head[0] + 1

        def up(self):
            self.head[0] = self.head[0] - 1
        
        count = 1
        
        get_value(self)
        print(self.head, self.result)
        
        while self.head != [0, 0]:
            
            if count % 2 == 0:
                
                for i in range(count):
                    right(self)
                    get_value(self)
                    print(self.head, self.result)

                for i in range(count):
                    up(self)
                    get_value(self)
                    print(self.head, self.result)

            elif count % 2 == 1:
                
                for i in range(count):
                    if self.head != [0, 0]:
                        left(self)
                        get_value(self)
                        print(self.head, self.result)

                for i in range(count):
                    if self.head != [0, 0]:
                        down(self)
                        get_value(self)
                        print(self.head, self.result)

            count += 1







        