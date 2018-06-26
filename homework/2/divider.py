from sys import getsizeof
from sorter import start_sorter

size_limit = 104857600

def check_size(chunk_size, size_limit):
    return chunk_size < size_limit

def start_divider():
    with open('logs.txt', 'r') as f:
        chunk = list()
        chunk_size = 0
        chunk_num = 0
        for line in f:
            chunk_size += getsizeof(line)
            if check_size(chunk_size, size_limit) == True:
                chunk.append(line)
            else:
                chunk_size = 0
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