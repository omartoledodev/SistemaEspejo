from django.contrib import admin 
from .models import Extra
# Register your models here.
class ExtraAdmin(admin.ModelAdmin): 
	list_display =('gafete_e', 'cantidad_e', 'fecha_e')
	list_filter = ('gafete_e', 'cantidad_e', 'fecha_e')
	search_field = ('gafete_e', 'cantidad_e', 'fecha_e')
admin.site.register(Extra, ExtraAdmin)
 