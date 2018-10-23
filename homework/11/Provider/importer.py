"""

    1) Receives data on exchange rates and checks the validity
    of the data (Check Integrity)
    
    2) Writes or updates data in the database (Transaction)

    3) Supplements the currency graph to the full (Import Algorithm)

"""


import psycopg2
from provider import Provider
from db_controller import ControlDb
from server import get_data_from_db
from build_graph import build_graph


def get_data_from_provider_update_db(connection, control):
    # Получаем данные от провайдера
    p = Provider()
    data = p.get_data()
    data = build_graph(data)

    # Записываем данные в базу
    cur = connection.cursor()
    r = control.upsert_request(data)
    cur.execute(r)
    conn.commit()
    cur.close()
    return data


if __name__ == '__main__':
    '''
        Run server:
        
            1) pg_ctl -D /usr/local/var/postgres start
            
            2) pg_ctl -D /usr/local/var/postgres status
            
            3) Интерактивная консоль базы: psql postgres
            
            4) pg_ctl -D /usr/local/var/postgres stop

    '''
    try:
        conn = psycopg2.connect("dbname=postgres user=vbaryshev")
        e = ControlDb()
        inside = get_data_from_provider_update_db(conn, e)
        out = get_data_from_db(conn, e)
        # print('IN', inside)
        # print('OUT', out)
        print('TRANSACTION STATUS:', inside == out)
    finally:
        conn.close()
