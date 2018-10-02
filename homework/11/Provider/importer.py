import psycopg2
from provider import Provider

"""
    2.1)Importer
        - Получает данные по курсам валют и проверяет валидность данных (Check Integrity)
        - Записывает или обновляет данные в базе(Transaction)
        - Дополняет граф валют до полного(Import Algorithm)
"""



if __name__ == '__main__':
    p = Provider()
    conn = psycopg2.connect("dbname=suppliers user=postgres password=postgres")