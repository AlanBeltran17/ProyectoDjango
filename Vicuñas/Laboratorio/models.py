from django.db import models
from Docente.models import Docente, JefeLaboratorio

class Laboratorio(models.Model):
    id_laboratorio = models.AutoField(primary_key=True)

    nombre_laboratorio = models.CharField(
        max_length=15,
        help_text = 'Nombre del Laboratorio'
    )

    ubicacion = models.CharField(
        max_length=100,
        help_text = 'Ubicación del laboratorio'
    )

    id_jefe_lab = models.ForeignKey(
        JefeLaboratorio,
        on_delete=models.CASCADE,
        related_name='jefe_lab'
    )

    def __str__(self):
        return self.nombre_laboratorio

    class Meta:
        verbose_name = 'Laboratorio'
        verbose_name_plural = 'Laboratorios'
        db_table = 'Laboratorio'


class Mantenimiento(models.Model):
    id_mantenimiento = models.AutoField(primary_key=True)

    fecha = models.DateTimeField(
        help_text='Fecha de mantenimiento'
    )

    descripcion = models.TextField(
        help_text='Descripción del mantenimiento realizado'
    )

    id_laboratorio = models.ForeignKey(
        Laboratorio,
        on_delete=models.CASCADE,
        related_name='mantenimientos'
    )

    def __str__(self):
        return f"Mantenimiento en {self.id_laboratorio.nombre_laboratorio} - {self.fecha}"

    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'
        db_table = 'Mantenimiento'


class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)

    fecha = models.DateField(
        help_text='Fecha del comentario'
    )

    # Cambia el IntegerField a CharField con opciones limitadas
    ESTADO_CHOICES = [
        ('solucionado', 'Solucionado'),
        ('no_solucionado', 'No Solucionado'),
    ]

    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='no_solucionado',
        help_text='Estado del comentario'
    )

    id_laboratorio = models.ForeignKey(
        Laboratorio,
        on_delete=models.CASCADE,
        related_name='comentarios'
    )

    def __str__(self):
        return f"Comentario {self.id_comentario} - {self.fecha} - {self.estado_icono()}"

    def estado_icono(self):
        # Método para retornar un símbolo según el estado
        return "✅" if self.estado == 'solucionado' else "❌"

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        db_table = 'Comentario'


class DocumentacionTecnica(models.Model):
    id_documentacion = models.AutoField(primary_key=True)

    documentacion = models.FileField(
        upload_to='documentacion_tecnica/',  # Esto hará que se guarde en media/documentacion_tecnica/
        help_text='Documentación técnica en formato PDF'
    )


    def __str__(self):
        return f"Documentación {self.id_documentacion}"

    class Meta:
        verbose_name = 'Documentación Técnica'
        verbose_name_plural = 'Documentaciones Técnicas'
        db_table = 'Documentacion_Tecnica'


class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)

    nombre_equipo = models.CharField(
        max_length=150,
        help_text='Nombre del equipo'
    )

    modelo = models.CharField(
        max_length=50,
        help_text='Modelo del equipo'
    )

    descripcion = models.TextField(
        help_text='Descripción del equipo'
    )

    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        help_text='Fecha de registro del equipo'
    )

    tiempo_de_vida = models.DateTimeField(
        help_text='Tiempo de vida útil del equipo'
    )

    ESTADO_CHOICES = [
        (1, 'En uso'),
        (2, 'Dañado'),
        (3, 'Mantenimiento'),
        (4, 'Obsoleto'),
    ]

    estado_equipo = models.IntegerField(
        choices=ESTADO_CHOICES,
        default=1,  # Opcional: establece 'En uso' como valor predeterminado
        help_text='Estado del equipo'
    )

    id_laboratorio = models.ForeignKey(
        Laboratorio,
        on_delete=models.CASCADE,
        related_name='equipos'
    )

    id_documentacion = models.ForeignKey(
        DocumentacionTecnica,
        on_delete=models.CASCADE,
        related_name='equipos_documentacion'
    )

    def __str__(self):
        return self.nombre_equipo

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        db_table = 'Equipo'


class Mobiliario(models.Model):
    id_mobiliario = models.AutoField(primary_key=True)

    nombre_mobiliario = models.CharField(
        max_length=120,
        help_text='Nombre del mobiliario'
    )

    descripcion = models.TextField(
        help_text='Descripción del mobiliario'
    )

    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        help_text='Fecha de registro del mobiliario'
    )

    ESTADO_CHOICES = [
        (1, 'En uso'),
        (2, 'Obsoleto'),
    ]

    estado_mobiliario = models.IntegerField(
        choices=ESTADO_CHOICES,
        default=1,  # Opcional: establece 'En uso' como valor predeterminado
        help_text='Estado del mobiliario'
    )

    id_laboratorio = models.ForeignKey(
        Laboratorio,
        on_delete=models.CASCADE,
        related_name='mobiliarios'
    )

    def __str__(self):
        return self.nombre_mobiliario

    class Meta:
        verbose_name = 'Mobiliario'
        verbose_name_plural = 'Mobiliarios'
        db_table = 'Mobiliario'


class EquipoFungible(models.Model):
    id_fungible = models.AutoField(primary_key=True)

    nombre_fungible = models.CharField(
        max_length=120,
        help_text='Nombre del equipo fungible'
    )

    descripcion = models.TextField(
        help_text='Descripción del equipo fungible'
    )

    cantidad = models.IntegerField(
        help_text='Cantidad disponible'
    )

    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        help_text='Fecha de registro del equipo fungible'
    )

    id_laboratorio = models.ForeignKey(
        Laboratorio,
        on_delete=models.CASCADE,
        related_name='equipos_fungibles'
    )

    def __str__(self):
        return self.nombre_fungible

    class Meta:
        verbose_name = 'Equipo Fungible'
        verbose_name_plural = 'Equipos Fungibles'
        db_table = 'Equipo_fungible'

