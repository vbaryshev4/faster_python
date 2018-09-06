import sys
import time
import string
import random
import redis
import uuid


message_speed = 0.5
message_length = 4


class Behavior:

    def __init__(self, status):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=1)
        self.status = status
        self.uuid = uuid.uuid4()
        self.message_queue = 'message_list'
        self.votes = 'votes_list'
        self.errors_queue = 'errors_queue'

    def pop_queue(self, queue):
        r = self.r
        if r.llen(queue) != 0:
            for i in range(r.llen(queue)):
                m = self.__pop(queue)
                r.delete(m)

    def vote(self, uuid):
        r = self.r
        self.__push(uuid, self.votes, 'candidate')
        if r.lindex(self.votes, 0) == str(uuid).encode('ascii') and r.get('heartbeat') == None:
            return True
        return False

    def __push(self, key, queue, message):
        r = self.r
        r.set(key, message)
        return r.rpush(queue, key)

    def __pop(self, queue):
        r = self.r
        m = r.lpop(queue)
        if m is not None:
            print('Key:', m, 'Value:', r.get(m))
            return m

    def produce(self):
        time.sleep(message_speed)
        s = [random.choices(string.ascii_uppercase)[0] for i in range(message_length)]
        s = ''.join(s)
        self.__push(s, self.message_queue, 'random')

    def consume(self):
        m = self.__pop(self.message_queue)
        # if m is not None:
        if m:
            error_probability = random.randrange(1, 101)
            if error_probability <= 5:
                print('Error with key: {}'.format(m))
                self.__push(m, self.errors_queue, 'error')

    def run(self):
        r = self.r
        while True:
            if self.status is 'master':
                print('I am master')
                self.produce()
                r.psetex('heartbeat', 1300, 'alive')
                self.pop_queue(self.votes)
            elif self.status is 'slave':
                self.consume()
                if r.get('heartbeat') is None:
                    print('No heartbeat')
                    sleep_time = random.randrange(1, 4)
                    time.sleep(sleep_time)
                    if self.vote(self.uuid):
                        self.status = 'master'
            elif self.status == 'GetErrors':
                self.pop_queue(self.errors_queue)
                print('End of errors')
                break


if __name__ == '__main__':
    try:
        status = sys.argv[1]
        if status != 'GetErrors':
            status = 'slave'

    except IndexError:
        status = 'slave'

    app = Behavior(status)
    app.run()


'''
    1. PyCharm же тебе подсказывает, что None нужно проверять как is и is not.  
    2. Я бы получение случайного числа делал только в случае, если из очереди получилось 
    что-то достать, чтобы не грузить проц почем зря.
'''