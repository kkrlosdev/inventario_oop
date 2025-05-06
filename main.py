from colorama import init
from inventory.inventory_manager import InventoryManager
from inventory.class_inventory import ClassInventory
from inventory.units import Units
from inventory.product import Product

init(autoreset=True)

bolsas = Units('bolsas', 'Bolsas para empaque', 'Bolsas para empaque')
alimentos = ClassInventory('Comestible', 'Empacados')
pan_bimbo = Product('Pan Bimbo Artesanal', 'Bimbo SAS', '2025-04-03', bolsas, alimentos)
inventory_manager = InventoryManager()
# print(inventory_manager.check_stock(pan_bimbo))
# print(inventory_manager.add_stock(pan_bimbo, 25, 10000, False))
# print(inventory_manager.add_stock(pan_bimbo, 25, 10000, False))
print(inventory_manager.check_stock(pan_bimbo))
print(pan_bimbo)