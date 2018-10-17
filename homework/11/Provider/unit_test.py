import time

from provider import Provider
from server import connection
from db_controller import ControlDb

## from Clients.client import ...

template = '''
            Item: {}
            from: {}
            test-status: {}
            '''

def equality(arg1, arg2):
    if arg1 == arg2:
        return True
    else:
        return False

def test_provider():
    unix_time = int(time.time())
    test = Provider()
    t = test.get_data()[0][3]
    result = equality(t, unix_time)
    print(template.format(test.__class__, test.__module__, result))


def test_connection():
    test = connection()
    result = equality(test.closed, 0)
    print(template.format(connection.__class__, connection.__module__, result))

    dsn = 'dbname=postgres user=vbaryshev'
    result = equality(test.dsn, dsn)
    print(template.format(connection.__class__, connection.__module__, result))


def control_db():
    t = ControlDb('any_other_table')
    result = equality(t.table, 'any_other_table')
    print(template.format(t.__class__, t.__module__, result))
    result = equality(t.select_request(), 'select * from any_other_table;')
    print(template.format(t.__class__, t.__module__, result))

    t = ControlDb()
    result = equality(t.table, 'rate')
    print(template.format(t.__class__, t.__module__, result))

    data = [['EUR', 'EUR', 1.0, 1539789352]]
    expected_data = ['insert', 'into', 'rate',
                    "values('EUR',", "'EUR',",
                    '1.0,', 'to_timestamp(1539789352))',
                    'ON', 'CONFLICT', '(cur1,', 'cur2)',
                    'DO', 'UPDATE', 'SET', 'uploadtime',
                    '=', 'EXCLUDED.uploadtime,', 'rate',
                    '=', 'EXCLUDED.rate;']
    result = equality(t.upsert_request(data).split(), expected_data)
    print(template.format(t.__class__, t.__module__, result))


if __name__ == '__main__':
    template = '''
                Item: {}
                from: {}
                test-status: {}
                '''

    test_provider()
    test_connection()
    control_db()
