import struct

scheme = {b'\x12': 'ON', b'\x13': 'OFF', b'\x20': 'COLOR'}
# Cache this struct definition
int_struct = struct.Struct("<H")
rgb_struct = struct.Struct("<BBB")
_UNPACK_INT = int_struct.unpack
_PACK_INT = int_struct.pack
_UNPACK_RGB = rgb_struct.unpack
_PACK_RGB = rgb_struct.pack
