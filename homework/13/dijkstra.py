'''

    Материал на Курсере (4 неделя из курса по графам):
    https://www.coursera.org/learn/algorithms-on-graphs/home/week/4
    Можно бесплатно записаться на курс,
    посмотреть видео и почитать материалы.

'''

from test_dijkstra import examples
import heapq


def find_way(tree, start, destination):
    result = tree[start]
    heap = []
    [heapq.heappush(heap, (result[i], i)) for i in result]
    h = (0, destination-1)
    while h[1] != destination:
        print('heap', heap)
        h = heapq.heappop(heap)
        if h[1] in tree.keys():
            [heapq.heappush(heap, i[::-1]) for i in tree[h[1]].items()]
            [result.update({i[0]: h[0]+i[1]}) for i in tree[h[1]].items() if h[0]+i[1] < result[i[0]]]
    # print('tree start destination', tree, start, destination)
    # print('result', result)
    return result[destination]



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
        output = examples[key]['Output']
        vertices, edges = examples[key]['Input'][0]
        raw_tree = examples[key]['Input'][1:-1]
        start, destination = examples[key]['Input'][-1]
        tree = build_tree(raw_tree)
        print('tree', tree)
        result = find_way(tree, start, destination)
        print('output', output, 'result', result, '\n')

