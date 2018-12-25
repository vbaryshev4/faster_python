def find_shortest(way):
    result = 0
    prev = way[0]
    for i in way[1:]:
        vector = (abs(prev[0]-i[0]), abs(prev[1]-i[1]))
        result += max(vector)
        prev = i
    return result


if __name__ == '__main__':
    routes = [(0, 0), (0, 1), (2, 2)]
    print(find_shortest(routes))
