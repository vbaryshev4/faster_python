from distance import distance

def test_summery(test_result):
    return len(result['True']), len(result['False'])

def run_test(cases):
    
    result = {'True':[], 'False':[]}

    for case in cases:
        a, b = case['words'] # words
        expected_result = case['result'] # correct return
        returned_result = distance(a,b)
        
        if expected_result == returned_result:
            result['True'].append(case)
        else:
            result['False'].append(case)

    return result

def get_test_data(word_x, word_y, matrix):
    
    result = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            case = {'words':None, 'result':None}
            case['words'] = [word_x[:j+1], word_y[:i+1]]
            case['result'] = matrix[i][j]
            result.append(case)

    return result 

if __name__ == '__main__':

    word_x = ' POLYNOMIAL'
    word_y = ' EXPONENTIAL'
    matrix = [
                [0,1,2,3,4,5,6,7,8,9,10],
                [1,1,2,3,4,5,6,7,8,9,10],
                [2,2,2,3,4,5,6,7,8,9,10],
                [3,2,3,3,4,5,6,7,8,9,10],
                [4,3,2,3,4,5,5,6,7,8,9],
                [5,4,3,3,4,4,5,6,7,8,9],
                [6,5,4,4,4,5,5,6,7,8,9],
                [7,6,5,5,5,4,5,6,7,8,9],
                [8,7,6,6,6,5,5,6,7,8,9],
                [9,8,7,7,7,6,6,6,6,7,8],
                [10,9,8,8,8,7,7,7,7,6,7],
                [11,10,9,8,9,8,8,8,8,7,6]
            ]

    test_data = get_test_data(word_x, word_y, matrix)                
    result = run_test(test_data)
    print(result)
    counts = test_summery(result)
    print('True = {0}, False = {1}'.format(counts[0], counts[1]))

