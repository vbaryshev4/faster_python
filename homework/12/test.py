from main import run
import pytest


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
                 'Output': 'June'},
            'case4':
                {'Input': [6,
                           'Paul',
                           'James',
                           'Sarah Fred',
                           'Sarah Paul',
                           'Fred Hilary',
                           'Fred Jenny',
                           'Jenny James'],
                 'Output': 'Sarah'},
            }


@pytest.mark.parametrize("case", ["case1", "case2", "case3", "case4"])
def test1(case):
    input_data = examples[case]['Input']
    expected = (examples[case]['Output'])
    result = run(input_data)
    assert result == expected