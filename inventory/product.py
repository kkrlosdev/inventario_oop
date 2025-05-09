from entities.base_entity import BaseEntity
from dataclasses import dataclass

@dataclass
class Product(BaseEntity):
    product_name: str
    expiration_date: str
    id_provider: int
    id_storage_unit: int
    id_inventory_class: int