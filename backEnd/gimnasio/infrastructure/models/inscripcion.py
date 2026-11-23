from django.db import models
from django.db.models.functions import Now

from .clase import ClaseModel
from .socio import SocioModel


class InscripcionModel(models.Model):
    pk = models.CompositePrimaryKey("clase", "socio")
    clase = models.ForeignKey(
        ClaseModel,
        on_delete=models.CASCADE,
        db_column="id_clase",
        related_name="inscripciones",
    )
    socio = models.ForeignKey(
        SocioModel,
        on_delete=models.PROTECT,
        db_column="id_socio",
        related_name="inscripciones",
    )
    fecha_inscripcion = models.DateTimeField(db_default=Now(), editable=False)
    asistio = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = "inscripciones"

    def __str__(self):
        return f"Clase {self.clase_id} - socio {self.socio_id}"
