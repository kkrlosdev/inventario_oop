from entities.base_dao import BaseDAO
from inventory.product import Product

class ProductDAO(BaseDAO):
    def create_product(self, product: Product):
        query = """
                INSERT INTO products (product_name, expiration_date, provider_id, storage_unit_id, inventory_class_id)
                VALUES (%s, %s, %s, %s, %s);
                """
        params = (product.product_name, product.expiration_date, product.id_provider, product.id_storage_unit, product.id_inventory_class)
        self._execute_query(query, params)

    def delete_product(self, product_id: int):
        query = "DELETE FROM products WHERE id = %s"
        params = (product_id,)
        self._execute_query(query, params)

    def update_product(self, product_id: int, product_data: Product):
        query = """
                UPDATE products
                SET product_name = %s, expiration_date = %s, provider_id = %s, storage_unit_id = %s, inventory_class_id = %s
                WHERE product_id = %s;
                """
        params = (product_data.product_name, product_data.expiration_date, product_data.id_provider, product_data.id_storage_unit, product_data.id_inventory_class, product_id)
        self._execute_query(query, params)

    def get_product_data(self, product_id: int) -> dict:
        query = """
            SELECT
                P.PRODUCT_NAME,
                TO_CHAR(P.EXPIRATION_DATE, 'YYYY-MM-DD') AS EXPIRATION_DATE,
                PRV.NAME AS PROVIDER_NAME,
                U.NAME AS STORAGE_UNIT,
                INV_CLS.NAME AS INVENTORY_CLASS
            FROM
                PRODUCTS P
                LEFT JOIN PROVIDER PRV ON P.PROVIDER_ID = PRV.ID
                LEFT JOIN UNITS U ON P.STORAGE_UNIT_ID = U.ID_UNIT
                LEFT JOIN INVENTORY_CLASS INV_CLS ON P.INVENTORY_CLASS_ID = INV_CLS.ID_INVENTORY
            WHERE
                P.ID_PRODUCT = %s;
            """
        params = (product_id,)
        try:
            data = self._execute_query(query, params, 'one')
            return data
        except Exception as e:
            raise Exception(f'Ocurrió una excepción al intentar recuperar la información del producto: {e}')

    def get_all_products(self) -> list[dict]:
        query = """
            SELECT
                P.PRODUCT_NAME,
                TO_CHAR(P.EXPIRATION_DATE, 'YYYY-MM-DD') AS EXPIRATION_DATE,
                PRV.NAME AS PROVIDER_NAME,
                U.NAME AS STORAGE_UNIT,
                INV_CLS.NAME AS INVENTORY_CLASS
            FROM
                PRODUCTS P
                LEFT JOIN PROVIDER PRV ON P.PROVIDER_ID = PRV.ID
                LEFT JOIN UNITS U ON P.STORAGE_UNIT_ID = U.ID_UNIT
                LEFT JOIN INVENTORY_CLASS INV_CLS ON P.INVENTORY_CLASS_ID = INV_CLS.ID_INVENTORY
            """
        try:
            data = self._execute_query(query, mode='all')
            return data
        except Exception as e:
            raise Exception(f'Ocurrió una excepción al intentar recuperar la información del producto: {e}')