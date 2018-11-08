'''

    Материал на Курсере (4 неделя из курса по графам):
    https://www.coursera.org/learn/algorithms-on-graphs/home/week/4
    Можно бесплатно записаться на курс,
    посмотреть видео и почитать материалы.

'''

from test_dijkstra import examples
import heapq


def find_way(tree, start, destination):
    if start in tree.keys():
        result = tree[start]
    else:
        return -1
    heap = [] # each element = (edge_weight, vertice)
    [heapq.heappush(heap, i) for i in [(r, result[r])[::-1] for r in result]]
    h = (0, start)
    debug_counter = 0
    print('vertice = {0}, destination = {1}, heap = {2}'.format(h[1], destination, heap))
    while h[1] != destination:
        h = heapq.heappop(heap)
        if h[1] in tree.keys():
            [heapq.heappush(heap, i[::-1]) for i in tree[h[1]].items()]
            print('vertice = {0}, destination = {1}, heap = {2}'.format(h[1], destination, heap))
            for i in tree[h[1]].items():
                if i[0] in result.keys():
                    if h[0] + i[1] < result[i[0]]:
                        result.update({i[0]: h[0] + i[1]})
                else:
                    result.update({i[0]: h[0] + i[1]})
                debug_counter += 1
                if debug_counter == 10:
                    return None

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
        if key == 'case2': # Only debug
            output = examples[key]['Output']
            vertices, edges = examples[key]['Input'][0]
            raw_tree = examples[key]['Input'][1:-1]
            start, destination = examples[key]['Input'][-1]
            tree = build_tree(raw_tree)
            print('tree', tree)
            result = find_way(tree, start, destination)
            print('output', output, 'result', result, '\n\n\n\n')

