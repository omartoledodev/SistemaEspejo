from django.shortcuts import render, get_object_or_404  
from django.contrib.auth.decorators import login_required
from .models import Evento
from asistencias.models import Asistencia
from .forms import AddEventForm
from django.contrib.auth.forms import User
from django.contrib.auth import get_user
from listas_asistencias.models import Lista
# Create your views here.
def eventos(request, teatro):
	evento = get_object_or_404(Evento, teatro=teatro)

	return render(request, 'eventos.html',{'evento': evento})

#@login_required 
def event_list(request): 
	form_event = AddEventForm(request.POST or None)

	if request.method == 'POST':
		id_e = request.POST.get('clave_evento')
		#id_e = form_event.clean()
		user = get_user(request) 
		id_u = user.id
		#id_e = user.id
		#--------------------------------------------------------------------
		#query que contiene la clave eventos que ha registrado el usaurio, las claves estan destro de una lista
		eventos_confirmados = Asistencia.objects.values_list('clave_evento', flat=True).filter(idusuario=id_u)
		empal = False
		lista = list(eventos_confirmados)
		id_evento = int(id_e)
		# si el id_evento ya esta en la lista de los eventos que ha confirmado no se inserta, de lo contrario se inserta 
		if id_evento in lista:
			a=1
		else:
			empal = form_event.empalmes(id_u, id_e)

		if empal:
			form_event.insertar(id_u, id_e)

		
	#----------------------------------------------------------------------
	
	event = Evento.objects.all()

	#usuario = get_object_or_404(User)
	usuario = request.user
	id_u = usuario.id
	
	claves_registrados = Asistencia.objects.values_list('clave_evento', flat=True).filter(idusuario=id_u)

	mis_eventos = Evento.objects.filter(id__in=claves_registrados)


	return render(request, 'lista_eventos.html', {'form_event': form_event, 'event': event, 'mis_eventos': mis_eventos})

from rest_framework import viewsets
from eventos.serializers import EventSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class EventoViewSet(viewsets.ModelViewSet):
	#model = Evento
	queryset = Evento.objects.all()
	serializer_class = EventSerializer
	permission_classes = (IsAuthenticated,)