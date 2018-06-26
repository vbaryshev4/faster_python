from sys import getsizeof
from sorter import start_sorter

size_limit = 10240

def check_size(chunk, line, size_limit):
    return getsizeof(chunk) + getsizeof(line) < size_limit

def start_divider():
    with open('logs.txt') as f:
        chunk = list()
        chunk_num = 0
        for line in f:
            if check_size(chunk, line, size_limit) == True:
                chunk.append(line)
            else:
                chunk_num += 1
                print('Chunk #{0}'.format(chunk_num))
                start_sorter(chunk, chunk_num)
                chunk = list()
                chunk.append(line)
        chunk_num += 1
        print('Chunk #{0}'.format(chunk_num))
        start_sorter(chunk, chunk_num)
        
if __name__ == '__main__':
    result = start_divider()