from typing import List, Optional

from gimnasio.application.exceptions import (
    EmailDuplicadoError,
    InstructorConClasesError,
    InstructorNoEncontradoError,
    RutDuplicadoError,
    UsuarioDuplicadoError,
)
from gimnasio.domain.entities import Instructor
from gimnasio.domain.repositories import InstructorRepository


def _validar_unicos(
    repo: InstructorRepository,
    rut: str,
    email: Optional[str],
    usuario: Optional[str],
    excluir_id: Optional[int] = None,
) -> None:
    if repo.existe_rut(rut, excluir_id):
        raise RutDuplicadoError(f"Ya existe un instructor con el RUT {rut}")
    if email and repo.existe_email(email, excluir_id):
        raise EmailDuplicadoError(f"Ya existe un instructor con el email {email}")
    if usuario and repo.existe_usuario(usuario, excluir_id):
        raise UsuarioDuplicadoError(f"Ya existe un instructor con el usuario {usuario}")


class ListarInstructoresUseCase:
    def __init__(self, repo: InstructorRepository):
        self.repo = repo

    def ejecutar(self) -> List[Instructor]:
        return self.repo.listar()


class ObtenerInstructorUseCase:
    def __init__(self, repo: InstructorRepository):
        self.repo = repo

    def ejecutar(self, instructor_id: int) -> Instructor:
        instructor = self.repo.obtener_por_id(instructor_id)
        if instructor is None:
            raise InstructorNoEncontradoError(f"No existe un instructor con id {instructor_id}")
        return instructor


class CrearInstructorUseCase:
    def __init__(self, repo: InstructorRepository):
        self.repo = repo

    def ejecutar(self, datos: dict) -> Instructor:
        _validar_unicos(self.repo, datos["rut"], datos.get("email"), datos.get("usuario"))

        instructor = Instructor(
            rut=datos["rut"],
            nombre=datos["nombre"],
            especialidad=datos["especialidad"],
            email=datos.get("email"),
            telefono=datos.get("telefono"),
            usuario=datos.get("usuario"),
            activo=datos.get("activo", True),
        )
        return self.repo.guardar(instructor)


class ActualizarInstructorUseCase:
    def __init__(self, repo: InstructorRepository):
        self.repo = repo

    def ejecutar(self, instructor_id: int, datos: dict) -> Instructor:
        instructor = ObtenerInstructorUseCase(self.repo).ejecutar(instructor_id)

        instructor.rut = datos.get("rut", instructor.rut)
        instructor.nombre = datos.get("nombre", instructor.nombre)
        instructor.especialidad = datos.get("especialidad", instructor.especialidad)
        instructor.email = datos.get("email", instructor.email)
        instructor.telefono = datos.get("telefono", instructor.telefono)
        instructor.usuario = datos.get("usuario", instructor.usuario)
        instructor.activo = datos.get("activo", instructor.activo)

        _validar_unicos(
            self.repo, instructor.rut, instructor.email, instructor.usuario, excluir_id=instructor_id
        )
        return self.repo.guardar(instructor)


class EliminarInstructorUseCase:
    def __init__(self, repo: InstructorRepository):
        self.repo = repo

    def ejecutar(self, instructor_id: int) -> None:
        ObtenerInstructorUseCase(self.repo).ejecutar(instructor_id)
        if self.repo.tiene_clases(instructor_id):
            raise InstructorConClasesError(
                "No se puede eliminar un instructor que tiene clases (desactívalo con activo=false)"
            )
        self.repo.eliminar(instructor_id)
