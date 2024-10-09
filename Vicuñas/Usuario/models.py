from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    id_usuario = models.AutoField(
        primary_key=True,
    )

    ROL_CHOICES = [
        ('1', 'Director de carrera'),
        ('2', 'Jefe de laboratorio'),
    ]

    nombre_usuario = models.CharField(
        max_length=100,
        unique=True,
        help_text='Nombre del usuario'
    )

    contraseña = models.CharField(
        max_length=128,  # El hash de la contraseña puede ser más largo
        help_text='Contraseña del usuario'
    )

    rol = models.CharField(
        max_length=1,
        choices=ROL_CHOICES,
        help_text='Rol del usuario'
    )

    ESTADO_CHOICES = [
        (1, 'Habilitado'),
        (0, 'Deshabilitado'),
    ]

    estado = models.IntegerField(
        choices = ESTADO_CHOICES,
        default = 1,
        help_text = 'Estado del usuario'
    )

    def __str__(self):
        return self.nombre_usuario

    def save(self, *args, **kwargs):
        # Al guardar el usuario, hashear la contraseña
        self.contraseña = make_password(self.contraseña)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'Usuario'
