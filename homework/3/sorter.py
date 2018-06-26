from datetime import *

def get_datetime_object(string):
    return datetime.strptime(string, '%Y-%m-%d %H:%M')

def key_func(i):
    date_time = i.split('\t')[2][:-1]
    return get_datetime_object(date_time)

def start():
    with open('logs.txt', 'r') as f:
        lines = f.readlines()

    lines.sort(key=key_func)
    with open('sort_results.txt', 'w') as f:
        f.writelines(lines)


if __name__ == '__main__':
    start()