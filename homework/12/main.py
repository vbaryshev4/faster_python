def build_tree(pairs):
    """
        :param pairs: ['Sarah Fred', 'Sarah Paul', 'Fred Hilary', 'Fred Jenny', 'Jenny James']
        :return: {'Sarah': ['Fred', 'Paul'], 'Fred': ['Hilary', 'Jenny'], 'Jenny': ['James']}
    """
    splitted_pairs = [i.split() for i in pairs]
    result = {}
    for pair in splitted_pairs:
        if pair[0] in result.keys():
            result[pair[0]].append(pair[1])
        else:
            result.update({pair[0]: [pair[1]]})
    return result


def dfs(tree):
    """
        Idea: Crawling trees in depth
    """
    popped = list()
    stack = list()
    stack.append([list(tree.keys())[0], 1, list(tree.keys())[0]])
    while len(stack) != 0:
        try:
            if stack[-1][1] == 2:
                popped.append(stack[-1])
                stack.pop()
            else:
                stack[-1][1] += 1
                nodes = tree[stack[-1][0]]
                ancestor = stack[-1][-1]
                [stack.append([i, 1, '/'.join([ancestor, i])]) for i in nodes]
        except KeyError:
            popped.append(stack[-1])
            stack.pop()
    return popped


def lca(splitted_routes):
    print(splitted_routes)
    for node_of_route_1 in reversed(splitted_routes[0]):
        for node_of_route_2 in reversed(splitted_routes[1]):
            if node_of_route_1 == node_of_route_2:
                return node_of_route_1


def search_common_ancestor(popped_tree, search_items):
    pair_from_popped_tree = [i[-1].split('/') for i in popped_tree if i[0] in search_items]
    result = lca(pair_from_popped_tree)
    return result


def run(input_data):
    pair_to_search = input_data[1:3]
    pairs = input_data[3:]
    tree = build_tree(pairs)
    popped_tree = dfs(tree)
    result = search_common_ancestor(popped_tree, pair_to_search)
    return result


if __name__ == '__main__':
    from test import examples
    result = run(examples['case4']['Input'])
    print('Result:', result)
    print('Expected:', examples['case4']['Output'])
