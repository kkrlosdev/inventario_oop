from .units import Units
from .class_inventory import ClassInventory

class Product:
    def __init__(self, product_name: str, provider: str, expiration_date: str, storage_unit: Units, inventory_class: ClassInventory):
        self.inventory_class = inventory_class
        self.product_name = product_name
        self.provider = provider
        self.expiration_date = expiration_date
        self.storage_unit = storage_unit

    def __str__(self):
        return f'Nombre producto: {self.product_name}\nProveedor: {self.provider}\nFecha de expiración: {self.expiration_date}\nUnidad de almacenamiento: {self.storage_unit.code}\nClase de inventario: {self.inventory_class.name}'