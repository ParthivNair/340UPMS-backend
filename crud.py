# crud.py
from db import get_connection
from pymysql.cursors import DictCursor

connection = get_connection()


# Tenant CRUD
def create_tenant(tenant_data: dict):
    """
    Inserts a new tenant into the Tenants table.
    Expects tenant_data with keys: firstName, lastName, phoneNumber, email.
    """
    query = """
    INSERT INTO Tenants (firstName, lastName, phoneNumber, email)
    VALUES (%(firstName)s, %(lastName)s, %(phoneNumber)s, %(email)s)
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query, tenant_data)
    connection.commit()
    tenantID = cursor.lastrowid
    cursor.close()
    return tenantID


def get_tenant(tenantID: int):
    """
    Returns a single tenant record by tenantID.
    """
    query = """
    SELECT tenantID, firstName, lastName, phoneNumber, email
    FROM Tenants
    WHERE tenantID = %(tenantID)s
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query, {"tenantID": tenantID})
    result = cursor.fetchone()
    cursor.close()
    return result


def get_tenants():
    """
    Returns all tenant records.
    """
    query = """
    SELECT tenantID, firstName, lastName, phoneNumber, email
    FROM Tenants
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def update_tenant(tenantID: int, tenant_data: dict):
    """
    Updates a tenant record identified by tenantID.
    Expects tenant_data with keys: firstName, lastName, phoneNumber, email.
    """
    query = """
    UPDATE Tenants
    SET firstName = %(firstName)s,
        lastName = %(lastName)s,
        phoneNumber = %(phoneNumber)s,
        email = %(email)s
    WHERE tenantID = %(tenantID)s
    """
    tenant_data["tenantID"] = tenantID
    cursor = connection.cursor()
    cursor.execute(query, tenant_data)
    connection.commit()
    cursor.close()


def delete_tenant(tenantID: int):
    """
    Deletes a tenant record by tenantID.
    """
    query = "DELETE FROM Tenants WHERE tenantID = %(tenantID)s"
    cursor = connection.cursor()
    cursor.execute(query, {"tenantID": tenantID})
    connection.commit()
    cursor.close()


# Property CRUD

def create_property(property_data: dict):
    """
    Inserts a new property into the Properties table.
    Expects property_data with keys: address, city, state, zipCode, propertyValue.
    """
    query = """
    INSERT INTO Properties (address, city, state, zipCode, propertyValue)
    VALUES (%(address)s, %(city)s, %(state)s, %(zipCode)s, %(propertyValue)s)
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query, property_data)
    connection.commit()
    propertyID = cursor.lastrowid
    cursor.close()
    return propertyID


def get_property(propertyID: int):
    """
    Returns a single property record by propertyID.
    """
    query = """
    SELECT propertyID, address, city, state, zipCode, propertyValue
    FROM Properties
    WHERE propertyID = %(propertyID)s
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query, {"propertyID": propertyID})
    result = cursor.fetchone()
    cursor.close()
    return result


def get_properties():
    """
    Returns all property records.
    """
    query = """
    SELECT propertyID, address, city, state, zipCode, propertyValue
    FROM Properties
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def update_property(propertyID: int, property_data: dict):
    """
    Updates a property record identified by propertyID.
    Expects property_data with keys: address, city, state, zipCode, propertyValue.
    """
    query = """
    UPDATE Properties
    SET address = %(address)s,
        city = %(city)s,
        state = %(state)s,
        zipCode = %(zipCode)s,
        propertyValue = %(propertyValue)s
    WHERE propertyID = %(propertyID)s
    """
    property_data["propertyID"] = propertyID
    cursor = connection.cursor()
    cursor.execute(query, property_data)
    connection.commit()
    cursor.close()


def delete_property(propertyID: int):
    """
    Deletes a property record by propertyID.
    """
    query = "DELETE FROM Properties WHERE propertyID = %(propertyID)s"
    cursor = connection.cursor()
    cursor.execute(query, {"propertyID": propertyID})
    connection.commit()
    cursor.close()


# Units CRUD

def create_unit(unit_data: dict):
    """
    Inserts a new unit into the Units table.
    Expects unit_data with keys: propertyID, unitNumber, unitType, status.
    """
    query = """
    INSERT INTO Units (propertyID, unitNumber, unitType, status)
    VALUES (%(propertyID)s, %(unitNumber)s, %(unitType)s, %(status)s)
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query, unit_data)
    connection.commit()
    unitID = cursor.lastrowid
    cursor.close()
    return unitID


def get_unit(unitID: int):
    """
    Returns a single unit record by unitID.
    """
    query = """
    SELECT unitID, propertyID, unitNumber, unitType, status
    FROM Units
    WHERE unitID = %(unitID)s
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query, {"unitID": unitID})
    result = cursor.fetchone()
    cursor.close()
    return result


