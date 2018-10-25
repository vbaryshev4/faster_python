from main import run


examples = {'case1':
                {'Input': [6,
                           'Hilary',
                           'James',
                           'Sarah Fred',
                           'Sarah Paul',
                           'Fred Hilary',
                           'Fred Jenny',
                           'Jenny James'],
                 'Output': 'Fred'},
            'case2':
                {'Input': [4,
                           'Simon',
                           'Claudiu',
                           'Sarah Claudiu',
                           'Sarah Paul',
                           'Claudiu Simon'],
                 'Output': 'Claudiu'},
            'case3':
                {'Input': [5,
                           'Gareth',
                           'Alex',
                           'June Alex',
                           'June Qing',
                           'Qing Paul',
                           'Qing Gareth'],
                 'Output': 'June'}
            }

if __name__ == '__main__':

    # TODO:
    # def test_answer(input_data, expectation):
    #     assert run(input_data) == expectation
    

    for key in examples.keys():
        input_data = examples[key]['Input']
        employees_num = examples[key]['Input'][0]
        expected = (examples[key]['Output'], employees_num)
        result = run(input_data)
        print(result, expected)
