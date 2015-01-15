from django.contrib import admin
from .models import Sancion
# Register your models here. 
class SancionAdmin(admin.ModelAdmin):
	list_display =('empleado', 'concepto')
	list_filter = ('empleado', 'concepto')
	search_field = ('empleado', 'concepto')
admin.site.register(Sancion, SancionAdmin)
