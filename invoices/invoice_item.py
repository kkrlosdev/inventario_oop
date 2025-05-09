from dataclasses import dataclass

@dataclass
class InvoiceItem:
    id_product: int
    units_sold: int
    unit_price: float | int
    discount_percentage: float = 0.0

    def get_total(self):
        total = self.units_sold * self.unit_price
        total = total * (1 - self.discount_percentage / 100)
        return total