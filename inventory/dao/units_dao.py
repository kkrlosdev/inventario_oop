from entities.base_dao import BaseDAO
from inventory.units import Units

class UnitsDAO(BaseDAO):
    def create_unit(self, unit: Units):
        query = "INSERT INTO units (name, code) VALUES (%s, %s)"
        params = (unit.name, unit.code)
        self._execute_query(query, params)

    def delete_unit(self, unit_id: int):
        query = "DELETE FROM units WHERE id_unit = %s"
        params = (unit_id,)
        self._execute_query(query, params)

    def update_unit(self, unit_id: int, unit_data: Units):
        query = "UPDATE units SET name = %s, code = %s WHERE id_unit = %s"
        params = (unit_data.name, unit_data.code, unit_id)
        self._execute_query(query, params)

    def get_all_units(self) -> list[dict]:
        query = "SELECT * FROM units"
        data = self._execute_query(query, None, 'all')
        return data