def get_units():
    """
    Returns all unit records.
    """
    query = """
    SELECT unitID, propertyID, unitNumber, unitType, status
    FROM Units
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def update_unit(unitID: int, unit_data: dict):
    """
    Updates a unit record identified by unitID.
    Expects unit_data with keys: propertyID, unitNumber, unitType, status.
    """
    query = """
    UPDATE Units
    SET propertyID = %(propertyID)s,
        unitNumber = %(unitNumber)s,
        unitType = %(unitType)s,
        status = %(status)s
    WHERE unitID = %(unitID)s
    """
    unit_data["unitID"] = unitID
    cursor = connection.cursor()
    cursor.execute(query, unit_data)
    connection.commit()
    cursor.close()


def delete_unit(unitID: int):
    """
    Deletes a unit record by unitID.
    """
    query = "DELETE FROM Units WHERE unitID = %(unitID)s"
    cursor = connection.cursor()
    cursor.execute(query, {"unitID": unitID})
    connection.commit()
    cursor.close()


# Maintenance Request CRUD

def create_maintenance_request(mr_data: dict):
    """
    Inserts a new maintenance request into the MaintenanceRequests table.
    Expects mr_data with keys: description, status, submissionDate, completionDate.
    """
    query = """
    INSERT INTO MaintenanceRequests (description, status, submissionDate, completionDate)
    VALUES (%(description)s, %(status)s, %(submissionDate)s, %(completionDate)s)
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query, mr_data)
    connection.commit()
    requestID = cursor.lastrowid
    cursor.close()
    return requestID


def get_maintenance_request(requestID: int):
    """
    Returns a single maintenance request record by requestID.
    """
    query = """
    SELECT requestID, description, status, submissionDate, completionDate
    FROM MaintenanceRequests
    WHERE requestID = %(requestID)s
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query, {"requestID": requestID})
    result = cursor.fetchone()
    cursor.close()
    return result


def get_maintenance_requests():
    """
    Returns all maintenance request records.
    """
    query = """
    SELECT requestID, description, status, submissionDate, completionDate
    FROM MaintenanceRequests
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def update_maintenance_request(requestID: int, mr_data: dict):
    """
    Updates a maintenance request record identified by requestID.
    Expects mr_data with keys: description, status, submissionDate, completionDate.
    """
    query = """
    UPDATE MaintenanceRequests
    SET description = %(description)s,
        status = %(status)s,
        submissionDate = %(submissionDate)s,
        completionDate = %(completionDate)s
    WHERE requestID = %(requestID)s
    """
    mr_data["requestID"] = requestID
    cursor = connection.cursor()
    cursor.execute(query, mr_data)
    connection.commit()
    cursor.close()


def delete_maintenance_request(requestID: int):
    """
    Deletes a maintenance request record by requestID.
    """
    query = "DELETE FROM MaintenanceRequests WHERE requestID = %(requestID)s"
    cursor = connection.cursor()
    cursor.execute(query, {"requestID": requestID})
    connection.commit()
    cursor.close()


# Leases CRUD

def create_lease(lease_data: dict):
    """
    Inserts a new lease into the Leases table.
    Expects lease_data with keys: unitID, tenantID, startDate, endDate, rentPrice.
    """
    query = """
    INSERT INTO Leases (unitID, tenantID, startDate, endDate, rentPrice)
    VALUES (%(unitID)s, %(tenantID)s, %(startDate)s, %(endDate)s, %(rentPrice)s)
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query, lease_data)
    connection.commit()
    leaseID = cursor.lastrowid
    cursor.close()
    return leaseID


def get_lease(leaseID: int):
    """
    Returns a single lease record by leaseID.
    """
    query = """
    SELECT leaseID, unitID, tenantID, startDate, endDate, rentPrice
    FROM Leases
    WHERE leaseID = %(leaseID)s
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query, {"leaseID": leaseID})
    result = cursor.fetchone()
    cursor.close()
    return result


