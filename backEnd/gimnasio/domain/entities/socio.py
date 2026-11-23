from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional


@dataclass
class Socio:
    rut: str
    nombre: str
    plan_id: int
    fecha_vencimiento: date
    email: Optional[str] = None
    telefono: Optional[str] = None
    activo: bool = True
    fecha_registro: Optional[datetime] = None
    id: Optional[int] = None
