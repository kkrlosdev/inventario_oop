from typing import Any
import json
from .product import Product
from colorama import Fore

class InventoryManager:
    def __init__(self):
        self.inventory_stock: list[dict[Any, Any]] = []
        self.load_stock()

    def save_stock(self):
        with open('inventory.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.inventory_stock, ensure_ascii=False, indent=4))

    def load_stock(self):
        try:
            with open('inventory.json', 'r', encoding='utf-8') as file:
                self.inventory_stock = json.loads(file.read())
        except FileNotFoundError:
            with open('inventory.json', 'x', encoding='utf-8') as file:
                file.write('[]')
                self.inventory_stock = []

    def add_stock(self, product: Product, stock: int, unit_price: float | int, has_discount: bool) -> str:
        for inv in self.inventory_stock:
            if inv['product_name'] == product.product_name:
                inv['stock'] += stock
                inv['unit_price'] = unit_price
                inv['has_discount'] = has_discount
                self.save_stock()
                return f'{Fore.YELLOW}Stock updated for {product.product_name}.'

        inventory_data = {
            'product_name': product.product_name,
            'stock': stock,
            'unit_price': unit_price,
            'has_discount': has_discount
            }
        self.inventory_stock.append(inventory_data)
        self.save_stock()
        return f'{Fore.GREEN}Inventory added successfully.'

    def check_stock(self, product: Product):
        for _, inv in enumerate(self.inventory_stock):
            if inv.get('product_name') == product.product_name:
                stock: int = inv.get('stock', 0)
                return stock
        else:
            return 0