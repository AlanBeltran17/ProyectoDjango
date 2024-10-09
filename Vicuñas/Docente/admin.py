from django.contrib import admin
from .models import Docente, JefeLaboratorio, DirCarrera

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'carnet_identidad', 'correo', 'nombre_usuario')  # Incluye nombre de usuario
    search_fields = ('nombre', 'apellido')  # Permite buscar por nombre completo

    # Función para mostrar el nombre de usuario del docente
    def nombre_usuario(self, obj):
        return obj.id_usuario.nombre_usuario  # Asume que el campo en el modelo Usuario es 'nombre_usuario'

    # Cambia el encabezado de la columna en el admin
    nombre_usuario.short_description = 'Nombre de Usuario'

class JefeLaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id_jefe_lab', 'id_docente')  # Puedes agregar más campos según sea necesario
    search_fields = ('id_docente__nombre', 'id_docente__apellido')  # Permite buscar por nombre y apellido del docente

class DirCarreraAdmin(admin.ModelAdmin):
    list_display = ('id_docente', 'fecha_inicio', 'fecha_fin')  # Muestra los campos deseados
    search_fields = ('id_docente__nombre', 'id_docente__apellido')  # Permite buscar por nombre y apellido del director


# Registra los modelos con las clases de administración
admin.site.register(Docente, DocenteAdmin)
admin.site.register(JefeLaboratorio, JefeLaboratorioAdmin)
admin.site.register(DirCarrera, DirCarreraAdmin)