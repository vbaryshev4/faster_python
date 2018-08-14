class Spiral:
    """docstring for Spiral"""
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        self.center = [self.rows//2, self.columns//2]

    def get_value(self, head):
        return self.matrix[head[0]][head[1]]

    def unspiral_matrix(self):

        def left():
            head[1] = head[1] - 1
            
        def right():
            head[1] = head[1] + 1

        def down():
            head[0] = head[0] + 1

        def up():
            head[0] = head[0] - 1

        head = self.center
        result = []
        count = 1
        
        result.append(self.get_value(head))
        while head != [0, 0]:
            if count % 2 == 0:
                for i in range(count):
                    right()
                    result.append(self.get_value(head))
                for i in range(count):
                    up()
                    result.append(self.get_value(head))
            elif count % 2 == 1:
                for i in range(count):
                    if head != [0, 0]:
                        left()
                        result.append(self.get_value(head))
                for i in range(count):
                    if head != [0, 0]:
                        down()
                        result.append(self.get_value(head))
            count += 1

        return result
        