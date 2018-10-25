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


def dfs(tree, search_items):
    """
        Idea: Crawling trees in depth

        :param tree: {'Sarah': ['Fred', 'Paul'], 'Fred': ['Hilary', 'Jenny'], 'Jenny': ['James']}
        :param search_items: ['Hilary', 'James']
        :return: Fred - Mutual director ['Hilary', 'James']
    """
    popped = list()
    stack = list()
    stack.append([list(tree.keys())[0], 1])
    while len(stack) != 0:
        try:
            if stack[-1][1] == 2:
                popped.append(stack[-1])
                stack.pop()
            else:
                stack[-1][1] += 1
                nodes = tree[stack[-1][0]]
                [stack.append([i, 1]) for i in nodes]
        except KeyError:
            popped.append(stack[-1])
            stack.pop()

    s = search_items.copy()
    for i in popped:
        if len(s) == 0:
            return i[0], len(popped)
        elif i[0] in s:
            s.remove(i[0])
            if len(s) == 0:
                if i[0] in list(tree.keys()) and set(tree[i[0]] + [i[0]]) == set(search_items):
                    return i[0], len(popped)


def run(input_data):
    selected_emp = input_data[1:3]
    pairs = input_data[3:]
    tree = build_tree(pairs)
    result = dfs(tree, selected_emp)
    return result

