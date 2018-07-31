
class Stack():
    """docstring for Stack"""
    def __init__(self):
        self.stack = []
        
    def put(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop()



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
        
        for elem in range(len(self.stack_1.stack)):
            a = self.stack_1.pop()
            self.stack_2.put(a)

        result = self.stack_2.pop()

        for elem in range(len(self.stack_2.stack)):
            a = self.stack_2.pop()
            self.stack_1.put(a)

        return result

a = StackAsQueue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
print(a.stack_1.stack)
print(a.dequeue())
print(a.stack_1.stack)
print(a.stack_2.stack)

'''
Кирилл Игнатьев, [25.07.18 20:46]
Нет, так нельзя делать:
self.stack_1.stack[0]
Ты используешь stack как массив.
Представь, что stack_1.stack это приватный член класса, он не входит в интерфейс.
можешь даже переименовать его в __stack, чтобы не было соблазна.

Можно использовать только методы put и pop, максимум для удобства еще можешь реализовать len()
'''

