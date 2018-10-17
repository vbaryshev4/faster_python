'''

    1) Avoiding ORM

    2) Database request templates for writing and reading

'''


class ControlDb:
    def __init__(self, table_name='rate'):
        self.table = table_name
        self.upload_template = """insert into {table_}
                            values{vals}
                            ON CONFLICT (cur1, cur2)
                            DO UPDATE SET
                            uploadtime = EXCLUDED.uploadtime,
                            rate = EXCLUDED.rate;"""

        self.request_tempelate = """select * from {table_};"""

    def upsert_request(self, data):
        v = (["('{}', '{}', {}, to_timestamp({}))".format(*i) for i in data])
        v = ','.join(v)
        return self.upload_template.format(table_=self.table, vals=v)

    def select_request(self):
        return self.request_tempelate.format(table_=self.table)
