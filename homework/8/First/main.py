import sys
import time
import string
import random
import redis

message_speed = 1  # in seconds
message_length = 4
channels = {
            'messages': 'messages-ch',
            'votes': 'votes-ch'
            }


class Behavior:

    def __init__(self, status):
        self.status = status
        self.r = redis.StrictRedis(host='localhost', port=6379, db=1)
        self.queue = 'message_list'

    def __decode(self, s):
        return s.decode('utf-8')

    def __push(self, key):
        r = self.r
        return r.rpush(self.queue, key)

    def produce(self):
        r = self.r
        while True:
            time.sleep(message_speed)
            s = [random.choices(string.ascii_uppercase)[0] for i in range(message_length)]
            s = ''.join(s)
            r.set(s, 'published')
            self.__push(s)

    def consume(self):
        r = self.r
        queue = self.queue
        while True:
            while (r.llen(queue) != 0):
                print(r.lpop(queue))

    def cadidate_rally(self):
        ...


if __name__ == '__main__':

    try:
        status = sys.argv[1]

    except IndexError:
        status = 'slave'
        app = Behavior(status)

    if status == 'master':
        app = Behavior(status)
        app.produce()
    app = Behavior(status)
    app.consume()


