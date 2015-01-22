from django import forms  
from inasistencias.models import Inasistencia
from asistencias.models import Asistencia 
from eventos.models import Evento 

class PasarLista():

	def insertar_asistencias(self, lista, id_evento):
		for gafete in lista:
			b = Asistencia()
			b.gafete_a = gafete
			b.idevento_a = id_evento
			#obtener fecha def evento
			f = Evento.objects.get(id=id_evento)
			b.fecha_a = f.fecha
			b.save()

	def eliminar_inasistencias(self, lista, id_evento):
		for gafete in lista:
			Inasistencia.objects.filter(gafete_i=gafete).filter(idevento_i=id_evento).delete()
