from django import forms  
from userprofiles.models import UserProfile
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm 

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name','email','username')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('username','gafete', 'avatar', 'genero', 'nombre', 'apellido')

class LoginForm(forms.Form):
	email = forms.CharField(max_length=200)
	password = forms.CharField(max_length=200)
