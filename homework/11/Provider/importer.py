import psycopg2
from provider import Provider
from db_controller import ControlDb
from server import get_data_from_db

"""
    Importer
    - Получает данные по курсам валют и проверяет валидность данных (Check Integrity)
    - Записывает или обновляет данные в базе(Transaction)
    - Дополняет граф валют до полного(Import Algorithm)
"""

def get_data_from_provider_update_db(connection, control):
    # Получаем данные от провайдера
    p = Provider()
    data = p.get_data()

    # Записываем данные в базу
    cur = connection.cursor()
    r = control.upsert_request(data)
    cur.execute(r)
    conn.commit()
    cur.close()
    return data


if __name__ == '__main__':
    '''
        Команды по управлению сервером
        pg_ctl -D /usr/local/var/postgres start
        pg_ctl -D /usr/local/var/postgres status
        Интерактивная консоль базы: psql postgres
        pg_ctl -D /usr/local/var/postgres stop

    '''
    try:
        conn = psycopg2.connect("dbname=postgres user=vbaryshev")
        # CASES:
        e = ControlDb()
        inside = get_data_from_provider_update_db(conn, e)
        out = get_data_from_db(conn, e)
        print('TEST STATUS:', inside == out)
    finally:
        conn.close()
