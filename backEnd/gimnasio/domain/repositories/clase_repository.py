from abc import ABC, abstractmethod
from typing import List, Optional

from gimnasio.domain.entities import Clase


class ClaseRepository(ABC):

    @abstractmethod
    def listar(self) -> List[Clase]:
        ...

    @abstractmethod
    def obtener_por_id(self, clase_id: int) -> Optional[Clase]:
        ...

    @abstractmethod
    def guardar(self, clase: Clase) -> Clase:
        ...

    @abstractmethod
    def eliminar(self, clase_id: int) -> bool:
        ...
