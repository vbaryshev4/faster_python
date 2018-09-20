t_cases = {
            1: {'message': [
                    b'\x12', b'\x00\x00',
                    b'\x20', b'\x00\x03', b'\xff\x00\x00',
                    b'\x13', b'\x00\x00',
                    b'\x12', b'\x00\x00',
                    b'\x20', b'\x00\x03', b'\x19\x00\xff',
                    b'\x12', b'\x00\x00'
                    ],
                'expected_result': [
                    ('ON', b''),
                    ('COLOR', b'\xff\x00\x00'),
                    ('OFF', b''),
                    ('ON', b''),
                    ('COLOR', b'\x19\x00\xff'),
                    ('ON', b'')
                    ]
                },
            2: {'message': [
                    b'\x00', b'\x00\x00',
                    b'\x20', b'\x00\x03', b'\xff\x37\x00',
                    b'\x00', b'\x00\x00'
                ],
                'expected_result': [
                    ('COLOR', b'\xff\x37\x00')
                ]
                },
            3: {'message': [
                    b''
                ],
                'expected_result': []
                },
            4: {'message': [
                    b'\x00', b'\x10\x00',
                    b'\x00', b'\x30\x00',
                    b'\x00', b'\x40\x00',
                    b'\x00', b'\x50\x00'
                ],
                'expected_result': []
            }
        }