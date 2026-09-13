import sqlite3

#check rental info 
def viewRentalInfo(tenant_id):
    conn = sqlite3.connect("rent_tracker.db")
    cursor = conn.cursor()

    cursor.execute('''SELECT properties.rent_amount, properties.address, tenants.lease_start, tenants.lease_end 
    FROM tenants
    JOIN properties ON tenants.property_id = properties.id
    WHERE tenants.id = ?''',(tenant_id,))
    rent_info = cursor.fetchone()
    conn.close()
    if rent_info:
        print(f"----YOUR RENTAL INFORMATION----")
        print(f"Address: {rent_info[1]}")
        print(f"Rent Amount: {rent_info[0]} TL")
        print(f"Lease Start: {rent_info[2]}")
        print(f"Lease End: {rent_info[3]}")
    else :
        print("No rental information found.")


#viewing previous payments 
def viewPaymentHistory(tenant_id):
    conn = sqlite3.connect("rent_tracker.db")
    cursor = conn.cursor()

    cursor.execute('''SELECT payments.amount, payments.date, payments.status
    FROM payments
    WHERE payments.tenant_id=? 
    ORDER BY date DESC''',(tenant_id,))
    payment_history = cursor.fetchall()
    conn.close()

    if payment_history:
        print("---PAYMENT HISTORY---")
        for index in payment_history:
            print(f"Amount: {index[0]} TL | Date: {index[1]} | Status: {index[2]}")
    else:
        print("No payment history found.")

    return payment_history

#Maintenance request
def submitMaintenanceRequest(tenant_id, property_id, request):
    conn = sqlite3.connect("rent_tracker.db")
    cursor = conn.cursor()

    from datetime import date
    today =str(date.today())

    cursor.execute('''INSERT INTO maintenance (property_id, tenant_id,request,date)
    VALUES (?, ?, ?, ?)''', (property_id, tenant_id, request, today))
    conn.commit()
    conn.close()
    print("Maintenance request submitted successfully.")


#view maintenance request
def viewMaintenanceRequests(tenant_id):
    conn = sqlite3.connect("rent_tracker.db")
    cursor = conn.cursor()

    cursor.execute('''SELECT request, response, cost, date
    FROM maintenance
    WHERE tenant_id = ?
    ORDER BY date DESC''', (tenant_id,))

    maintenance_requests = cursor.fetchall()
    conn.close()

    if maintenance_requests:
        print("---MAINTENANCE REQUESTS---")
        for index in maintenance_requests:
            print(f"Request: {index[0]}")
            print(f"response: {index[1] if index[1] else 'Pending...'}")
            print(f"Cost: {index[2] if index[2] else 'To Be Determined'}")
            print(f"Date: {index[3]}")
    else:
        print("No maintenance requests found.")

    return maintenance_requests

#viewing landlord info
def viewLandlordInfo(tenant_id):
    conn = sqlite3.connect("rent_tracker.db")
    cursor = conn.cursor()

    cursor.execute('''SELECT landlords.name, landlords.phone, landlords.email
    FROM tenants
    JOIN properties ON tenants.property_id = properties.id
    JOIN landlords ON properties.landlord_id = landlords.id
    WHERE tenants.id = ?''', (tenant_id,))

    landlord_info = cursor.fetchone()
    conn.close()

    if landlord_info:
        print("---YOUR LANDLORD INFORMATION---")
        print(f"Name: {landlord_info[0]}")
        print(f"Phone: {landlord_info[1]}")
        print(f"Email: {landlord_info[2]}")
       
    else:
        print("No landlord information found.")

    return landlord_info

if __name__ == "__main__":
    viewRentalInfo(1)
    viewPaymentHistory(1)
    submitMaintenanceRequest(1, 1, "Kitchen sink is leaking")
    viewMaintenanceRequests(1)
    viewLandlordInfo(1)