
class Stack():
    """docstring for Stack"""
    def __init__(self):
        self.__stack = []
    
    def __str__(self):
        '''Returns representation of the object'''
        return "{}({})".format(self.__class__.__name__, self.__stack)

    def is_empty(self):
        return len(self.__stack) == 0

    def put(self, elem):
        self.__stack.append(elem)

    def pop(self):
        return self.__stack.pop()



class Queue():
    """docstring for Queue"""
    def __init__(self):
        self.queue = []
        
    def enqueue(self, elem):
        self.queue.append(elem)

    def dequeue(self):
        result = self.queue[0] 
        self.queue = self.queue[1:]
        return result


class StackAsQueue():

    """docstring for Queue"""
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, elem):
        self.stack_1.put(elem)

    def dequeue(self):
        if self.stack_2.is_empty():
            while not self.stack_1.is_empty():
                elem = self.stack_1.pop()
                self.stack_2.put(elem)

        return self.stack_2.pop()

a = StackAsQueue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
print(a.stack_1)
print(a.dequeue())
print(a.stack_1)
print(a.stack_2)

'''
Кирилл Игнатьев, [25.07.18 20:46]
Нет, так нельзя делать:
self.stack_1.stack[0]
Ты используешь stack как массив.
Представь, что stack_1.stack это приватный член класса, он не входит в интерфейс.
можешь даже переименовать его в __stack, чтобы не было соблазна.

Можно использовать только методы put и pop, максимум для удобства еще можешь реализовать len()
'''

