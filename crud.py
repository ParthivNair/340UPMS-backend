from fastapi import HTTPException
from db import get_connection, convert_query


def create_tenant(first_name: str, last_name: str, phone_number: str, email: str):
    # Check if a tenant with the given email already exists.
    check_query = "SELECT tenantID FROM Tenants WHERE email = :emailInput;"
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            converted_check = convert_query(check_query)
            cursor.execute(converted_check, {"emailInput": email})
            if cursor.fetchone():
                raise HTTPException(status_code=400, detail="Email already registered")

            # Insert new tenant using your provided SQL query.
            insert_query = """
            INSERT INTO Tenants (firstName, lastName, phoneNumber, email) 
            VALUES (:firstNameInput, :lastNameInput, :phoneNumberInput, :emailInput);
            """
            converted_insert = convert_query(insert_query)
            cursor.execute(converted_insert, {
                "firstNameInput": first_name,
                "lastNameInput": last_name,
                "phoneNumberInput": phone_number,
                "emailInput": email
            })
            conn.commit()
            tenant_id = cursor.lastrowid
            return {
                "tenantID": tenant_id,
                "firstName": first_name,
                "lastName": last_name,
                "phoneNumber": phone_number,
                "email": email
            }
    finally:
        conn.close()


def get_tenants():
    query = "SELECT tenantID, firstName, lastName, phoneNumber, email FROM Tenants;"
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            converted_query = convert_query(query)
            cursor.execute(converted_query)
            return cursor.fetchall()
    finally:
        conn.close()


def update_tenant(tenant_id: int, first_name: str | None, last_name: str | None, phone_number: str | None,
                  email: str | None):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Retrieve the existing tenant.
            select_query = "SELECT * FROM Tenants WHERE tenantID = :tenantIDSelected;"
            converted_select = convert_query(select_query)
            cursor.execute(converted_select, {"tenantIDSelected": tenant_id})
            tenant = cursor.fetchone()
            if not tenant:
                raise HTTPException(status_code=404, detail="Tenant not found")

            # Determine the new values (retain existing value if none provided).
            new_first_name = first_name if first_name is not None else tenant["firstName"]
            new_last_name = last_name if last_name is not None else tenant["lastName"]
            new_phone_number = phone_number if phone_number is not None else tenant["phoneNumber"]
            new_email = email if email is not None else tenant["email"]

            # If the email is changed, ensure it isn’t already used by another tenant.
            if new_email != tenant["email"]:
                check_query = "SELECT tenantID FROM Tenants WHERE email = :emailInput AND tenantID != :tenantIDSelected;"
                converted_check = convert_query(check_query)
                cursor.execute(converted_check, {"emailInput": new_email, "tenantIDSelected": tenant_id})
                if cursor.fetchone():
                    raise HTTPException(status_code=400, detail="Email already registered to another tenant")

            # Update tenant using your provided SQL query.
            update_query = """
            UPDATE Tenants 
            SET firstName = :firstNameInput, lastName = :lastNameInput, 
                phoneNumber = :phoneNumberInput, email = :emailInput
            WHERE tenantID = :tenantIDSelected;
            """
            converted_update = convert_query(update_query)
            cursor.execute(converted_update, {
                "firstNameInput": new_first_name,
                "lastNameInput": new_last_name,
                "phoneNumberInput": new_phone_number,
                "emailInput": new_email,
                "tenantIDSelected": tenant_id
            })
            conn.commit()
            return {
                "tenantID": tenant_id,
                "firstName": new_first_name,
                "lastName": new_last_name,
                "phoneNumber": new_phone_number,
                "email": new_email
            }
    finally:
        conn.close()


def delete_tenant(tenant_id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Verify the tenant exists.
            select_query = "SELECT tenantID FROM Tenants WHERE tenantID = :tenantIDSelected;"
            converted_select = convert_query(select_query)
            cursor.execute(converted_select, {"tenantIDSelected": tenant_id})
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Tenant not found")

            # Delete the tenant.
            delete_query = "DELETE FROM Tenants WHERE tenantID = :tenantIDSelected;"
            converted_delete = convert_query(delete_query)
            cursor.execute(converted_delete, {"tenantIDSelected": tenant_id})
            conn.commit()
            return {"message": "Tenant deleted successfully"}
    finally:
        conn.close()
