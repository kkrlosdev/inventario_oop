from db.connection import get_connection
from utils.fetchall_as_dict import fetchall_as_dict
from utils.fetchone_as_dict import fetchone_as_dict

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

    def _execute_query(self, query, params=None, mode=None):
        """
        Ejecuta una consulta SQL.

        # Params:
        - query: la consulta SQL.
        - params: los parámetros para la consulta.
        - mode: 'one' para fetchone, 'all' para fetchall, None para operaciones tipo INSERT/UPDATE/DELETE.
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            if mode == "one":
                return fetchone_as_dict(cursor)
            elif mode == "all":
                return fetchall_as_dict(cursor)
        except:
            raise
        finally:
            cursor.close()