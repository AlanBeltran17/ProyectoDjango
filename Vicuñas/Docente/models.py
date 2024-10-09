from django.db import models
from Usuario.models import Usuario

class Docente(models.Model):
    id_docente = models.AutoField(
        primary_key=True
    )

    nombre = models.CharField(
        max_length = 75,
        help_text = 'Nombres'
    )

    apellido = models.CharField(
        max_length = 75,
        help_text = 'Apellidos',
        default = ''
    )

    carnet_identidad = models.BigIntegerField(
        unique = True,
        help_text = 'Número de carnet de identidad'
    )

    correo = models.EmailField(
        max_length = 254,
        unique = True,
        help_text = 'Correo electrónico'
    )

    id_usuario = models.ForeignKey(
        Usuario,
        on_delete = models.CASCADE,
        related_name = 'docentes',
        null = True  # Permite valores nulos
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        db_table = 'Docentes'


class JefeLaboratorio(models.Model):
    id_jefe_lab = models.AutoField(primary_key=True)

    # Relación con el docente (solo los docentes existentes pueden ser jefes de laboratorio)
    id_docente = models.ForeignKey(
        Docente,
        on_delete=models.CASCADE,
        related_name='jefaturas'
    )

    def __str__(self):
        return f"Jefe de Laboratorio: {self.id_docente.nombre} {self.id_docente.apellido}"

    class Meta:
        verbose_name = 'Jefe de Laboratorio'
        verbose_name_plural = 'Jefes de Laboratorio'
        db_table = 'Jefe_laboratorio'


class DirCarrera(models.Model):
    id_director = models.AutoField(primary_key=True)

    fecha_inicio = models.DateField(
        help_text='Fecha de inicio'
    )

    fecha_fin = models.DateField(
        help_text='Fecha de fin'
    )

    id_docente = models.ForeignKey(
        Docente,
        on_delete=models.CASCADE,
        related_name='direcciones_carrera'
    )

    def __str__(self):
        return f"Director: {self.id_docente.nombre} {self.id_docente.apellido}"

    class Meta:
        verbose_name = 'Director de Carrera'
        verbose_name_plural = 'Directores de Carrera'
        db_table = 'Dir_carrera'