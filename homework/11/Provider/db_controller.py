class ControlDb:
    def __init__(self):
        self.upload_template =  """insert into rate
                            values{vals}
                            ON CONFLICT (cur1, cur2)
                            DO UPDATE SET
                            uploadtime = EXCLUDED.uploadtime,
                            rate = EXCLUDED.rate;"""

        self.request_tempelate = """select * from rate;"""

    def upsert_request(self, data):
        v = (["('{}', '{}', {}, to_timestamp({}))".format(*i) for i in data])
        v = ','.join(v)
        return self.upload_template.format(vals=v)

    def select_request(self):
        return self.request_tempelate