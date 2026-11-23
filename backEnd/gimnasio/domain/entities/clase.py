from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Clase:
    instructor_id: int
    nombre: str
    fecha_hora: datetime
    cupo_maximo: int
    estado: str = "programada"
    descripcion: Optional[str] = None
    id: Optional[int] = None
