class Client:
    def __init__(self, id_client: int, name: str, document: str, address: str, phone_number: str, is_company: bool):
        self.id_client = id_client
        self.name = name
        self.document = document
        self.address = address
        self.phone_number = phone_number
        self.is_company = is_company

    def update_info(self, **data):
        if 'name' in data and isinstance(data['name'], str):
            self.name = data['name']
        if 'document' in data and isinstance(data['document'], str):
            self.document = data['document']
        if 'address' in data and isinstance(data['address'], str):
            self.address = data['address']
        if 'phone_number' in data and isinstance(data['phone_number'], str):
            self.phone_number = data['phone_number']
        if 'is_company' in data and isinstance(data['is_company'], bool):
            self.is_company = data['is_company']

    def __str__(self):
        return f'ID: {self.id_client}\nNombre: {self.name}\nNúmero de documento: {self.document}\nDirección: {self.address}\nNúmero teléfonico: {self.phone_number}\nRepresentante legal? {self.is_company}'
