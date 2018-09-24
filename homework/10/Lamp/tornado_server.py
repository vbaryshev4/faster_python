import asyncio
import logging
import os
from tornado.iostream import StreamClosedError
from tornado.ioloop import IOLoop
from tornado.tcpserver import TCPServer
from tornado.options import options as tornado_options
from protocol import _PACK_INT

PORT = 10000
# This is just to configure Tornado logging.
tornado_options.parse_command_line()
logger = logging.getLogger(os.path.basename(__file__))


def build_msg():
    msg_type = b'\x20'
    msg_len = _PACK_INT(3)
    msg_val = b'\xff\x00\x00'
    msg = b''.join([msg_type, msg_len, msg_val])
    return msg


class MyServer(TCPServer):
    async def handle_stream(self, stream, address):
        logging.info("Connection from peer")
        try:
            msg = build_msg()
            while True:
                logging.info("Sending message...")
                await stream.write(msg)
                await asyncio.sleep(3)

        except StreamClosedError:
            logger.error("%s disconnected", address)


server = MyServer()
server.listen(PORT)
loop = IOLoop.current()
loop.start()
