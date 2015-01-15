from django.shortcuts import render  
from django import forms 
from .forms import UserCreationEmailForm, EmailAuthenticationForm, DeleteEventForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, get_user
from django.contrib.auth.forms import User
from listas_asistencias.models import Lista
from eventos.models import Evento
from asistencias.models import Asistencia
import datetime 

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
        login(request, form.get_user())
        #redireccionar al home

    return render(request, 'signin.html', {'form':form})
	

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

@login_required(login_url='/signin/')
def socios(request):
	user = get_user(request)
	u=user.password
	return HttpResponse(u)

def cancelar(request): 
	#form = DeleteEventForm(request.POST or None)
	claves_registrados = Asistencia.objects.values_list('clave_evento', flat=True).filter(idusuario=request.user.id)

	mis_eventos = Evento.objects.filter(id__in=claves_registrados)
	now = datetime.datetime.now()

	if request.method == 'POST':
		user = get_user(request)
		id_u = user.id
		id_e = request.POST.get('clave_evento')
		id_evento = int(id_e)

		#eliminar de asistencias y de listas_de_asistencias
		Asistencia.objects.filter(idusuario=id_u).filter(clave_evento=id_evento).delete()
		Lista.objects.filter(idusuario=id_u).filter(clave_evento=id_evento).delete()

	asistencia_conf = Asistencia.objects.filter()
	return render(request, 'cancelar.html', {'now': now, 'mis_eventos': mis_eventos})