from db.connection import get_connection

class BaseDAO:
    def __enter__(self):
        # Se ejecuta al momento de abrir la conexión y crea la conexión y el cursor. Retorna el DAO
        self.connection = get_connection()
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Se ejecuta siempre al cierre de la operación; en caso de éxito hace commit, sino hace rollback. Para finalizar cierra conexión y cursor.
        if exc_type:
            self.connection.rollback()
        else:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()