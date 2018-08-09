from second import Spiral

if __name__ == '__main__':
    cases = {
                1:{
                    'matrix':[
                                [1,2,3],
                                [4,5,6],
                                [7,8,9]
                            ],
                    'result':[5,4,7,8,9,6,3,2,1]
                },
                2:{
                    'matrix':[
                                [1,2,3,4,5],
                                [6,7,8,9,10],
                                [11,12,13,14,15],
                                [16,17,18,19,20],
                                [21,22,23,24,25]
                            ],
                    'result':[13,12,17,18,19,14,9,8,7,6,11,16,21,22,23,24,25,20,15,10,5,4,3,2,1]
                },
                3:{
                    'matrix':[
                                [1,1,1],
                                [1,1,1],
                                [1,1,1]
                            ],
                    'result':[1,1,1,1,1,1,1,1,1]
                },
                4:{
                    'matrix':[
                                [-1,-1,-1],
                                [-1,-1,-1],
                                [-1,-1,-1]
                            ],
                    'result':[-1,-1,-1,-1,-1,-1,-1,-1,-1]
                },
                5:{
                    'matrix':[
                                ['i','h','g'],
                                ['b','a','f'],
                                ['c','d','e']
                            ],
                    'result':['a','b','c','d','e','f','g','h','i']
                },
            }
    
    for i in range(1,6):
        matrix = cases[i]['matrix']
        item = Spiral(matrix)
        result = item.unspiral_matrix()
        if result == cases[i]['result']:
            print('OK')
        else:
            print('False')

