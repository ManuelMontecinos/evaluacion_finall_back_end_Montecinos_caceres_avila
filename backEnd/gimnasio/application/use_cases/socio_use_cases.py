from typing import List, Optional

from gimnasio.application.exceptions import (
    EmailDuplicadoError,
    PlanNoEncontradoError,
    RutDuplicadoError,
    SocioConInscripcionesError,
    SocioNoEncontradoError,
)
from gimnasio.domain.entities import Socio
from gimnasio.domain.repositories import PlanRepository, SocioRepository


def _validar_unicos(
    repo: SocioRepository,
    rut: str,
    email: Optional[str],
    excluir_id: Optional[int] = None,
) -> None:
    if repo.existe_rut(rut, excluir_id):
        raise RutDuplicadoError(f"Ya existe un socio con el RUT {rut}")
    if email and repo.existe_email(email, excluir_id):
        raise EmailDuplicadoError(f"Ya existe un socio con el email {email}")


def _validar_plan(planes: PlanRepository, plan_id: int) -> None:
    if planes.obtener_por_id(plan_id) is None:
        raise PlanNoEncontradoError(f"No existe un plan con id {plan_id}")


class ListarSociosUseCase:
    def __init__(self, repo: SocioRepository):
        self.repo = repo

    def ejecutar(self) -> List[Socio]:
        return self.repo.listar()


class ObtenerSocioUseCase:
    def __init__(self, repo: SocioRepository):
        self.repo = repo

    def ejecutar(self, socio_id: int) -> Socio:
        socio = self.repo.obtener_por_id(socio_id)
        if socio is None:
            raise SocioNoEncontradoError(f"No existe un socio con id {socio_id}")
        return socio


class CrearSocioUseCase:
    def __init__(self, repo: SocioRepository, planes: PlanRepository):
        self.repo = repo
        self.planes = planes

    def ejecutar(self, datos: dict) -> Socio:
        _validar_plan(self.planes, datos["plan_id"])
        _validar_unicos(self.repo, datos["rut"], datos.get("email"))

        socio = Socio(
            rut=datos["rut"],
            nombre=datos["nombre"],
            plan_id=datos["plan_id"],
            fecha_vencimiento=datos["fecha_vencimiento"],
            email=datos.get("email"),
            telefono=datos.get("telefono"),
            activo=datos.get("activo", True),
        )
        return self.repo.guardar(socio)


class ActualizarSocioUseCase:
    def __init__(self, repo: SocioRepository, planes: PlanRepository):
        self.repo = repo
        self.planes = planes

    def ejecutar(self, socio_id: int, datos: dict) -> Socio:
        socio = ObtenerSocioUseCase(self.repo).ejecutar(socio_id)

        socio.rut = datos.get("rut", socio.rut)
        socio.nombre = datos.get("nombre", socio.nombre)
        socio.email = datos.get("email", socio.email)
        socio.telefono = datos.get("telefono", socio.telefono)
        socio.plan_id = datos.get("plan_id", socio.plan_id)
        socio.fecha_vencimiento = datos.get("fecha_vencimiento", socio.fecha_vencimiento)
        socio.activo = datos.get("activo", socio.activo)

        _validar_plan(self.planes, socio.plan_id)
        _validar_unicos(self.repo, socio.rut, socio.email, excluir_id=socio_id)
        return self.repo.guardar(socio)


class EliminarSocioUseCase:
    def __init__(self, repo: SocioRepository):
        self.repo = repo

    def ejecutar(self, socio_id: int) -> None:
        ObtenerSocioUseCase(self.repo).ejecutar(socio_id)
        if self.repo.tiene_inscripciones(socio_id):
            raise SocioConInscripcionesError(
                "No se puede eliminar un socio que tiene inscripciones (desactívalo con activo=false)"
            )
        self.repo.eliminar(socio_id)
