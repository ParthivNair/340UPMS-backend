from datetime import date
from pydantic import BaseModel
from typing import Optional


class Tenant(BaseModel):
    firstName: str
    lastName: str
    phoneNumber: str
    email: str


class TenantOut(Tenant):
    tenantID: int


class Property(BaseModel):
    address: str
    city: str
    state: str
    zipCode: str
    propertyValue: float


class PropertyOut(Property):
    propertyID: int


class Unit(BaseModel):
    propertyID: int
    unitNumber: str
    unitType: str
    status: Optional[str] = "Vacant"


class UnitOut(Unit):
    unitID: int


class MaintenanceRequest(BaseModel):
    description: str
    status: str
    submissionDate: date
    completionDate: Optional[date] = None


class MaintenanceRequestOut(MaintenanceRequest):
    requestID: int


# Leases
class Lease(BaseModel):
    unitID: int
    tenantID: int
    startDate: date
    endDate: Optional[date] = None
    rentPrice: float


class LeaseOut(Lease):
    leaseID: int


class Payment(BaseModel):
    tenantID: int
    leaseID: int
    amount: float
    paymentDate: date
    paymentMethod: str


class PaymentOut(Payment):
    paymentID: int


class UnitMaintenanceRequest(BaseModel):
    unitID: int
    requestID: int
