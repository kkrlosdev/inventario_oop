from dataclasses import dataclass
from entities.base_entity import BaseEntity

@dataclass
class ClassInventory(BaseEntity):
    name: str