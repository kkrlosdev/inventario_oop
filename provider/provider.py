from dataclasses import dataclass
from entities.base_entity import BaseEntity

@dataclass
class Provider(BaseEntity):
    name: str
    contact_name: str
    nit: str
    phone: str
    email: str