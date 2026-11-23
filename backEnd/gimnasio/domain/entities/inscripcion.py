from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Inscripcion:
    clase_id: int
    socio_id: int
    fecha_inscripcion: Optional[datetime] = None
    asistio: bool = False
