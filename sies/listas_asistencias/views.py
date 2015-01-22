from django.shortcuts import render
from .forms import SelectEvent
from eventos.models import Evento 
from asistencias.models import Asistencia
from inasistencias.models import Inasistencia 
from extras.models import Extra 
from sanciones.models import Sancion 
from userprofiles.models import UserProfile
from django.contrib.auth.forms import User
from pagos.models import Pago 
# Create your views here.

def lista(request):
	list_form = SelectEvent(request.POST or None)

	return render(request, 'lista.html', {'list_form': list_form, })

def asistencias(request):
	empleados =  UserProfile.objects.all()[0:]

	return render(request, 'asistencias.html', {'empleados': empleados})
 
