from dataclasses import dataclass
from entities.base_entity import BaseEntity

@dataclass
class Units(BaseEntity):
    code: str
    name: str