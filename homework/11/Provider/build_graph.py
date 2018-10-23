'''

    Import algorithm: adds the graph up to full graph

    Еach major currency has another as second and exchange value

'''


def build_graph(cur_data):
    result = []
    time_stamp = cur_data[0][3]
    for i in range(len(cur_data)):
        for k in range(len(cur_data)):
            result.append([cur_data[k][1],
                           cur_data[i][1],
                           cur_data[i][2]/cur_data[k][2],
                           cur_data[i][3]])
    return result

