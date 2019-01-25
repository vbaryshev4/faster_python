from functools import  total_ordering
import inspect

@total_ordering
class Compare:

    def __init__(self, letter):
        self.letter = letter

    def __lt__(self, other):
        print('? {} {}'.format(self.letter, other.letter))
        r = input()
        if r == '<':
            return True
        return False


if __name__ == "__main__":

    a = Compare('A')
    print(inspect.getsource(a.__gt__))