import psycopg2
from provider import Provider

"""
    Importer
    - Получает данные по курсам валют и проверяет валидность данных (Check Integrity)
    - Записывает или обновляет данные в базе(Transaction)
    - Дополняет граф валют до полного(Import Algorithm)
"""


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


if __name__ == '__main__':
    '''
        Команды по управлению сервером
        pg_ctl -D /usr/local/var/postgres start
        pg_ctl -D /usr/local/var/postgres status
        Интерактивная консоль базы: psql postgres
        pg_ctl -D /usr/local/var/postgres stop

    '''
    def get_data_from_provider_update_db():
        # Получаем данные от провайдера
        p = Provider()
        data = p.get_data()

        # Записываем данные в базу
        conn = psycopg2.connect("dbname=postgres user=vbaryshev")
        cur = conn.cursor()
        e = ControlDb()
        r = e.upsert_request(data)
        cur.execute(r)
        conn.commit()
        cur.close()
        conn.close()
        return data


    def get_data_from_db():
        # Получаем данные из базы
        conn = psycopg2.connect("dbname=postgres user=vbaryshev")
        cur = conn.cursor()
        e = ControlDb()
        r = e.select_request()
        cur.execute(r)
        row = cur.fetchone()
        result = []
        while row is not None:
            row = list(row)
            # row[2] = int(row[2])
            row[3] = int(row[3].timestamp())
            result.append(row)
            row = cur.fetchone()
        cur.close()
        conn.close()
        return result


    # CASES:
    inside = get_data_from_provider_update_db()
    out = get_data_from_db()
    # print(inside)
    # print(out)
    print('TEST STATUS:', inside == out)


