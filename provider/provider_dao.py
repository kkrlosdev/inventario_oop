from entities.base_dao import BaseDAO
from .provider import Provider

class ProviderDAO(BaseDAO):
    def create_provider(self, provider: Provider):
        query = """
                INSERT INTO provider(name, contact_name, nit, phone, email)
                VALUES (%s, %s, %s, %s, %s)
                """
        params = (provider.name, provider.contact_name, provider.nit, provider.phone, provider.email)
        self._execute_query(query, params)

    def delete_provider(self, provider_id: int):
        query = "DELETE FROM provider WHERE id = %s"
        params = (provider_id,)
        self._execute_query(query, params)

    def update_provider(self, provider_id: int, provider_data: Provider):
        query = """
                UPDATE provider
                SET name = %s, contact_name = %s, nit = %s, phone = %s, email = %s
                WHERE id = $s;
                """
        params = (provider_data.name, provider_data.contact_name, provider_data.nit, provider_data.phone, provider_data.email, provider_id)
        self._execute_query(query, params)

    def get_provider_data(self, provider_id) -> dict:
        query = "SELECT name, contact_name, nit, phone, email FROM provider WHERE id = %s"
        params = (provider_id,)
        try:
            data = self._execute_query(query, params, 'one')
            return data
        except Exception as e:
            raise Exception(f'Ocurrió una excepción al momento de obtener la información del cliente: {e}')

    def get_all_providers(self) -> list[dict]:
        query = "SELECT name, contact_name, nit, phone, email FROM provider"
        try:
            data = self._execute_query(query, None, 'all')
            return data
        except Exception as e:
            raise Exception(f'Ocurrió una excepción al momento de obtener la información de clientes: {e}')
