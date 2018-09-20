from protocol import scheme
from test import t_cases


class Lamp:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = '9999'
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


if __name__ == '__main__':
    s = """
CASE# {}
MESSAGE: {}
EXPECTED: {}
PASSED: {}
    """

    def itter_message(m):
        result = []
        a = Lamp()
        for i in a.get_message(m):
            result.append(i)
        return result


    for i in t_cases:
        message = b''.join(t_cases[i]['message'])
        try:
            result = itter_message(message)
            [print('LAMP action:', i) for i in result]

        except:
            result = False
        print(s.format(
                i,
                t_cases[i]['message'],
                t_cases[i]['expected_result'],
                result == t_cases[i]['expected_result']
                )
            )
