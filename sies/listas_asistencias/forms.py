from django.shortcuts import render, get_object_or_404 
from django import forms 
from asistencias.models import Asistencia
from eventos.models import Evento
from django.contrib.auth.forms import User 
from listas_asistencias.models import Lista

class SelectEvent(forms.ModelForm):

	#query que devuelve los eventos para que se seleccione alguno
	evento = forms.ModelChoiceField(queryset=Evento.objects.values_list('evento', flat=True).all())
	
	class Meta:
		model = Lista
		exclude = ['idusuario','first_name', 'last_name', 'clave_evento']
	
	def clean(self):

		evento = self.cleaned_data.get('evento')

		#query que contiene la id del evento que se selecciono
		clave_evento = Evento.objects.values_list('id', flat=True).filter(evento=evento)
		#query que contiene los id de usuarios que registraron el evento seleccinado, asistencia es iterable ya q contiene una lista
		asistencias = Asistencia.objects.values_list('idusuario', flat=True).filter(clave_evento=clave_evento)
		
		for id_u in asistencias:
			a = Lista()
			a.idusuario = id_u
			a.first_name = User.objects.values_list('first_name', flat=True).filter(id=id_u)
			a.last_name = User.objects.values_list('last_name', flat=True).filter(id=id_u)
			a.clave_evento = clave_evento
			a.evento = evento
			a.save()

	