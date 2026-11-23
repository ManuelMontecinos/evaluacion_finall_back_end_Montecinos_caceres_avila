from typing import List, Optional

from gimnasio.domain.entities import Instructor
from gimnasio.domain.repositories import InstructorRepository
from gimnasio.infrastructure.models import ClaseModel, InstructorModel

CAMPOS = ["rut", "nombre", "especialidad", "email", "telefono", "usuario", "activo"]


def _to_entity(m: InstructorModel) -> Instructor:
    return Instructor(
        id=m.id,
        rut=m.rut,
        nombre=m.nombre,
        especialidad=m.especialidad,
        email=m.email,
        telefono=m.telefono,
        usuario=m.usuario,
        activo=m.activo,
    )


class DjangoInstructorRepository(InstructorRepository):

    def listar(self) -> List[Instructor]:
        return [_to_entity(m) for m in InstructorModel.objects.order_by("nombre")]

    def obtener_por_id(self, instructor_id: int) -> Optional[Instructor]:
        m = InstructorModel.objects.filter(id=instructor_id).first()
        return _to_entity(m) if m else None

    def existe_rut(self, rut: str, excluir_id: Optional[int] = None) -> bool:
        return InstructorModel.objects.filter(rut=rut).exclude(id=excluir_id).exists()

    def existe_email(self, email: str, excluir_id: Optional[int] = None) -> bool:
        return InstructorModel.objects.filter(email=email).exclude(id=excluir_id).exists()

    def existe_usuario(self, usuario: str, excluir_id: Optional[int] = None) -> bool:
        return InstructorModel.objects.filter(usuario=usuario).exclude(id=excluir_id).exists()

    def tiene_clases(self, instructor_id: int) -> bool:
        return ClaseModel.objects.filter(instructor_id=instructor_id).exists()

    def guardar(self, instructor: Instructor) -> Instructor:
        valores = {campo: getattr(instructor, campo) for campo in CAMPOS}
        if instructor.id is None:
            m = InstructorModel.objects.create(**valores)
        else:
            m = InstructorModel.objects.get(id=instructor.id)
            for campo, valor in valores.items():
                setattr(m, campo, valor)
            m.save(update_fields=CAMPOS)
        return _to_entity(m)

    def eliminar(self, instructor_id: int) -> bool:
        borrados, _ = InstructorModel.objects.filter(id=instructor_id).delete()
        return borrados > 0
