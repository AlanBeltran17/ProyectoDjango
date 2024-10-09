from django.contrib import admin
from .models import (
    Laboratorio,
    Mantenimiento,
    Comentario,
    DocumentacionTecnica,
    Equipo,
    Mobiliario,
    EquipoFungible
)

# Registro del modelo Laboratorio
@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id_laboratorio', 'nombre_laboratorio', 'ubicacion', 'id_jefe_lab')
    search_fields = ('nombre_laboratorio', 'ubicacion')

# Registro del modelo Mantenimiento
@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('id_mantenimiento', 'fecha', 'descripcion', 'id_laboratorio')
    list_filter = ('id_laboratorio',)
    search_fields = ('descripcion',)

# Registro del modelo Comentario
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id_comentario', 'fecha', 'estado', 'id_laboratorio')
    list_filter = ('estado', 'id_laboratorio')
    search_fields = ('id_laboratorio__nombre_laboratorio',)

# Registro del modelo DocumentacionTecnica
@admin.register(DocumentacionTecnica)
class DocumentacionTecnicaAdmin(admin.ModelAdmin):
    list_display = ('id_documentacion', 'documentacion')
    search_fields = ('documentacion',)

# Registro del modelo Equipo
@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id_equipo', 'nombre_equipo', 'modelo', 'estado_equipo', 'id_laboratorio')
    list_filter = ('estado_equipo', 'id_laboratorio')
    search_fields = ('nombre_equipo', 'modelo', 'descripcion')

# Registro del modelo Mobiliario
@admin.register(Mobiliario)
class MobiliarioAdmin(admin.ModelAdmin):
    list_display = ('id_mobiliario', 'nombre_mobiliario', 'estado_mobiliario', 'id_laboratorio')
    list_filter = ('estado_mobiliario', 'id_laboratorio')
    search_fields = ('nombre_mobiliario',)

# Registro del modelo EquipoFungible
@admin.register(EquipoFungible)
class EquipoFungibleAdmin(admin.ModelAdmin):
    list_display = ('id_fungible', 'nombre_fungible', 'cantidad', 'id_laboratorio')
    search_fields = ('nombre_fungible',)

# Configura el panel de administración
admin.site.site_header = 'Administración de Laboratorios'
admin.site.site_title = 'Laboratorios'
admin.site.index_title = 'Panel de Control'
