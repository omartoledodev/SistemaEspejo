from django.contrib import admin
from .models import Lista
# Register your models here.
class ListAdmin(admin.ModelAdmin):
	list_display =('idusuario','gafete_l','first_name', 'last_name', 'clave_evento', 'evento')
	list_filter = ('first_name','last_name', 'evento')
	search_field = ('first_name','last_name', 'evento')
admin.site.register(Lista, ListAdmin)