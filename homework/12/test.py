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


def test1():
    input_data = examples['case1']['Input']
    employees_num = examples['case1']['Input'][0]
    expected = (examples['case1']['Output'], employees_num)
    result = run(input_data)
    assert result == expected


def test2():
    input_data = examples['case2']['Input']
    employees_num = examples['case2']['Input'][0]
    expected = (examples['case2']['Output'], employees_num)
    result = run(input_data)
    assert result == expected


def test3():
    input_data = examples['case3']['Input']
    employees_num = examples['case3']['Input'][0]
    expected = (examples['case3']['Output'], employees_num)
    result = run(input_data)
    assert result == expected


