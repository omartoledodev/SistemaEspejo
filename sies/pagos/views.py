from django.shortcuts import render 
from userprofiles.models import UserProfile
from asistencias.models import Asistencia
from inasistencias.models import Inasistencia 
from extras.models import Extra
from sanciones.models import Sancion
from eventos.models import Evento
from django.contrib.auth import authenticate, get_user
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import datetime 

# Create your views here.
def pagos(request):
	title = "Pagos"
	empleados = UserProfile.objects.all()[0:]
	now = datetime.datetime.now()
	today = str(now.strftime("%A %d. %B %Y"))

	if request.method == 'POST':
		gafete = request.POST.get('gefete')
		start = request.POST.get('start')
		end = request.POST.get('end')
		try:
			imprimir = request.POST.get('imprimir')
		except:
			imprimir = False
		#---------------------------------
		try:
			start_anio = int(start[0:4])
			start_mes = int(start[5:7])
			start_dia = int(start[8:10])

			end_anio = int(end[0:4])
			end_mes = int(end[5:7])
			end_dia = int(end[8:10])
			#---------------------------------
			fecha_start = datetime.date(start_anio, start_mes, start_dia)
			fecha_end = datetime.date(end_anio, end_mes, end_dia)
			#---------------------------------
		except:
			fecha_start = datetime.date.today()
			fecha_end = datetime.date.today()

		pagos = 150.0
		#queryes
		emple = UserProfile.objects.get(gafete=gafete)
		empleado = emple.nombre + " " + emple.apellido
		#Asistencias
		ids_asistencias =  Asistencia.objects.values_list('idevento_a', flat=True).filter(gafete_a=gafete).filter(fecha_a__range=(fecha_start, fecha_end))
		a = Asistencia.objects.filter(gafete_a=gafete).filter(fecha_a__range=(fecha_start, fecha_end)).count()
		eventos_a = list(Evento.objects.values_list('fecha', flat=True).filter(id__in=ids_asistencias))
		total_asistencias = a * pagos
		t_a = str(total_asistencias)
		#Inasistencias
		ids_inasistencias = Inasistencia.objects.values_list('idevento_i', flat=True).filter(gafete_i=gafete).filter(fecha_i__range=(fecha_start, fecha_end))
		i = Inasistencia.objects.filter(gafete_i=gafete).filter(fecha_i__range=(fecha_start, fecha_end)).count()
		eventos_i = Evento.objects.values_list('fecha', flat=True).filter(id__in=ids_inasistencias)
		total_inasistencias = i * pagos
		t_i = str(total_inasistencias)
		#Pagos Extras
		e = Extra.objects.filter(gafete_e=gafete).filter(fecha_e__range=(fecha_start, fecha_end)).values_list('cantidad_e', flat=True)
		total_extras = sum(e) * 1.0
		t_e = str(total_extras)
		#Sanciones
		s = Sancion.objects.filter(gafete_s=gafete).filter(fecha_s__range=(fecha_start, fecha_end)).values_list('cantidad_s', flat=True)
		total_sanciones = sum(s) * 1.0
		t_s = str(total_sanciones)
		#TOTAL
		total = total_asistencias - total_inasistencias + total_extras - total_sanciones
		t = str(total)
		#--------------------------------------PDF------------------------------------------------
		if imprimir:
			# Create the HttpResponse object with the appropriate PDF headers.
		    response = HttpResponse(content_type='application/pdf')
		    response['Content-Disposition'] = 'attachment; filename="pago.pdf"'

		    # Create the PDF object, using the response object as its "file."
		    i=700
		    p = canvas.Canvas(response)

		    # Draw things on the PDF. Here's where the PDF generation happens.
		    # See the ReportLab documentation for the full list of functionality.
		   	
		    p.drawString(50,800 , today)#fecha
		    p.drawString(120, 750, empleado)#empleado
		    p.drawString(50, 750, 'Empleado: ')
		    p.drawString(50,720, 'Asistencias')
		    for a in eventos_a:
		    	a=str(a.strftime("%A %d. %B %Y"))
		    	p.drawString(50, i, a)
		    	i=i-15

		    p.drawString(50, i-20, "Descripcion")
		    p.drawString(50, i-40, "Total por Asistencias :")
		    p.drawString(200, i-40, t_a)
		    p.drawString(50, i-55, "Total por Inasistencias :")
		    p.drawString(200, i-55, t_i)
		    p.drawString(50, i-70, "Total por Extras :")
		    p.drawString(200, i-70, t_e)
		    p.drawString(50, i-85, "Total por Sanciones :")
		    p.drawString(200, i-85, t_s)
		    p.drawString(50, i-100, "Total :")
		    p.drawString(200, i-100, t)

		    # Close the PDF object cleanly, and we're done.
		    p.showPage()
		    p.save()
		    return response
		#-----------------------------------------------------------------------------------------
		return render(request, 'pagos.html', {'empleados': empleados, 'gafete':gafete, 'total': total, 'eventos_a':eventos_a, 'eventos_i':eventos_i, 'fecha_start':fecha_start,'fecha_end':fecha_end , 'title':title,})
	
	else:
		return render(request, 'pagos.html', {'empleados': empleados, 'title':title})

def pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    now = datetime.datetime.now()
    empleado = 'Omar Toledo'
    asi = ['lunes', 'martes', 'miercoles', 'jueves','viernes', 'sabado', 'domingo']
    i=700
    a = 150
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
   	
    p.drawString(50,800 , 'fecha')#fecha
    p.drawString(120, 750, empleado)#empleado
    p.drawString(50, 750, 'Empleado: ')
    p.drawString(50,730, 'Asistencias')
    for a in asi:
    	p.drawString(50, i, a)
    	i=i-15
    stri = str(i)
    p.drawString(50, i-20, stri)
    p.drawString(50, i-40, "Total por Asistencias :")
    p.drawString(200, i-40, a)
    p.drawString(50, i-55, "Total por Inasistencias :")
    p.drawString(50, i-70, "Total por Extras :")
    p.drawString(50, i-85, "Total por Sanciones :")
    p.drawString(50, i-100, "Total")
    p.drawString(500,20, "yo")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

	