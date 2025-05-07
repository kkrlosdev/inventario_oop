from clients.client import Client
from inventory.product import Product
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
