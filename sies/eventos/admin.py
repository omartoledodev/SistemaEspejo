from django.contrib import admin
from .models import Evento
# Register your models here.

class EventAdmin(admin.ModelAdmin):
	list_display =('evento', 'teatro', 'fecha', 'hombres', 'mujeres')
	list_filter = ('teatro','fecha')
	search_field = ('evento', 'teatro')
admin.site.register(Evento, EventAdmin)

