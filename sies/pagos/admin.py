from django.contrib import admin
from .models import Pago
# Register your models here.
class PagoAdmin(admin.ModelAdmin):
	list_display = ('empleado', 'fecha')
	list_filter = ('empleado', 'fecha')
	search_field = ('empleado', 'fecha')
admin.site.register(Pago, PagoAdmin)