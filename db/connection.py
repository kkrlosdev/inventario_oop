import psycopg2
from .config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname = DB_NAME,
            user = DB_USER,
            password = DB_PASSWORD,
            host = DB_HOST,
            port = DB_PORT
        )
        print(f'Conexión exitosa a la base de datos:\nNombre: {conn.info.dbname} | Host: {conn.info.host} | Puerto: {conn.info.port}')
        return conn
    except psycopg2.Error as e:
        print('Ocurrió un error conectando a la base de datos: ', e)
        return None