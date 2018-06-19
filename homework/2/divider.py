from sys import getsizeof
from sorter import start_sorter

size_limit = 1024

def check_size(chunk, line, size_limit):
    return getsizeof(chunk) + getsizeof(line) < size_limit

def start_divider():
    with open('logs.txt') as f:
        chunk = list()
        for line in f:
            if check_size(chunk, line, size_limit) == True:
                chunk.append(line)
            else:
                print(getsizeof(chunk))
                start_sorter(chunk)
                chunk = list()
                chunk.append(line)
        start_sorter(chunk)
        
if __name__ == '__main__':
    result = start_divider()