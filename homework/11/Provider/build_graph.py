'''

    Import algorithm: adds the graph up to full graph

    Еach major currency has another as second and exchange value

'''


def build_graph(cur_data):
    result = [i for i in cur_data]
    for i in range(len(cur_data)):
        for k in range(len(cur_data[i])):
            print(cur_data[i], cur_data[i][k])
            # print(cur_data[i])
        # for k in range(len(i)):
        #     print(cur_data[i][k])
        # item = [i[1], i[0], 1/i[2], i[3]]
        # if item not in result:
        #     result.append(item)


    print(result)