from django.contrib import admin 
from .models import Extra
# Register your models here.
class ExtraAdmin(admin.ModelAdmin):
	list_display =('empleado', 'concepto')
	list_filter = ('empleado', 'concepto')
	search_field = ('empleado', 'concepto')
admin.site.register(Extra, ExtraAdmin)
 