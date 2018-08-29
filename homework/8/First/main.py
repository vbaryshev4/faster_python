import sys
import time
import string
import random
import redis

message_speed = 1 # in seconds
message_length = 4
channels = {
            'messages': 'messages-ch',
            'votes': 'votes-ch'
            }


class Behavior:

    def __init__(self, status):
        self.status = status

    def produce(self):
        r = redis.StrictRedis(host='localhost', port=6379, db=1)
        while True:
            time.sleep(message_speed)
            s = [random.choices(string.ascii_uppercase)[0] for i in range(message_length)]
            s = ''.join(s)
            print(r.publish(channels['messages'], s), s)

    def consume(self):
        r = redis.StrictRedis(host='localhost', port=6379, db=1)
        p = r.pubsub()
        p.subscribe(channels['messages'])
        while True:
            time.sleep(message_speed)
            m = p.get_message()
            print(m)

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


'''
    Особенно нам интересен CAS
    В Питоне примерно так:
    
    def client_side_incr(pipe):
    ...     current_value = pipe.get('OUR-SEQUENCE-KEY')
    ...     next_value = int(current_value) + 1
    ...     pipe.multi()
    ...     pipe.set('OUR-SEQUENCE-KEY', next_value)
    
    r.transaction(client_side_incr, 'OUR-SEQUENCE-KEY')
    
    (это из документации redis-py: https://pypi.org/project/redis/ )
'''