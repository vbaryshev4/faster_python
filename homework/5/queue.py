
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


class StackAsQueue(object):
    """docstring for Queue"""
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, elem):
        self.stack_1.put(elem)

    def dequeue(self):
        self.stack_2.stack = self.stack_1.stack[1:]
        result = self.stack_1.stack[0]
        self.stack_1.stack = self.stack_2.stack
        self.stack_2 = Stack()
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
