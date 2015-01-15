from django.contrib import admin
from .models import ConceptoExtra
# Register your models here.
class ConceptoExtraAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'cantidad')
	list_filter = ('nombre', 'cantidad')
	search_field = ('nombre', 'cantidad')
admin.site.register(ConceptoExtra, ConceptoExtraAdmin) 