from django.contrib import admin
from .models import UserProfile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	list_display =('id','username', 'gafete', 'nombre', 'apellido', 'genero', 'foto')
	list_filter = ('nombre','apellido', 'genero', 'gafete')
	search_field = ('nombre','apellido', 'genero', 'gafete')
admin.site.register(UserProfile, ProfileAdmin)