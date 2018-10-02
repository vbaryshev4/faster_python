import redis
import uuid
from test import fixer_response_example

'''
    1) Data Provider(http://data.fixer.io)
        - Передает данные по курсам валют
        - Получает данные
'''
class Fixer:
    def __init__(self):
        self.key = "97ee15850fb7fd028cf83cf807cba6e3"
        self.url = "http://data.fixer.io/api/"
        self.query = "http://data.fixer.io/api/latest&base=EUR?access_key=97ee15850fb7fd028cf83cf807cba6e3"
        self.test_query = None

    def set_test_value(self, example):
        self.test_query = example

    def set_test_value(self):
        try:
            return self.test_query

class Provider:
    def __init__(self, status):
        self.r = redis.StrictRedis(host='localhost', port=1300, db=1)
        self.status = status
        self.uuid = uuid.uuid4()
        self.message_queue = 'message_list'


if __name__ == '__main__':
    f = Fixer(fixer_response_example)
    print(f)