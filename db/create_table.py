import connection

def execute_table_creation(query: str, table_name: str):
    conn = connection.get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print(f"Tabla '{table_name}' creada exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error creando la tabla '{table_name}': {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()