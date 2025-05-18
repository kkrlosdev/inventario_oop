from entities.base_dao import BaseDAO
from inventory.class_inventory import ClassInventory

class ClassInventoryDAO(BaseDAO):
    def create_inventory_class(self, inventory_class: ClassInventory):
        query = "INSERT INTO inventory_class (name) VALUES (%s)"
        params = (inventory_class.name,)
        self._execute_query(query, params)

    def delete_inventory_class(self, id_inventory_class: int):
        query = "DELETE FROM inventory_class WHERE id_inventory = %s"
        params = (id_inventory_class,)
        self._execute_query(query, params)

    def update_inventory_class(self, id_inventory_class: int, inventory_class_data: ClassInventory):
        query = """UPDATE inventory_class SET name = %s"""
        params = (inventory_class_data.name,)
        self._execute_query(query, params)

    def get_inventory_classes(self) -> list[dict]:
        query = "SELECT * FROM inventory_class"
        data = self._execute_query(query, None, 'all')
        return data