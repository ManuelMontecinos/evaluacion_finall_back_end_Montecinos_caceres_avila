from typing import List

from gimnasio.application.exceptions import (
    PlanConSociosError,
    PlanDuplicadoError,
    PlanNoEncontradoError,
)
from gimnasio.domain.entities import Plan
from gimnasio.domain.repositories import PlanRepository


class ListarPlanesUseCase:
    def __init__(self, repo: PlanRepository):
        self.repo = repo

    def ejecutar(self) -> List[Plan]:
        return self.repo.listar()


class ObtenerPlanUseCase:
    def __init__(self, repo: PlanRepository):
        self.repo = repo

    def ejecutar(self, plan_id: int) -> Plan:
        plan = self.repo.obtener_por_id(plan_id)
        if plan is None:
            raise PlanNoEncontradoError(f"No existe un plan con id {plan_id}")
        return plan


class CrearPlanUseCase:
    def __init__(self, repo: PlanRepository):
        self.repo = repo

    def ejecutar(self, datos: dict) -> Plan:
        if self.repo.existe_nombre(datos["nombre"]):
            raise PlanDuplicadoError(f"Ya existe un plan con el nombre {datos['nombre']}")

        plan = Plan(
            nombre=datos["nombre"],
            precio_mensual=datos["precio_mensual"],
            clases_por_semana=datos["clases_por_semana"],
            descripcion=datos.get("descripcion"),
        )
        return self.repo.guardar(plan)


class ActualizarPlanUseCase:
    def __init__(self, repo: PlanRepository):
        self.repo = repo

    def ejecutar(self, plan_id: int, datos: dict) -> Plan:
        plan = ObtenerPlanUseCase(self.repo).ejecutar(plan_id)

        plan.nombre = datos.get("nombre", plan.nombre)
        plan.descripcion = datos.get("descripcion", plan.descripcion)
        plan.precio_mensual = datos.get("precio_mensual", plan.precio_mensual)
        plan.clases_por_semana = datos.get("clases_por_semana", plan.clases_por_semana)

        if self.repo.existe_nombre(plan.nombre, excluir_id=plan_id):
            raise PlanDuplicadoError(f"Ya existe un plan con el nombre {plan.nombre}")
        return self.repo.guardar(plan)


class EliminarPlanUseCase:
    def __init__(self, repo: PlanRepository):
        self.repo = repo

    def ejecutar(self, plan_id: int) -> None:
        ObtenerPlanUseCase(self.repo).ejecutar(plan_id)
        if self.repo.tiene_socios(plan_id):
            raise PlanConSociosError("No se puede eliminar un plan que tiene socios")
        self.repo.eliminar(plan_id)
