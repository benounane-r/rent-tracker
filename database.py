import sqlite3

def create_database():
    conn = sqlite3.connect("rent_tracker.db")
    cursor = conn.cursor()

    # Landlords
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS landlords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Properties
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS properties (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            landlord_id INTEGER NOT NULL,
            address TEXT NOT NULL,
            rent_amount REAL NOT NULL,
            FOREIGN KEY (landlord_id) REFERENCES landlords(id)
        )
    ''')

    # Tenants
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tenants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            property_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            lease_start TEXT NOT NULL,
            lease_end TEXT NOT NULL,
            FOREIGN KEY (property_id) REFERENCES properties(id)
        )
    ''')

    # Payments
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tenant_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            status TEXT NOT NULL,
            proof_path TEXT,
            FOREIGN KEY (tenant_id) REFERENCES tenants(id)
        )
    ''')

    # Maintenance
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS maintenance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            property_id INTEGER NOT NULL,
            tenant_id INTEGER NOT NULL,
            request TEXT NOT NULL,
            response TEXT,
            cost REAL,
            date TEXT NOT NULL,
            FOREIGN KEY (property_id) REFERENCES properties(id),
            FOREIGN KEY (tenant_id) REFERENCES tenants(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database created successfully!")

create_database()


