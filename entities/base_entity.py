from dataclasses import dataclass, field, fields

@dataclass
class BaseEntity:
    def update_info(self, **data):
        for f in fields(self):
            if f.name in data and isinstance(data[f.name], f.type):
                setattr(self, f.name, data[f.name])