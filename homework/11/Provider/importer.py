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
        self.template =  """insert into rate
                            values{vals}
                            ON CONFLICT (cur1, cur2)
                            DO UPDATE SET
                            uploadtime = EXCLUDED.uploadtime,
                            rate = EXCLUDED.rate;"""

    def create_request(self, data):
        v = (["('{}', '{}', {}, to_timestamp({}))".format(*i) for i in data])
        v = ','.join(v)
        return self.template.format(vals=v)


if __name__ == '__main__':
    '''
        Команды по управлению сервером
        pg_ctl -D /usr/local/var/postgres start
        pg_ctl -D /usr/local/var/postgres status
        Интерактивная консоль базы: psql postgres
        pg_ctl -D /usr/local/var/postgres stop

    '''
    p = Provider()
    data = p.get_data()
    conn = psycopg2.connect("dbname=postgres user=vbaryshev")
    cur = conn.cursor()
    e = ControlDb()
    r = e.create_request(data)
    cur.execute(r)
    conn.commit()
    cur.close()
    conn.close()


