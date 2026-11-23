from typing import List, Optional

from gimnasio.domain.entities import Plan
from gimnasio.domain.repositories import PlanRepository
from gimnasio.infrastructure.models import PlanModel, SocioModel


def _to_entity(m: PlanModel) -> Plan:
    return Plan(
        id=m.id,
        nombre=m.nombre,
        descripcion=m.descripcion,
        precio_mensual=m.precio_mensual,
        clases_por_semana=m.clases_por_semana,
    )


class DjangoPlanRepository(PlanRepository):

    def listar(self) -> List[Plan]:
        return [_to_entity(m) for m in PlanModel.objects.order_by("nombre")]

    def obtener_por_id(self, plan_id: int) -> Optional[Plan]:
        m = PlanModel.objects.filter(id=plan_id).first()
        return _to_entity(m) if m else None

    def existe_nombre(self, nombre: str, excluir_id: Optional[int] = None) -> bool:
        return PlanModel.objects.filter(nombre=nombre).exclude(id=excluir_id).exists()

    def tiene_socios(self, plan_id: int) -> bool:
        return SocioModel.objects.filter(plan_id=plan_id).exists()

    def guardar(self, plan: Plan) -> Plan:
        if plan.id is None:
            m = PlanModel.objects.create(
                nombre=plan.nombre,
                descripcion=plan.descripcion,
                precio_mensual=plan.precio_mensual,
                clases_por_semana=plan.clases_por_semana,
            )
        else:
            m = PlanModel.objects.get(id=plan.id)
            m.nombre = plan.nombre
            m.descripcion = plan.descripcion
            m.precio_mensual = plan.precio_mensual
            m.clases_por_semana = plan.clases_por_semana
            m.save(update_fields=["nombre", "descripcion", "precio_mensual", "clases_por_semana"])
        return _to_entity(m)

    def eliminar(self, plan_id: int) -> bool:
        borrados, _ = PlanModel.objects.filter(id=plan_id).delete()
        return borrados > 0
