from django.contrib import admin
from .models import Sancion
# Register your models here. 
class SancionAdmin(admin.ModelAdmin):
	list_display =('gafete_s', 'cantidad_s', 'fecha_s')
	list_filter = ('gafete_s', 'cantidad_s', 'fecha_s')
	search_field = ('gafete_s', 'cantidad_s', 'fecha_s')
admin.site.register(Sancion, SancionAdmin)
