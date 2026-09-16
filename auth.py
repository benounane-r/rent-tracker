import sqlite3

def register_landlord(name, email, phone, password, currency):
    conn = sqlite3.connect("rent_tracker.db")
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO landlords (name, email, phone, password, currency)
        VALUES (?, ?, ?, ?, ?)''', (name, email, phone, password, currency))
        conn.commit()
        print(f"landlord {name} is registered")
        return True
    except sqlite3.IntegrityError:
        print("Error: Email already exists.")
        return False
    finally:
        conn.close()

def register_tenant(property_id, name, phone, email, password, lease_start, lease_end):
    conn = sqlite3.connect("rent_tracker.db")
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO tenants (name, email, phone, password, property_id, lease_start, lease_end )
        vALUES(?,?,?,?,?,?,?)''',(name, email, phone, password, property_id, lease_start, lease_end) )
        conn.commit()
        print(f"Tenant {name} is registered")
        return True
    except sqlite3.IntegrityError:
        print("Error: email already exists.")
        return False
    finally:
        conn.close()


def login(email, password, user_type):
    conn = sqlite3.connect("rent_tracker.db")
    cursor = conn.cursor()

    table = "landlords" if user_type == "landlord" else "tenants"

    cursor.execute(f'''
        SELECT * FROM {table} WHERE email= ? AND password = ?''',(email, password))

    user = cursor.fetchone()
    conn.close()

    if user:
        print(f"login successful! welcome {user[1]}")
        return user
    else:
        print("login failed! invalid email or password")
        return None


if __name__ == "__main__":
    register_landlord("John Doe", "john.doe@example.com", "123-456-7890", "password123", "QR")
    login("john.doe@example.com", "password123", "landlord")