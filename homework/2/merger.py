from os import listdir
import heapq
from datetime import *

def get_datetime_object(string):
    return datetime.strptime(string, '%Y-%m-%d %H:%M')

def key_func(i):
    date_time = i.split('\t')[2][:-1]
    return get_datetime_object(date_time)

def join_results(lst):
    with open('chunks/sort_results.txt', 'a') as f:
        for i in heapq.merge(*lst, key=key_func):
            f.write(i)
            f.flush()

def start_merger():
    result = []
    for file in listdir('chunks'):
        if file != '.DS_Store':
            result.append(open('chunks/' + file))
    join_results(result)


if __name__ == '__main__':
    result = start_merger()