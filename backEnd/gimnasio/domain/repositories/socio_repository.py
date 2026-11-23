from abc import ABC, abstractmethod
from typing import List, Optional

from gimnasio.domain.entities import Socio


class SocioRepository(ABC):

    @abstractmethod
    def listar(self) -> List[Socio]:
        ...

    @abstractmethod
    def obtener_por_id(self, socio_id: int) -> Optional[Socio]:
        ...

    @abstractmethod
    def existe_rut(self, rut: str, excluir_id: Optional[int] = None) -> bool:
        ...

    @abstractmethod
    def existe_email(self, email: str, excluir_id: Optional[int] = None) -> bool:
        ...

    @abstractmethod
    def tiene_inscripciones(self, socio_id: int) -> bool:
        ...

    @abstractmethod
    def guardar(self, socio: Socio) -> Socio:
        ...

    @abstractmethod
    def eliminar(self, socio_id: int) -> bool:
        ...
