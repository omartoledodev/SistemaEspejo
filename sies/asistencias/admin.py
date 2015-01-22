from django.contrib import admin  
from .models import Asistencia
# Register your models here.
class AsistenciaAdmin(admin.ModelAdmin):
	list_display =('gafete_a', 'idevento_a', 'fecha_a')
	list_filter = ('gafete_a', 'idevento_a', 'fecha_a')
	search_field = ('gafete_a', 'idevento_a', 'fecha_a')
admin.site.register(Asistencia, AsistenciaAdmin)