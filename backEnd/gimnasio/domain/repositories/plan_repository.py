from abc import ABC, abstractmethod
from typing import List, Optional

from gimnasio.domain.entities import Plan


class PlanRepository(ABC):

    @abstractmethod
    def listar(self) -> List[Plan]:
        ...

    @abstractmethod
    def obtener_por_id(self, plan_id: int) -> Optional[Plan]:
        ...

    @abstractmethod
    def existe_nombre(self, nombre: str, excluir_id: Optional[int] = None) -> bool:
        ...

    @abstractmethod
    def tiene_socios(self, plan_id: int) -> bool:
        ...

    @abstractmethod
    def guardar(self, plan: Plan) -> Plan:
        ...

    @abstractmethod
    def eliminar(self, plan_id: int) -> bool:
        ...
