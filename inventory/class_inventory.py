from dataclasses import dataclass
from entities.base_entity import BaseEntity

@dataclass
class ClassInventory(BaseEntity):
    inventory_type: str
    name: str