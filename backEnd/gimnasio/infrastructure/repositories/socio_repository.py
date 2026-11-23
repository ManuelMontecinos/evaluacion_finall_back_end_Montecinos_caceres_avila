from typing import List, Optional

from gimnasio.domain.entities import Socio
from gimnasio.domain.repositories import SocioRepository
from gimnasio.infrastructure.models import InscripcionModel, SocioModel

CAMPOS = ["rut", "nombre", "email", "telefono", "plan_id", "fecha_vencimiento", "activo"]


def _to_entity(m: SocioModel) -> Socio:
    return Socio(
        id=m.id,
        rut=m.rut,
        nombre=m.nombre,
        email=m.email,
        telefono=m.telefono,
        plan_id=m.plan_id,
        fecha_vencimiento=m.fecha_vencimiento,
        activo=m.activo,
        fecha_registro=m.fecha_registro,
    )


class DjangoSocioRepository(SocioRepository):

    def listar(self) -> List[Socio]:
        return [_to_entity(m) for m in SocioModel.objects.order_by("nombre")]

    def obtener_por_id(self, socio_id: int) -> Optional[Socio]:
        m = SocioModel.objects.filter(id=socio_id).first()
        return _to_entity(m) if m else None

    def existe_rut(self, rut: str, excluir_id: Optional[int] = None) -> bool:
        return SocioModel.objects.filter(rut=rut).exclude(id=excluir_id).exists()

    def existe_email(self, email: str, excluir_id: Optional[int] = None) -> bool:
        return SocioModel.objects.filter(email=email).exclude(id=excluir_id).exists()

    def tiene_inscripciones(self, socio_id: int) -> bool:
        return InscripcionModel.objects.filter(socio_id=socio_id).exists()

    def guardar(self, socio: Socio) -> Socio:
        valores = {campo: getattr(socio, campo) for campo in CAMPOS}
        if socio.id is None:
            m = SocioModel.objects.create(**valores)
            m.refresh_from_db()
        else:
            m = SocioModel.objects.get(id=socio.id)
            for campo, valor in valores.items():
                setattr(m, campo, valor)
            m.save(update_fields=CAMPOS)
        return _to_entity(m)

    def eliminar(self, socio_id: int) -> bool:
        borrados, _ = SocioModel.objects.filter(id=socio_id).delete()
        return borrados > 0
