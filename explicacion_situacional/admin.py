from django.contrib.gis import admin as adminGeo
from django.contrib import admin
from explicacion_situacional.modelsEncuestas.modelsConsultas import *
from explicacion_situacional.modelsEncuestas.modelsParticipacion import *
from explicacion_situacional.modelsExplicacion.modelsExplicacionesSituacional import *

class RespuestaSinoAdmin(admin.ModelAdmin):
    """!
	Clase que agrega modelo RespuestaSino en el panel administrativo

	@author Lully Troconis (ltroconis at cenditel.gob.ve)
	@copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
	@date 10-07-2018
	"""
	## Mostrar los campos
    list_display = ('user','pregunta', 'respuesta',)
	## Filtrar por campos
    list_filter = ('user',)

	## Mostrar 25 registros por página
    list_per_page = 25

    ## Ordenar por usuario
    ordering = ('user',)

	## Buscar por campos
	#search_fields = ('pregunta','user',)

class CaracterizacionAdmin(admin.ModelAdmin):
    """!
	Clase que agrega modelo Caracterizacion en el panel administrativo

	@author Lully Troconis (ltroconis at cenditel.gob.ve)
	@copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
	@date 10-07-2018
	"""
    ## Mostrar los campos
    list_display = ('caracterizacion', 'descripcion',)
	## Filtrar por campos
    list_filter = ('caracterizacion',)

	## Mostrar 25 registros por página
    list_per_page = 25

    ## Ordenar por usuario
    ordering = ('caracterizacion',)

class ConsultaAdmin(admin.ModelAdmin):
    """!
	Clase que agrega modelo Consulta en el panel administrativo

	@author Lully Troconis (ltroconis at cenditel.gob.ve)
	@copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
	@date 10-07-2018
	"""
	## Mostrar los campos
    list_display = ('user','activa' ,'nombre_consulta','fk_caracterizacion',)
	## Filtrar por campos
    list_filter = ('user',)

	## Mostrar 25 registros por página
    list_per_page = 25

    ## Ordenar por usuario
    ordering = ('user',)

class PreguntaAdmin(admin.ModelAdmin):
    """!
	Clase que agrega modelo Pregunta en el panel administrativo

	@author Lully Troconis (ltroconis at cenditel.gob.ve)
	@copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
	@date 10-07-2018
	"""
	## Mostrar los campos
    list_display = ('consulta', 'tipo_pregunta', 'texto_pregunta',)
	## Filtrar por campos
    list_filter = ('consulta',)

	## Mostrar 25 registros por página
    list_per_page = 25

    ## Ordenar por usuario
    ordering = ('consulta',)

class OpcionAdmin(admin.ModelAdmin):
    """!
	Clase que agrega modelo Opcion en el panel administrativo

	@author Lully Troconis (ltroconis at cenditel.gob.ve)
	@copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
	@date 10-07-2018
	"""
	## Mostrar los campos
    list_display = ('pregunta', 'texto_opcion',)
	## Filtrar por campos
    list_filter = ('texto_opcion',)

	## Mostrar 25 registros por página
    list_per_page = 25

    ## Ordenar por usuario
    ordering = ('texto_opcion',)

class RespuestaOpcionesAdmin(admin.ModelAdmin):
    """!
	Clase que agrega modelo RespuestaOpciones en el panel administrativo

	@author Lully Troconis (ltroconis at cenditel.gob.ve)
	@copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
	@date 10-07-2018
	"""
	## Mostrar los campos
    list_display = ('opcion', 'user',)
	## Filtrar por campos
    list_filter = ('user',)

	## Mostrar 25 registros por página
    list_per_page = 25

    ## Ordenar por usuario
    ordering = ('user',)

class RespuestaAbiertaAdmin(admin.ModelAdmin):
    """!
	Clase que agrega modelo RespuestaAbierta en el panel administrativo

	@author Lully Troconis (ltroconis at cenditel.gob.ve)
	@copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
	@date 10-07-2018
	"""
	## Mostrar los campos
    list_display = ('user', 'pregunta', 'es_justificacion',)
	## Filtrar por campos
    list_filter = ('user',)

	## Mostrar 25 registros por página
    list_per_page = 25

    ## Ordenar por usuario
    ordering = ('user',)

class RespuestaUbicacionAdmin(admin.ModelAdmin):
    """!
	Clase que agrega modelo RespuestaUbicacion en el panel administrativo

	@author Lully Troconis (ltroconis at cenditel.gob.ve)
	@copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
	@date 10-07-2018
	"""
	## Mostrar los campos
    list_display = ('user', 'pregunta', 'coordenadas',)
	## Filtrar por campos
    list_filter = ('user',)

	## Mostrar 25 registros por página
    list_per_page = 25

    ## Ordenar por usuario
    ordering = ('user',)

class ExplicSitConsultaAdmin(admin.ModelAdmin):
    """!
	Clase que agrega modelo ExplicSitConsulta en el panel administrativo

	@author Lully Troconis (ltroconis at cenditel.gob.ve)
	@copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
	@date 10-07-2018
	"""
    ## Mostrar los campos
    list_display = ('fk_consulta', 'fk_explicacion',)
	## Filtrar por campos
    list_filter = ('fk_consulta',)

	## Mostrar 25 registros por página
    list_per_page = 25

    ## Ordenar por usuario
    ordering = ('fk_consulta',)

## Registra cada modelo en el panel administrativo
#admin.site.register(RespuestaSino)
admin.site.register(RespuestaSino, RespuestaSinoAdmin)
admin.site.register(Caracterizacion, CaracterizacionAdmin)
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(TipoPregunta)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Opcion)
admin.site.register(RespuestaOpciones, RespuestaOpcionesAdmin)
admin.site.register(RespuestaAbierta, RespuestaAbiertaAdmin)
admin.site.register(RespuestaUbicacion, RespuestaUbicacionAdmin)
admin.site.register(ExplicacionSituacional, adminGeo.OSMGeoAdmin)
admin.site.register(ExplicSitConsulta, ExplicSitConsultaAdmin)
