from datetime import *
from collections import *

def get_datetime_object(string):
    return datetime.strptime(string, '%Y-%m-%d %H:%M')
    
def time_stamp(datetime_object):
    return datetime.timestamp(datetime_object)

def sort_(result):
    return OrderedDict(sorted(result.items(), key=lambda t: t[1]))

def save_(data, file_name):
    with open(file_name, 'w') as f:
        f.writelines(data)

def start_sorter(chunk, chunk_num):
    result = {}
    for i in chunk:
        log = i.split()
        date_time = ' '.join(log[3:5])
        result.update({i:time_stamp(get_datetime_object(date_time))})
    return save_(sort_(result), 'chunks/sort_results_{0}.txt'.format(chunk_num))
