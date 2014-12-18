from django.shortcuts import render
from .forms import UserCreationEmailForm, EmailAuthenticationForm
from django.contrib.auth import login
# Create your views here.
def signup(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():#validar form, funcion heredada
		form.save()#guardar formulario

		#loguear el usuario
		#userprofile
		#redireccionar al home

	return render(request, 'signup.html' , {'form': form})

#vista para loguearse
def signin(request):
	form = EmailAuthenticationForm(request.POST or None)

	if form.is_valid():
		login(request, form.get_user())#llamo al usurio que esta en cache con la funcion get_user que esta en form
		
		#redireccionar al home
	return render(request, 'signin.html', {'form': form})
