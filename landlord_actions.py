import sqlite3
#adding property
def addProperty(Landlord_id, address, rent_amount):
    conn = sqlite3.connect("rent_tracker.db")
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO properties (landlord_id, address, rent_amount)
        VALUES (?,?,?)''', (Landlord_id, address, rent_amount))

    conn.commit()
    conn.close()
    print(f"property '{address}' has been added successfully ")

#veiwing property 
def viewProperty(landlord_id):
    conn = sqlite3.connect("rent_tracker.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT tenants.name, tenants.phone , tenants.email, properties.address, tenants.lease_start, tenants.lease_end 
        FROM tenants
        JOIN properties ON tenants.property_id = properties.ID
        WHERE properties.landlord_id = ?''',(landlord_id,))
    tenants = cursor.fetchall()
    conn. close()

    if tenants :
        print("--Your Tenants--")
        for index in tenants:
            print(f"Tenant Name : {index[0]} Tenant Phone number : {index[1]} Tenant email : {index[2]} \n address : {index[3]} Lease start : {index[4]} Lease end: {index[5]}")
    else :
        print("You have no current tenants.")


# recording the paymenst 
def recordPayment(tenant_id, amount, date, status):
    conn = sqlite3.connect("rent_tracker.db")
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO payments (tenant_id, amount, date, status)
    VALUES (?, ?, ?, ?)''', (tenant_id, amount, date, status))

    conn.commit()
    conn.close()

    print(f"Payment of {amount} TL has been recorded successfully")
    

#viewing payment
def viewPayments(landlord_id):
    conn = sqlite3.connect("rent_tracker.db")
    cursor= conn.cursor()

    cursor.execute('''SELECT tenants.name, payments.amount, payments.date, payments.status 
    FROM payments
    JOIN tenants ON payments.tenant_id = tenants.id
    JOIN properties ON tenants.property_id = properties.id
    WHERE properties.landlord_id = ?''',(landlord_id,))
    payments  =cursor.fetchall()
    conn.close()

    if payments:
        print ("--Payment History--")
        for index in payments:
            print(f"Tenant name : {index[0]} | Payment amount : {index[1]} | Date : {index[2]} | Status : {index[3]}")
    else:
        print("No payments found for your properties.")

    return payments


# Test it
if __name__ == "__main__":
    addProperty(1, "123 Istanbul Street, Besiktas", 5000)
    viewProperty(1)
    recordPayment(1, 5000, "2026-09-01", "paid")
    viewPayments(1)