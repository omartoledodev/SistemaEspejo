from django import forms 
from userprofiles.models import UserProfile
class SelectEmpleado(forms.ModelForm):
	empleado = forms.ModelChoiceField(queryset=UserProfile.objects.values_list('gafete', flat=True).all())