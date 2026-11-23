from django.db import models


class InstructorModel(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_instructor")
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=80)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    usuario = models.CharField(max_length=150, unique=True, null=True, blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = "instructores"

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"
