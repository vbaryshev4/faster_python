'''

    Gets data from external sources: Fixer or CurrencyLayer.

        If data from Fixer is not available
        gets data from CurrencyLayer

'''


from test import fixer_response, currencylayer_response
from credentials import creds



class Provider:
    def __init__(self):
        self.sources = [Fixer, CurrencyLayer]

    def get_data(self):
        for i in self.sources:
            try:
                test = i()
                raw = test.get_test_value()
                data = test.get_db_values(raw)
                return data
            except:
                continue

class Fixer:
    def __init__(self):
        self.key = creds['Fixer']['key']
        self.url = creds['Fixer']['url']
        self.query = creds['Fixer']['query']
        self.test_query = fixer_response

    def get_test_value(self):
        return self.test_query

    def get_db_values(self, data_set):
        curs = ["RUB", "USD", "EUR", "GBP"]
        base = data_set['base']
        date = data_set['timestamp']
        return [[base, i, data_set['rates'][i], date] for i in data_set['rates'] if i in curs]


class CurrencyLayer:
    def __init__(self):
        self.key = creds['Currencylayer']['key']
        self.url = creds['Currencylayer']['url']
        self.query = creds['Currencylayer']['query']
        self.test_query = currencylayer_response

    def get_test_value(self):
        return self.test_query

    def get_db_values(self, data_set):
        curs = ["RUB", "USD", "EUR", "GBP"]
        source = data_set['source']
        date = data_set['timestamp']
        return [[source, i[3:], data_set['quotes'][i], date] for i in data_set['quotes'] if i[3:] in curs]


