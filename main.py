from fastapi import FastAPI
from fastapi.openapi.utils import status_code_ranges

app = FastAPI()
phones_db=[]



@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/health")
def health():
    return "OK"

from typing import List
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Phones API - Mémoire")

class Characteristic(BaseModel):
    ram_memory: int
    rom_memory: int

class Phone(BaseModel):
    id: str
    brand: str
    model: str
    characteristics: Characteristic


phones_db: List[Phone] = []

@app.post("/phones", status_code=status.HTTP_201_CREATED, response_model=Phone)
def create_phone(phone: Phone):

    if any(p.id == phone.id for p in phones_db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Phone with id '{phone.id}' already exists."
        )
    phones_db.append(phone)
    return phone







