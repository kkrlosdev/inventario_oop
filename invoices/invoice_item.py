from dataclasses import dataclass
from inventory.product import Product

@dataclass
class InvoiceItem:
    product: Product
    units_sold: int
    unit_price: float | int
    discount_applied: bool

    def get_total(self):
        total = self.units_sold * self.unit_price
        return total