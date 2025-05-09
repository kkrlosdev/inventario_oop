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

# Unidades
bolsas = Units('bolsas', 'Bolsas para empaque', 'Bolsas para empaque')
botellas = Units('botellas', 'Botellas de vidrio', 'Botellas de vidrio')
cajas = Units('cajas', 'Cajas de cartón', 'Cajas para embalaje')
# Clases de inventario
alimentos = ClassInventory('Comestible', 'Empacados')
bebidas = ClassInventory('Bebidas', 'Líquidos')
electrodomesticos = ClassInventory('Electrodoméstico', 'Aparatos eléctricos')
# Productos
pan_bimbo = Product('Pan Bimbo Artesanal', 'Bimbo SAS', '2025-04-03', bolsas, alimentos)
jugo_naranja = Product('Jugo Natural de Naranja', 'JugoCorp', '2025-06-01', botellas, bebidas)
licuadora = Product('Licuadora Oster', 'Oster Inc.', '2025-12-15', cajas, electrodomesticos)

#inventory_manager = InventoryManager()
# print(inventory_manager.check_stock(pan_bimbo))
# print(inventory_manager.add_stock(pan_bimbo, 25, 10000, False))
# print(inventory_manager.add_stock(pan_bimbo, 25, 10000, False))
# print(inventory_manager.check_stock(pan_bimbo))
# print(pan_bimbo)
# farmacaps = Client('1000112', 'Roberto Mélendez', '10004575', 'Carrera 42. Avenida Nopales', '3001636', True)
# lote_1120 = InvoiceItem(pan_bimbo, 100, 10000)
# lote_1121 = InvoiceItem(licuadora, 25, 35000, 10)
# fact_fn_2255 = Invoice('12220021', str(datetime.date.today()), farmacaps, [lote_1120, lote_1121])
# fact_fn_2255.calculate_total()
# print(fact_fn_2255.subtotal)
# print(fact_fn_2255.date)
# print(fact_fn_2255)
producto1 = Product('Pepe', '2025-04-04', 1, 2, 3)
print(producto1.product_name)
producto1.update_info(product_name='Carlos')
print(producto1.product_name)