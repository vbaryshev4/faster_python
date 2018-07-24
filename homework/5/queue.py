
class Stack(object):
    """docstring for Stack"""
    def __init__(self):
        self.stack = []
        
    def put(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop()



class Queue(object):
    """docstring for Queue"""
    def __init__(self):
        self.queue = []
        
    def enqueue(self, elem):
        self.queue.append(elem)

    def dequeue(self):
        result = self.queue[0] 
        self.queue = self.queue[1:]
        return result


class Queue_2(object):
    """docstring for Queue"""
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()
        
    """
    TODO дописать чтобы применялись методы к экземплярам класс из конструктора

    def enqueue(self, elem):
        self.queue.append(elem)

    def dequeue(self):
        result = self.queue[0] 
        self.queue = self.queue[1:]
        return result

    """
