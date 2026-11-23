from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class Plan:
    nombre: str
    precio_mensual: Decimal
    clases_por_semana: int
    descripcion: Optional[str] = None
    id: Optional[int] = None

    @property
    def precio_anual(self) -> Decimal:
        return self.precio_mensual * 12
