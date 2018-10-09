from test import fixer_response_example

'''
    1) Data Provider(http://data.fixer.io)
        - Передает данные по курсам валют
        - Получает данные
'''
'''
    pg_ctl -D /usr/local/var/postgres start
    pg_ctl -D /usr/local/var/postgres status
    psql postgres ...
    pg_ctl -D /usr/local/var/postgres stop
    
'''
class Provider:
    def __init__(self):
        self.sources = [Fixer]

    def get_data(self):
        for i in self.sources:
            try:
                test = i()
                raw = test.get_test_value()
                data = test.get_db_values(raw)
                return data
            except ValueError:
                continue


class Fixer:
    def __init__(self):
        self.key = "97ee15850fb7fd028cf83cf807cba6e3"
        self.url = "http://data.fixer.io/api/"
        self.query = "http://data.fixer.io/api/latest&base=EUR?access_key=97ee15850fb7fd028cf83cf807cba6e3"
        self.test_query = fixer_response_example

    def get_test_value(self):
        return self.test_query

    def get_db_values(self, data_set):
        curs = ["RUB", "USD", "EUR", "GBP"]
        base = data_set['base']
        date = data_set['date']
        return [[base, i, data_set['rates'][i], date] for i in data_set['rates'] if i in curs]



if __name__ == '__main__':
    t = Provider()
    print(t.get_data())
