
class Spiral(object):
    """docstring for Spiral"""
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        self.center = [self.rows//2, self.columns//2]
        self.head = self.center
        # self.result = []

    def unspiral_matrix(self):

        result = []

        def get_value(self):
            item = self.matrix[self.head[0]][self.head[1]]
            result.append(item)

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
        
        while self.head != [0, 0]:
            
            if count % 2 == 0:
                
                for i in range(count):
                    right(self)
                    get_value(self)

                for i in range(count):
                    up(self)
                    get_value(self)

            elif count % 2 == 1:
                
                for i in range(count):
                    if self.head != [0, 0]:
                        left(self)
                        get_value(self)

                for i in range(count):
                    if self.head != [0, 0]:
                        down(self)
                        get_value(self)

            count += 1

        return result
