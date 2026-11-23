from abc import ABC, abstractmethod
from typing import List, Optional

from gimnasio.domain.entities import Inscripcion


class InscripcionRepository(ABC):

    @abstractmethod
    def listar(self) -> List[Inscripcion]:
        ...

    @abstractmethod
    def obtener(self, clase_id: int, socio_id: int) -> Optional[Inscripcion]:
        ...

    @abstractmethod
    def guardar(self, inscripcion: Inscripcion) -> Inscripcion:
        ...

    @abstractmethod
    def eliminar(self, clase_id: int, socio_id: int) -> bool:
        ...
