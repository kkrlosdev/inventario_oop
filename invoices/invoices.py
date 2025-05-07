from clients.client import Client
from inventory.inventory_manager import InventoryManager
from .invoice_item import InvoiceItem

inventory_manager = InventoryManager()

class Invoice:
    def __init__(self, invoice_id, invoice_date, invoice_client: Client, products: list[InvoiceItem]):
        self.id = invoice_id
        self.date = invoice_date
        self.invoice_client = invoice_client
        self.products = products
        self.subtotal = 0
        self.state = True
        self.inventory = inventory_manager.inventory_stock

    def calculate_total(self):
        self.subtotal = sum(product.get_total() for product in self.products)

    def __str__(self):
        format_products = "\n".join(f"- {item.product.product_name} | {item.units_sold} uds | {item.discount_percentage}% = ${item.get_total():,.2f}" for item in self.products)
        format_message = f"""> {self.date} | {self.id}
Cliente: {self.invoice_client.name}
Documento: {self.invoice_client.document}
Contacto: {self.invoice_client.phone_number}
Productos:
{format_products}
Total facturado: $ {self.subtotal:,.2f}"""
        return format_message
