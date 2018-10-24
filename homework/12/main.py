from test import examples


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
    popped = []
    stack = []
    stack.append([list(tree.keys())[0], 1])
    while stack != []:
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
    print('stack', stack)
    print('popped', popped, '\n')

    s = search_items
    for i in popped:
        if s == []:
            return i[0]
        elif i[0] in s:
            s.remove(i[0])
            if s == []:
                if i[0] in list(tree.keys()):
                    if set(tree[i[0]]).union(set([i[0]])):
                        return i[0]



if __name__ == '__main__':
    for key in examples.keys():
        input_data = examples[key]['Input']
        output_data = examples[key]['Output']
        employees = input_data[0]
        selected_emp = input_data[1:3]
        pairs = input_data[3:]
        tree = build_tree(pairs)
        print('pairs', pairs)
        print('Tree:', tree)
        print('Searching:', selected_emp)
        print('Should be:', output_data)
        result = dfs(tree, selected_emp)
        print('Result', result)
        print('\n')
