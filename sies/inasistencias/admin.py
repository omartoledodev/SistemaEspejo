from django.contrib import admin
from inasistencias.models import Inasistencia
# Register your models here.
class InasistenciaAdmin(admin.ModelAdmin):
	list_display =('gafete_i', 'idevento_i', 'fecha_i')
	list_filter = ('gafete_i', 'idevento_i', 'fecha_i')
	search_field = ('gafete_i', 'idevento_i', 'fecha_i')
admin.site.register(Inasistencia, InasistenciaAdmin)