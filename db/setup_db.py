from create_table import execute_table_creation

def create_inventory_class_table():
    query = """
    CREATE TABLE IF NOT EXISTS inventory_class(
                id_inventory SERIAL PRIMARY KEY,
                name VARCHAR(50) UNIQUE NOT NULL
                );
    """
    execute_table_creation(query, 'inventory_class')

def create_units_table():
    query = """
    CREATE TABLE IF NOT EXISTS units(
    id_unit SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    code VARCHAR(20) UNIQUE NOT NULL
    );
    """
    execute_table_creation(query, 'units')

def create_provider_table():
    query = """
    CREATE TABLE IF NOT EXISTS provider(
    id SERIAL PRIMARY KEY,
    name VARCHAR(300) NOT NULL,
    contact_name VARCHAR(200) NOT NULL,
    nit VARCHAR(200),
    phone VARCHAR(200) NOT NULL,
    email VARCHAR(200) NOT NULL
    );
    """
    execute_table_creation(query, 'provider')

def create_client_table():
    query = """
    CREATE TABLE IF NOT EXISTS client(
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL UNIQUE,
    address VARCHAR(500),
    email VARCHAR(200) UNIQUE,
    phone_number VARCHAR(200) UNIQUE NOT NULL,
    is_company BOOLEAN DEFAULT FALSE
    );
    """
    execute_table_creation(query, 'client')

def create_products_table():
    query = """
    CREATE TABLE IF NOT EXISTS products(
    id_product SERIAL PRIMARY KEY,
    product_name VARCHAR(500) NOT NULL,
    expiration_date DATE,
    provider_id INTEGER REFERENCES provider(id)
    );
    """
    execute_table_creation(query, 'products')

def create_invoice_item_table():
    query = """
    CREATE TABLE IF NOT EXISTS invoice_item(
    id_invoice_item SERIAL PRIMARY KEY,
    id_invoice INTEGER REFERENCES invoice(id_invoice),
    id_product INTEGER REFERENCES products(id_product),
    units_sold INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    discount_percentage DECIMAL(5, 2) DEFAULT 0.00
    );
    """
    execute_table_creation(query, 'invoice_item')

def create_invoices_table():
    query = """
    CREATE TABLE IF NOT EXISTS invoice(
    id_invoice SERIAL PRIMARY KEY,
    invoice_date DATE NOT NULL,
    id_invoice_client INTEGER REFERENCES client(id),
    subtotal DECIMAL(10, 2) DEFAULT 0.00,
    discount_percentage DECIMAL(5, 2) DEFAULT 0.00,
    total DECIMAL(10, 2) DEFAULT 0.00,
    state BOOLEAN DEFAULT TRUE
    );
    """
    execute_table_creation(query, 'invoice')

if __name__ == '__main__':
    create_inventory_class_table()
    create_units_table()
    create_provider_table()
    create_client_table()
    create_products_table()
    create_invoices_table()
    create_invoice_item_table()
    print('Se crearon todas las tablas exitosamente!')