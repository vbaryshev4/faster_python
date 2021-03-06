import socket
from test import t_cases

lamp_port = 9999
host = 'localhost'

if __name__ == '__main__':

    def send(message):
        sock.send(message)
        result = sock.recv(1024) # Заготовка под подтверждение о получении сообщения
        if result:
            print(result)

    sock = socket.socket()
    sock.connect((host, lamp_port))

    for i in t_cases:
        m = b''.join(t_cases[i]['message'])
        send(m)

    sock.close()