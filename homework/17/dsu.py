from test import cases


class DisjointSets:

    def __init__(self, n):
        self.parents = [i for i in range(n+1)]

    def find(self, x):
        indexes = []
        while x != self.parents[x]:
            indexes.append(x)
            x = self.parents[x]
        indexes.append(x)
        # return indexes
        return [x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        for i in root_y:
            self.parents[i] = root_x[0]

if __name__ == "__main__":
    for i in cases:
        result = 1
        input = i['input']
        expected = i['expected_output']
        p = DisjointSets(input[0][0])
        print(p.parents)
        for e in input[1]:
            p.union(e[0], e[1])
            print('e', e)
            print(p.parents)
        print(p.parents)
        for d in input[2]:
            root_x = p.find(d[0])[-1]
            root_y = p.find(d[1])[-1]
            if root_x == root_y:
                result = 0
        print('Test passed:', result == expected, '\n')
