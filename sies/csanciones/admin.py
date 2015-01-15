from django.contrib import admin 
from .models import ConceptoSancion
# Register your models here.
class CSancionAdmin(admin.ModelAdmin):
	list_display =('nombre', 'cantidad')
	list_filter = ('nombre', 'cantidad')
	search_field = ('nombre', 'cantidad')
admin.site.register(ConceptoSancion, CSancionAdmin)
