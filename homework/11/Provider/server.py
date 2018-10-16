from flask import Flask
import psycopg2
import json
from db_controller import ControlDb

app = Flask(__name__)

def get_data_from_db(connection, control):
    # Получаем данные из базы
    cur = connection.cursor()
    r = control.select_request()
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
    return result


def connection(cache = []):
    if len(cache) == 0:
        conn = psycopg2.connect("dbname=postgres user=vbaryshev")
        cache.append(conn)
    return cache[0]


@app.route('/data')
def return_data():
    e = ControlDb()
    conn = connection()
    out = get_data_from_db(conn, e)
    return json.dumps(out)

