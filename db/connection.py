import psycopg2
from db import config

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname = config.DB_NAME,
            user = config.DB_USER,
            password = config.DB_PASSWORD,
            host = config.DB_HOST,
            port = config.DB_PORT
        )
        print(f'Conexión exitosa a la base de datos:\nNombre: {conn.info.dbname} | Host: {conn.info.host} | Puerto: {conn.info.port}')
        return conn
    except psycopg2.Error as e:
        print('Ocurrió un error conectando a la base de datos: ', e)
        return None