def get_leases():
    """
    Returns all lease records.
    """
    query = """
    SELECT leaseID, unitID, tenantID, startDate, endDate, rentPrice
    FROM Leases
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def update_lease(leaseID: int, lease_data: dict):
    """
    Updates a lease record identified by leaseID.
    Expects lease_data with keys: unitID, tenantID, startDate, endDate, rentPrice.
    """
    query = """
    UPDATE Leases
    SET unitID = %(unitID)s,
        tenantID = %(tenantID)s,
        startDate = %(startDate)s,
        endDate = %(endDate)s,
        rentPrice = %(rentPrice)s
    WHERE leaseID = %(leaseID)s
    """
    lease_data["leaseID"] = leaseID
    cursor = connection.cursor()
    cursor.execute(query, lease_data)
    connection.commit()
    cursor.close()


def delete_lease(leaseID: int):
    """
    Deletes a lease record by leaseID.
    """
    query = "DELETE FROM Leases WHERE leaseID = %(leaseID)s"
    cursor = connection.cursor()
    cursor.execute(query, {"leaseID": leaseID})
    connection.commit()
    cursor.close()


# Payments CRUD

def create_payment(payment_data: dict):
    """
    Inserts a new payment into the Payments table.
    Expects payment_data with keys: tenantID, leaseID, amount, paymentDate, paymentMethod.
    """
    query = """
    INSERT INTO Payments (tenantID, leaseID, amount, paymentDate, paymentMethod)
    VALUES (%(tenantID)s, %(leaseID)s, %(amount)s, %(paymentDate)s, %(paymentMethod)s)
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query, payment_data)
    connection.commit()
    paymentID = cursor.lastrowid
    cursor.close()
    return paymentID


def get_payment(paymentID: int):
    """
    Returns a single payment record by paymentID.
    """
    query = """
    SELECT paymentID, tenantID, leaseID, amount, paymentDate, paymentMethod
    FROM Payments
    WHERE paymentID = %(paymentID)s
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query, {"paymentID": paymentID})
    result = cursor.fetchone()
    cursor.close()
    return result


def get_payments():
    """
    Returns all payment records.
    """
    query = """
    SELECT paymentID, tenantID, leaseID, amount, paymentDate, paymentMethod
    FROM Payments
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def update_payment(paymentID: int, payment_data: dict):
    """
    Updates a payment record identified by paymentID.
    Expects payment_data with keys: tenantID, leaseID, amount, paymentDate, paymentMethod.
    """
    query = """
    UPDATE Payments
    SET tenantID = %(tenantID)s,
        leaseID = %(leaseID)s,
        amount = %(amount)s,
        paymentDate = %(paymentDate)s,
        paymentMethod = %(paymentMethod)s
    WHERE paymentID = %(paymentID)s
    """
    payment_data["paymentID"] = paymentID
    cursor = connection.cursor()
    cursor.execute(query, payment_data)
    connection.commit()
    cursor.close()


def delete_payment(paymentID: int):
    """
    Deletes a payment record by paymentID.
    """
    query = "DELETE FROM Payments WHERE paymentID = %(paymentID)s"
    cursor = connection.cursor()
    cursor.execute(query, {"paymentID": paymentID})
    connection.commit()
    cursor.close()


# Unit Maintenance Request CRUD

def create_unit_maintenance_request(umr_data: dict):
    """
    Inserts a new association in the UnitMaintenanceRequests table.
    Expects umr_data with keys: unitID, requestID.
    """
    query = """
    INSERT INTO UnitMaintenanceRequests (unitID, requestID)
    VALUES (%(unitID)s, %(requestID)s)
    """
    cursor = connection.cursor()
    cursor.execute(query, umr_data)
    connection.commit()
    cursor.close()


def get_unit_maintenance_request(unitID: int, requestID: int):
    """
    Returns a specific UnitMaintenanceRequests record based on unitID and requestID.
    """
    query = """
    SELECT unitID, requestID
    FROM UnitMaintenanceRequests
    WHERE unitID = %(unitID)s AND requestID = %(requestID)s
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query, {"unitID": unitID, "requestID": requestID})
    result = cursor.fetchone()
    cursor.close()
    return result


def get_unit_maintenance_requests():
    """
    Returns all records from the UnitMaintenanceRequests table.
    """
    query = """
    SELECT unitID, requestID
    FROM UnitMaintenanceRequests
    """
    cursor = connection.cursor(DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def delete_unit_maintenance_request(unitID: int, requestID: int):
    """
    Deletes a record from UnitMaintenanceRequests based on unitID and requestID.
    """
    query = """
    DELETE FROM UnitMaintenanceRequests
    WHERE unitID = %(unitID)s AND requestID = %(requestID)s
    """
    cursor = connection.cursor()
    cursor.execute(query, {"unitID": unitID, "requestID": requestID})
    connection.commit()
    cursor.close()
