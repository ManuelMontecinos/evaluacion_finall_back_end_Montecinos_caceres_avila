from dataclasses import dataclass
from typing import Optional


@dataclass
class Instructor:
    rut: str
    nombre: str
    especialidad: str
    email: Optional[str] = None
    telefono: Optional[str] = None
    usuario: Optional[str] = None
    activo: bool = True
    id: Optional[int] = None
