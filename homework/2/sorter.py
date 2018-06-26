from datetime import *

def get_datetime_object(string):
    return datetime.strptime(string, '%Y-%m-%d %H:%M')
    
def time_stamp(datetime_object):
    return datetime.timestamp(datetime_object)

def key_func(i):
    date_time = i.split('\t')[2][:-1]
    return get_datetime_object(date_time)

def save_(data, file_name):
    with open(file_name, 'w') as f:
        f.writelines(data)

def start_sorter(chunk, chunk_num):
    chunk.sort(key=key_func)
    return save_(chunk, 'chunks/sort_results_{0}.txt'.format(chunk_num))
