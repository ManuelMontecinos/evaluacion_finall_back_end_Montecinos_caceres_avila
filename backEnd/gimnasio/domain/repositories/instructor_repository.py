from abc import ABC, abstractmethod
from typing import List, Optional

from gimnasio.domain.entities import Instructor


class InstructorRepository(ABC):

    @abstractmethod
    def listar(self) -> List[Instructor]:
        ...

    @abstractmethod
    def obtener_por_id(self, instructor_id: int) -> Optional[Instructor]:
        ...

    @abstractmethod
    def existe_rut(self, rut: str, excluir_id: Optional[int] = None) -> bool:
        ...

    @abstractmethod
    def existe_email(self, email: str, excluir_id: Optional[int] = None) -> bool:
        ...

    @abstractmethod
    def existe_usuario(self, usuario: str, excluir_id: Optional[int] = None) -> bool:
        ...

    @abstractmethod
    def tiene_clases(self, instructor_id: int) -> bool:
        ...

    @abstractmethod
    def guardar(self, instructor: Instructor) -> Instructor:
        ...

    @abstractmethod
    def eliminar(self, instructor_id: int) -> bool:
        ...
