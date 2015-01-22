from django.shortcuts import render, get_object_or_404 
from django import forms  
from asistencias.models import Asistencia
from userprofiles.models import UserProfile
from eventos.models import Evento
from django.contrib.auth.forms import User  
from listas_asistencias.models import Lista
from inasistencias.models import Inasistencia
  
 
class AddEventForm(forms.ModelForm): 

	clave_evento = forms.ModelChoiceField(queryset=Evento.objects.values_list('id', flat=True).all())

	class Meta:
		model = Asistencia
		exclude = ['gafete_a', 'idevento_a', 'fecha_a']

	def empalmes(self, gafete, id_e):
		claves_registrados = Asistencia.objects.values_list('idevento_a', flat=True).filter(gafete_a=gafete)
		mis_eventos = Evento.objects.filter(id__in=claves_registrados)

		evento = Evento.objects.get(id=id_e)

		empalmes = 0
		n_empalmes = 0
		
		for e in mis_eventos:
			e_m = e.fecha.month == evento.fecha.month
			e_d = e.fecha.day == evento.fecha.day
			e_h = e.fecha.hour - evento.fecha.hour
			e_h = abs(e_h)
			if e_m and e_d and e_h < 5:
				empalmes = empalmes + 1
			else:
				n_empalmes = n_empalmes +1

		if empalmes > 0:
			return False
		else:
			return True



	def insertar(self,gafete, id_e, id_u):
		#a = Asistencia()
		#a.gafete_a = gafete
		#a.idevento_a = id_e
		#fecha =  Evento.objects.get(id=id_e)
		#a.fecha_a = fecha.fecha
		#a.save()	
		
		#se crea una instancia del clase lista para almacenarlo en las listas de asistencia
		b = Lista()
		
		b.idusuario = id_u
	
		#obtener firts_nae y last_name
		user = User.objects.get(id=id_u)
		f_n = user.first_name
		f_n = str(f_n)
		l_n = user.last_name
		l_n = str(l_n)
		b.gafete_l = gafete
		b.first_name = f_n
		b.last_name = l_n
		#obtener id evento
		b.clave_evento = id_e
		#obtener nombre del evento
		name_evento = Evento.objects.get(id=id_e)
		n_event = name_evento.evento
		n_event = str(n_event)
		b.evento = n_event
		
		b.save()
		#---------------------------------
		c = Inasistencia()
		c.gafete_i = gafete
		c.idevento_i = id_e
		fecha =  Evento.objects.get(id=id_e)
		c.fecha_i = fecha.fecha
		c.save()

	def updategenero(self, genero, id_e):
		e = Evento.objects.get(id=id_e)
		if genero == 'M':
			h = e.hombres - 1
			e.hombres = h 
			e.save()
		else:
			m = e. mujeres - 1
			e.mujeres = m
			e.save()

	def lugares(self, genero, id_e):
		e = Evento.objects.get(id=id_e)
		if genero == 'M':
			if e.hombres == 0:
				return False
			else:
				return True
		else:
			if e.mujeres == 0:
				return False
			else:
				return True