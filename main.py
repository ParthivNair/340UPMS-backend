from fastapi import FastAPI, HTTPException
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import crud
from models import Tenant, TenantOut, Property, PropertyOut, Unit, UnitOut, MaintenanceRequest, MaintenanceRequestOut, \
    Lease, LeaseOut, Payment, PaymentOut, UnitMaintenanceRequest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/tenants", response_model=TenantOut)
def create_tenant(tenant: Tenant):
    try:
        tenantID = crud.create_tenant(tenant.dict())
        return {**tenant.dict(), "tenantID": tenantID}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/tenants/{tenantID}", response_model=TenantOut)
def read_tenant(tenantID: int):
    tenant = crud.get_tenant(tenantID)
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return tenant


@app.get("/tenants", response_model=List[TenantOut])
def read_tenants():
    return crud.get_tenants()


@app.put("/tenants/{tenantID}", response_model=TenantOut)
def update_tenant(tenantID: int, tenant: Tenant):
    try:
        crud.update_tenant(tenantID, tenant.dict())
        updated = crud.get_tenant(tenantID)
        if not updated:
            raise HTTPException(status_code=404, detail="Tenant not found")
        return updated
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/tenants/{tenantID}")
def delete_tenant(tenantID: int):
    try:
        crud.delete_tenant(tenantID)
        return {"detail": "Tenant deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ------------------------------
# PROPERTIES ENDPOINTS
# ------------------------------

@app.post("/properties", response_model=PropertyOut)
def create_property(property: Property):
    try:
        propertyID = crud.create_property(property.dict())
        return {**property.dict(), "propertyID": propertyID}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/properties/{propertyID}", response_model=PropertyOut)
def read_property(propertyID: int):
    property_obj = crud.get_property(propertyID)
    if not property_obj:
        raise HTTPException(status_code=404, detail="Property not found")
    return property_obj


@app.get("/properties", response_model=List[PropertyOut])
def read_properties():
    return crud.get_properties()


@app.put("/properties/{propertyID}", response_model=PropertyOut)
def update_property(propertyID: int, property: Property):
    try:
        crud.update_property(propertyID, property.dict())
        updated = crud.get_property(propertyID)
        if not updated:
            raise HTTPException(status_code=404, detail="Property not found")
        return updated
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/properties/{propertyID}")
def delete_property(propertyID: int):
    try:
        crud.delete_property(propertyID)
        return {"detail": "Property deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/units", response_model=UnitOut)
def create_unit(unit: Unit):
    try:
        unitID = crud.create_unit(unit.dict())
        return {**unit.dict(), "unitID": unitID}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/units/{unitID}", response_model=UnitOut)
def read_unit(unitID: int):
    unit_obj = crud.get_unit(unitID)
    if not unit_obj:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit_obj


@app.get("/units", response_model=List[UnitOut])
def read_units():
    return crud.get_units()


@app.put("/units/{unitID}", response_model=UnitOut)
def update_unit(unitID: int, unit: Unit):
    try:
        crud.update_unit(unitID, unit.dict())
        updated = crud.get_unit(unitID)
        if not updated:
            raise HTTPException(status_code=404, detail="Unit not found")
        return updated
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/units/{unitID}")
def delete_unit(unitID: int):
    try:
        crud.delete_unit(unitID)
        return {"detail": "Unit deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/maintenance_requests", response_model=MaintenanceRequestOut)
def create_maintenance_request(mr: MaintenanceRequest):
    try:
        requestID = crud.create_maintenance_request(mr.dict())
        return {**mr.dict(), "requestID": requestID}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/maintenance_requests/{requestID}", response_model=MaintenanceRequestOut)
def read_maintenance_request(requestID: int):
    mr_obj = crud.get_maintenance_request(requestID)
    if not mr_obj:
        raise HTTPException(status_code=404, detail="Maintenance request not found")
    return mr_obj


@app.get("/maintenance_requests", response_model=List[MaintenanceRequestOut])
def read_maintenance_requests():
    return crud.get_maintenance_requests()


@app.put("/maintenance_requests/{requestID}", response_model=MaintenanceRequestOut)
def update_maintenance_request(requestID: int, mr: MaintenanceRequest):
    try:
        crud.update_maintenance_request(requestID, mr.dict())
        updated = crud.get_maintenance_request(requestID)
        if not updated:
            raise HTTPException(status_code=404, detail="Maintenance request not found")
        return updated
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/maintenance_requests/{requestID}")
def delete_maintenance_request(requestID: int):
    try:
        crud.delete_maintenance_request(requestID)
        return {"detail": "Maintenance request deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/leases", response_model=LeaseOut)
def create_lease(lease: Lease):
    try:
        leaseID = crud.create_lease(lease.dict())
        return {**lease.dict(), "leaseID": leaseID}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/leases/{leaseID}", response_model=LeaseOut)
def read_lease(leaseID: int):
    lease_obj = crud.get_lease(leaseID)
    if not lease_obj:
        raise HTTPException(status_code=404, detail="Lease not found")
    return lease_obj


@app.get("/leases", response_model=List[LeaseOut])
def read_leases():
    return crud.get_leases()


@app.put("/leases/{leaseID}", response_model=LeaseOut)
def update_lease(leaseID: int, lease: Lease):
    try:
        crud.update_lease(leaseID, lease.dict())
        updated = crud.get_lease(leaseID)
        if not updated:
            raise HTTPException(status_code=404, detail="Lease not found")
        return updated
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/leases/{leaseID}")
def delete_lease(leaseID: int):
    try:
        crud.delete_lease(leaseID)
        return {"detail": "Lease deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/payments", response_model=PaymentOut)
def create_payment(payment: Payment):
    try:
        paymentID = crud.create_payment(payment.dict())
        return {**payment.dict(), "paymentID": paymentID}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/payments/{paymentID}", response_model=PaymentOut)
def read_payment(paymentID: int):
    payment_obj = crud.get_payment(paymentID)
    if not payment_obj:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment_obj


@app.get("/payments", response_model=List[PaymentOut])
def read_payments():
    return crud.get_payments()


@app.put("/payments/{paymentID}", response_model=PaymentOut)
def update_payment(paymentID: int, payment: Payment):
    try:
        crud.update_payment(paymentID, payment.dict())
        updated = crud.get_payment(paymentID)
        if not updated:
            raise HTTPException(status_code=404, detail="Payment not found")
        return updated
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/payments/{paymentID}")
def delete_payment(paymentID: int):
    try:
        crud.delete_payment(paymentID)
        return {"detail": "Payment deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/unit_maintenance_requests")
def create_unit_maintenance_request(umr: UnitMaintenanceRequest):
    try:
        crud.create_unit_maintenance_request(umr.dict())
        return {"detail": "Association created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/unit_maintenance_requests", response_model=List[UnitMaintenanceRequest])
def read_unit_maintenance_requests():
    return crud.get_unit_maintenance_requests()


@app.delete("/unit_maintenance_requests")
def delete_unit_maintenance_request(unitID: int, requestID: int):
    try:
        crud.delete_unit_maintenance_request(unitID, requestID)
        return {"detail": "Association deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
