from .invoice_item import InvoiceItem

class Invoice:
    def __init__(self, invoice_date: str, id_invoice_client: int, products: list[InvoiceItem]):
        self.date = invoice_date
        self.invoice_client = id_invoice_client
        self.products = products
        self.subtotal = 0
        self.state = True

    def calculate_total(self):
        self.subtotal = sum(product.get_total() for product in self.products)