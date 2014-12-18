from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


class UserCreationEmailForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=200)
	last_name = forms.CharField(max_length=200)


	class Meta:
		model = User
		fields = ('first_name', 'last_name','email','username')
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
	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		self.user_cache = None #se inicializa en NONE
		super(EmailAuthenticationForm, self).__init__(*args, **kwargs)

	def clean(self):
		email = self.cleaned_data.get('email')#capturar datos
		password = self.cleaned_data.get('password')

		#authenticate devuelve el usuario o NONE
		self.user_cache = authenticate(email=email, password=password)#se captura al usuario que se quiere loggear

		if self.user_cache is None:
			raise forms.ValidationError('Usuario Incorrecto')
		elif not self.user_cache.is_active: #revisa que el usuario este activo, esta info esta en admin
		    raise forms.ValidationError('Usuario Inactivo')

		return self.cleaned_data

	#funcion que regresa el usuario que esta en user_cache
	def get_user(self):
		return self.user_cache


