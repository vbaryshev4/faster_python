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
        self.sources = [Fixer()]

    def prepare_data_for_db(self, source):
        data = source.get_test_value()
        if source.__class__.__name__ == "Fixer":
            data...

        """
            TODO
        """


    def get_data(self):
        data = self.prepare_data_for_db(self.fixer)

class Fixer:
    def __init__(self):
        self.key = "97ee15850fb7fd028cf83cf807cba6e3"
        self.url = "http://data.fixer.io/api/"
        self.query = "http://data.fixer.io/api/latest&base=EUR?access_key=97ee15850fb7fd028cf83cf807cba6e3"
        self.test_query = fixer_response_example

    def get_test_value(self):
        return self.test_query


# if __name__ == '__main__':
#
#     tests...

