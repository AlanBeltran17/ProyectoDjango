from django.contrib import admin
from .models import Usuario
from .forms import UsuarioForm

class AdminUsuario(admin.ModelAdmin):
    form = UsuarioForm
    list_display = [
        'nombre_usuario',
        'rol'  # Es recomendable no mostrar la contraseña en el panel de administración.
    ]

    search_fields = ('nombre_usuario',)

    class Meta:
        model = Usuario  # Esto indica que esta configuración se aplica al modelo Usuario

# Registrar tu modelo con la configuración personalizada
admin.site.register(Usuario, AdminUsuario)
