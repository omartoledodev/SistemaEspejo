from django.shortcuts import render
from eventos.models import Evento 
from listas_asistencias.models import Lista
from asistencias.models import Asistencia
from inasistencias.models import Inasistencia 
from extras.models import Extra 
from sanciones.models import Sancion 
from userprofiles.models import UserProfile
from django.contrib.auth.forms import User
from pagos.models import Pago 
from .forms import PasarLista
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import datetime

def asistencias(request): 
	eventos =  Evento.objects.all()[0:]
	now = datetime.datetime.now()
	today = str(now.strftime("%A %d. %B %Y"))

	if request.method == 'POST':
		id_evento = request.POST.get('id_evento')
		empleados = Lista.objects.filter(clave_evento=id_evento)
		evento = Evento.objects.get(id=id_evento)
		try:
			imprimir = request.POST.get('imprimir')
		except:
			imprimir = False
		
		post = request.POST.keys()
		
		lista = list()
		l = list()
		for a in post:
			try:
				i = int(a)
				lista.append(i)
			except:
				l.append(a)

		pl = PasarLista()
		pl.insertar_asistencias(lista, id_evento)
		pl.eliminar_inasistencias(lista, id_evento)
		#--------------------------------------PDF------------------------------------------------
		if imprimir:
			# Create the HttpResponse object with the appropriate PDF headers.
		    response = HttpResponse(content_type='application/pdf')
		    response['Content-Disposition'] = 'attachment; filename="lista.pdf"'

		    # Create the PDF object, using the response object as its "file."
		    i=650
		    p = canvas.Canvas(response)

		    # Draw things on the PDF. Here's where the PDF generation happens.
		    # See the ReportLab documentation for the full list of functionality.
		   	
		    p.drawString(50,800 , today)#fecha
		    p.drawString(120, 750, evento.evento)
		    f=evento.fecha
		    fe = str(f.strftime("%A %d. %B %Y"))
		    p.drawString(190, 750, fe)
		    p.drawString(50, 750, 'Evento: ')
		    p.drawString(50,720, 'Lista de Asistencia')
		    p.drawString(50, 680, "Gafete   Nombre     Apellido")
		    for a in empleados:
		    	gafete = str(a.gafete_l)
		    	a=str(gafete + '      ' + a.first_name + '      ' + a.last_name)
		    	p.drawString(50, i, a)
		    	i=i-15

		    # Close the PDF object cleanly, and we're done.
		    p.showPage()
		    p.save()
		    return response
		#-----------------------------------------------------------------------------------------
		return render(request, 'asistencias.html', {'eventos': eventos, 'empleados': empleados, 'evento': evento,'lista':lista,})
	else:
		return render(request, 'asistencias.html', {'eventos': eventos})

def sanciones(request):
	title = "Sanciones"
	now = datetime.datetime.now()
	empleados = UserProfile.objects.all()[0:]

	if request.method == "POST": 
		gafete = request.POST.get('gafete')
		cantidad = request.POST.get('cantidad')
		fecha = request.POST.get('fecha')

		a = Sancion()
		a.gafete_s = gafete
		a.cantidad_s = cantidad
		a.fecha_s = fecha
		a.save()

	return render(request, 'sanciones.html', {'title': title, 'now': now , 'empleados': empleados})

def extras(request):
	title = "Pagos Extras"
	now = datetime.datetime.now()
	empleados = UserProfile.objects.all()[0:]

	if request.method == "POST":
		gafete = request.POST.get('gafete')
		cantidad = request.POST.get('cantidad')
		fecha = request.POST.get('fecha')

		a = Extra()
		a.gafete_e = gafete
		a.cantidad_e = cantidad
		a.fecha_e = fecha
		a.save()

	return render(request, 'extras.html', {'title': title, 'now': now , 'empleados': empleados})