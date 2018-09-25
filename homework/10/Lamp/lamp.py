from protocol import scheme
from test import t_cases
import socket
import sys

lamp_port = 9999
host = 'localhost'

class Lamp:
    def __init__(self):
        self.host = host
        self.port = lamp_port
        self.scheme = scheme

    def get_message(self, message):
        while True:
            length = 0
            if len(message) < 3:
                return None
            if message[0] in self.scheme.keys():
                length = int.from_bytes(message[1:3], byteorder='big')
                yield (self.scheme[message[0]], message[3:3+length])
            message = message[3+length:]  # Переделать в виде генератора


def consume():
    sock = socket.socket()
    sock.bind(('', lamp_port))
    sock.listen()
    conn, addr = sock.accept()
    print('connected:', addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        result = []
        a = Lamp()
        for i in a.get_message(data):
            result.append(i)
        [print('LAMP action:', i) for i in result]
        conn.send(b'got a message') # Заготовка под подтверждение о получении сообщения
    return conn.close()


if __name__ == '__main__':

    def itter_message(m):
        result = []
        a = Lamp()
        for i in a.get_message(m):
            result.append(i)
        return result

    try:
        if sys.argv[1] == 'test':
            s = """ 
                CASE# {} 
                MESSAGE: {} 
                EXPECTED: {} 
                PASSED: {}
                """

            for i in t_cases:
                message = b''.join(t_cases[i]['message'])
                try:
                    result = itter_message(message)
                    [print('LAMP action:', i) for i in result]

                except IndexError:
                    result = False
                print(s.format(
                        i,
                        t_cases[i]['message'],
                        t_cases[i]['expected_result'],
                        result == t_cases[i]['expected_result']
                        )
                    )

    except IndexError:
        while True:
            consume()  # запуск конзумера Лампы