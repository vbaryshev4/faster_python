import logging
import os
from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError
from tornado.tcpclient import TCPClient
from tornado.options import options as tornado_options
from protocol import scheme, _UNPACK_INT, _UNPACK_RGB

PORT = 10000

# This is just to configure Tornado logging.
tornado_options.parse_command_line()
logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.INFO)
tcp_client = TCPClient()


async def read_lru_msg(stream):
    msg_type = await stream.read_bytes(1)
    msg_length = await stream.read_bytes(2)
    # Convert from network order to int.
    length = _UNPACK_INT(msg_length)[0]
    msg_value = await stream.read_bytes(length)
    return msg_type, msg_value


async def client():
    try:
        stream = await tcp_client.connect('localhost', PORT)
        while True:
            msg_type, msg_val = await read_lru_msg(stream)
            type_str = scheme[msg_type]
            logger.info('type: %s' % type_str)
            if type_str == "COLOR":
                msg_val = _UNPACK_RGB(msg_val)
                logger.info('#%02x%02x%02x' % msg_val)

    except StreamClosedError as exc:
        print("error connecting")

loop = IOLoop.current()
loop.spawn_callback(client)
loop.start()
