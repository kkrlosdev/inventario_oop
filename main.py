from colorama import init
from inventory.inventory_manager import InventoryManager
from inventory.class_inventory import ClassInventory
from inventory.units import Units
from inventory.product import Product
from clients.client import Client
from invoices.invoice_item import InvoiceItem
from invoices.invoices import Invoice
import datetime

init(autoreset=True)

bolsas = Units('bolsas', 'Bolsas para empaque', 'Bolsas para empaque')
alimentos = ClassInventory('Comestible', 'Empacados')
pan_bimbo = Product('Pan Bimbo Artesanal', 'Bimbo SAS', '2025-04-03', bolsas, alimentos)
inventory_manager = InventoryManager()
# print(inventory_manager.check_stock(pan_bimbo))
# print(inventory_manager.add_stock(pan_bimbo, 25, 10000, False))
# print(inventory_manager.add_stock(pan_bimbo, 25, 10000, False))
# print(inventory_manager.check_stock(pan_bimbo))
# print(pan_bimbo)
farmacaps = Client('1000112', 'Roberto Mélendez', '10004575', 'Carrera 42. Avenida Nopales', '3001636', True)
lote_1120 = InvoiceItem(pan_bimbo, 100, 10000, False)
fact_fn_2255 = Invoice('12220021', str(datetime.date.today()), farmacaps, [lote_1120])
fact_fn_2255.calculate_total()
print(fact_fn_2255.subtotal)
print(fact_fn_2255.date)