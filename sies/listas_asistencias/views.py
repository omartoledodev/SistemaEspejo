from django.shortcuts import render
from asistencias.models import Asistencia
from eventos.models import Evento
from django.contrib.auth.forms import User 
from .forms import SelectEvent
# Create your views here.

def lista(request):
	list_form = SelectEvent(request.POST or None)

	return render(request, 'lista.html', {'list_form': list_form, })
 
