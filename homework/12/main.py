from test import examples


def build_tree(pairs):
    splitted_pairs = [i.split() for i in pairs]
    result = {}
    for pair in splitted_pairs:
        if pair[0] in result.keys():
            result[pair[0]].append(pair[1])
        else:
            result.update({pair[0]: [pair[1]]})
    return result


for key in examples.keys():
    input_data = examples[key]['Input']
    employees = input_data[0]
    selected_emp = input_data[1:3]
    pairs = input_data[3:]
    # print(employees, selected_emp, pairs)
    tree = build_tree(pairs)
    print(tree, '\n')
