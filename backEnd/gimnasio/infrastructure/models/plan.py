from django.db import models


class PlanModel(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_plan")
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    clases_por_semana = models.IntegerField()
    precio_anual = models.GeneratedField(
        expression=models.F("precio_mensual") * 12,
        output_field=models.DecimalField(max_digits=12, decimal_places=2),
        db_persist=False,
    )

    class Meta:
        managed = False
        db_table = "planes"

    def __str__(self):
        return self.nombre
