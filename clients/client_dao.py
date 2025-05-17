from entities.base_dao import BaseDAO
from .client import Client

class ClientDAO(BaseDAO):
    def add_client(self, client: Client):
        query = """
                INSERT INTO client(name, address, email, phone_number, is_company)
                VALUES (%s, %s, %s, %s, %s)
                """
        params = (client.name, client.address, client.email, client.phone_number, client.is_company)
        try:
            self._execute_query(query, params)
        except Exception as e:
            raise Exception(f'Ocurrió una excepción al momento de agregar el cliente: {e}')

    def delete_client(self, client_id: int):
        query = """DELETE FROM client WHERE id = %s"""
        params = (client_id,)
        try:
            self._execute_query(query, params)
            return f'Se eliminó el cliente exitosamente: {client_id}'
        except Exception as e:
            raise Exception(f'Ocurrió una excepción al momento de eliminar el cliente: {e}')
    
    def update_client(self, client_id: int, client_data: Client):
        query = """
                UPDATE client
                SET name = %s, address = %s, email = %s, phone_number = %s, is_company = %s
                WHERE id = %s
                """
        params = (client_data.name, client_data.address, client_data.email, client_data.phone_number, client_data.is_company, client_id)
        try:
            self._execute_query(query, params)
        except Exception as e:
            raise Exception(f'Ocurrió una excepción al momento de actualizar la información del cliente: {e}')

    def get_client_data(self, client_id):
        query = """
                SELECT name, address, email, phone_number, is_company
                FROM client
                WHERE id = %s;
                """
        params = (client_id,)
        try:
            data = self._execute_query(query, params, 'one')
            return data
        except Exception as e:
            raise Exception(f'Ocurrió una excepción tratando de recuperar la información del cliente: {e}')

    def get_all_clients(self):
        query = "SELECT name, address, email, phone_number, is_company FROM client;"
        return self._execute_query(query, None, 'all')