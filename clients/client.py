from dataclasses import dataclass
from entities.base_entity import BaseEntity

@dataclass
class Client(BaseEntity):
    name: str
    document: str
    address: str
    phone_number: str
    is_company: bool = False

    def __str__(self):
        return f'ID: {self.id_client}\nNombre: {self.name}\nNúmero de documento: {self.document}\nDirección: {self.address}\nNúmero teléfonico: {self.phone_number}\nRepresentante legal? {self.is_company}'
