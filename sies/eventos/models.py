from django.db import models
#from teatros.models import Teatro
# Create your models here.


class Evento(models.Model):
	#clave = models.AutoField('Clave', primary_key=True)
	evento = models.CharField(max_length=200)
	teatro = models.CharField(max_length=200)
	fecha = models.DateTimeField()
	hombres = models.PositiveIntegerField()
	mujeres =  models.PositiveIntegerField()

	def get_absolute_url(self):
		return '/eventos/%s/' % self.teatro


	def __unicode__(self):
		return self.evento