'''

    Материал на Курсере (4 неделя из курса по графам):
    https://www.coursera.org/learn/algorithms-on-graphs/home/week/4
    Можно бесплатно записаться на курс,
    посмотреть видео и почитать материалы.

'''


from test_dijkstra import examples
import math


def find_way(tree, vertices, start, destination):
    cheking_list = {i: {'known': False, 'cost': math.inf} for i in vertices}
    if start in tree.keys():
        cheking_list[start]['cost'] = 0
    else:
        return -1
    while False in set(cheking_list[i]['known'] for i in cheking_list):
        cursor = {i: cheking_list[i]['cost'] for i in cheking_list if cheking_list[i]['known'] == False}
        cursor = min(cursor, key=cursor.get)
        cheking_list[cursor]['known'] = True
        if cursor in tree.keys():
            for i in tree[cursor]:
                sum = cheking_list[cursor]['cost'] + tree[cursor][i]
                if cheking_list[i]['cost'] > sum:
                    cheking_list[i]['cost'] = sum
    return cheking_list[destination]['cost']


def build_tree(data):
    result = {}
    for i in data:
        if i[0] not in result:
            result.update({i[0]: {i[1]: i[2]}})
        else:
            result[i[0]].update({i[1]: i[2]})
    return result


if __name__ == "__main__":
    for key in examples.keys():
        expected_output = examples[key]['Output']
        count_vertices, edges = examples[key]['Input'][0]
        raw_tree = examples[key]['Input'][1:-1]
        start, destination = examples[key]['Input'][-1]
        tree = build_tree(raw_tree)
        vertices = [i[0:2] for i in raw_tree]
        vertices = set([y for x in vertices for y in x])
        print('tree', tree)
        result = find_way(tree, vertices, start, destination)
        print(result, expected_output)