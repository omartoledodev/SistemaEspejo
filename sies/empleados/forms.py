from django import forms   
from django.contrib.auth import authenticate, get_user 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import User
from django.shortcuts import redirect
from eventos.models import Evento



class UserCreationEmailForm(UserCreationForm):
	email = forms.EmailField()
	#first_name = forms.CharField(max_length=200)
	#last_name = forms.CharField(max_length=200)

 
	class Meta:
		model = User
		fields = ('username','email')
		#fields = '__all__'

		#validar email
		def clean_email(self):
			email = self.cleaned_data["email"]
			try:
				User._default_manager.get(email=email)
			except User.DoesNotExist:
				return email
			raise forms.ValidationError("Email Duplicate")


class EmailAuthenticationForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(label='Password', widget=forms.PasswordInput)#init del padre,se define personalizado

	def __init__(self, *args, **kwargs):#constructor
		self.user_cache = None #incializar variable vacia
		super(EmailAuthenticationForm, self).__init__(*args, **kwargs)#super padre de la clase para hacer el init

	def clean(self):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')

		self.user_cache = authenticate(email=email, password=password)

		#la funcion authenticate puede devolver el usuario or none
		if self.user_cache is None:
			raise forms.ValidationError('Usuario Incorrecto')#levantar un error si  los datos no son correctos
		elif not self.user_cache.is_active:
			raise forms.ValidationError('usuario inactivo')

		return self.cleaned_data

	def get_user(self):
		return 	self.user_cache

class DeleteEventForm(forms.Form):
	clave_evento = forms.ModelChoiceField(queryset=Evento.objects.values_list('id', flat=True).all())