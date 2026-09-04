from datetime import date
from enum import Enum

from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from typing_extensions import Self


class Usuario(BaseModel):
    nombre: str = Field(min_length=2, max_length=80)
    email: EmailStr
    edad: int = Field(ge=18, le=120)


class Producto(BaseModel):
    nombre: str = Field(min_length=2, max_length=80)
    precio: float
    descuento_pct: float = Field(ge=0, le=100, default=0)

    @field_validator("precio")
    @classmethod
    def validar_precio(cls, precio: float) -> float:
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        return round(precio, 2)


class Orden(BaseModel):
    id_orden: str = Field(min_length=5, max_length=50)
    productos: list[Producto] = Field(min_length=1)

    @property
    def total(self) -> float:
        precio_total = 0.0
        for p in self.productos:
            precio_total += p.precio * (1 - p.descuento_pct / 100)
        return round(precio_total, 2)


class EstadoTicket(str, Enum):
    ABIERTO = "abierto"
    EN_PROGRESO = "en_progreso"
    CERRADO = "cerrado"


class Ticket(BaseModel):
    titulo: str = Field(min_length=2, max_length=80)
    estado: EstadoTicket = EstadoTicket.ABIERTO


class Reserva(BaseModel):
    fecha_inicio: date
    fecha_fin: date
    huespedes: int = Field(ge=1, le=10)

    @model_validator(mode="after")
    def validar_fecha(self) -> Self:
        if self.fecha_inicio >= self.fecha_fin:
            raise ValueError("La fecha fin debe ser más reciente que la fecha inicio")
        return self
