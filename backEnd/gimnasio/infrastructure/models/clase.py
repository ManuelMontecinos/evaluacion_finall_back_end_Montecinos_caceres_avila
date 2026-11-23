from django.db import models

from .instructor import InstructorModel


class ClaseModel(models.Model):
    ESTADOS = [
        ("programada", "Programada"),
        ("realizada", "Realizada"),
        ("suspendida", "Suspendida"),
    ]

    id = models.AutoField(primary_key=True, db_column="id_clase")
    instructor = models.ForeignKey(
        InstructorModel,
        on_delete=models.PROTECT,
        db_column="id_instructor",
        related_name="clases",
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    fecha_hora = models.DateTimeField()
    cupo_maximo = models.IntegerField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default="programada")

    class Meta:
        managed = False
        db_table = "clases"

    def __str__(self):
        return f"{self.nombre} ({self.estado})"
