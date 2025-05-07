from dataclasses import dataclass
from inventory.product import Product

@dataclass
class InvoiceItem:
    product: Product
    units_sold: int
    unit_price: float | int
    discount_percentage: float = 0.0

    def get_total(self):
        total = self.units_sold * self.unit_price
        total = total * (1 - self.discount_percentage / 100)
        return total