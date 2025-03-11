from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db import initialize_db
from fastapi.middleware.cors import CORSMiddleware
import crud

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize the database when the app starts.
@app.on_event("startup")
def startup():
    initialize_db()


# Pydantic schemas for request bodies.
class TenantCreate(BaseModel):
    firstName: str
    lastName: str
    phoneNumber: str
    email: str


class TenantUpdate(BaseModel):
    firstName: str | None = None
    lastName: str | None = None
    phoneNumber: str | None = None
    email: str | None = None


@app.post("/tenants/", response_model=dict)
def add_tenant(tenant: TenantCreate):
    return crud.create_tenant(
        first_name=tenant.firstName,
        last_name=tenant.lastName,
        phone_number=tenant.phoneNumber,
        email=tenant.email
    )


@app.get("/tenants/", response_model=list)
def read_tenants():
    return crud.get_tenants()


@app.put("/tenants/{tenant_id}", response_model=dict)
def update_tenant_route(tenant_id: int, tenant_data: TenantUpdate):
    return crud.update_tenant(
        tenant_id=tenant_id,
        first_name=tenant_data.firstName,
        last_name=tenant_data.lastName,
        phone_number=tenant_data.phoneNumber,
        email=tenant_data.email
    )


@app.delete("/tenants/{tenant_id}", response_model=dict)
def delete_tenant_route(tenant_id: int):
    return crud.delete_tenant(tenant_id)
