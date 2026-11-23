from django.db import models
from django.db.models.functions import Now

from .plan import PlanModel


class SocioModel(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_socio")
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    plan = models.ForeignKey(
        PlanModel, on_delete=models.PROTECT, db_column="id_plan", related_name="socios"
    )
    fecha_vencimiento = models.DateField()
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(db_default=Now(), editable=False)

    class Meta:
        managed = False
        db_table = "socios"

    def __str__(self):
        return f"{self.nombre} ({self.rut})"
