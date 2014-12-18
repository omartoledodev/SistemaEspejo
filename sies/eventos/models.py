from django.db import models

# Create your models here.


class Eventos(models.Model):
	clave = models.AutoField('Clave', primary_key=True)
	evento = models.CharField(max_length=200)
	teatro = models.CharField(max_length=200)
	fecha = models.DateTimeField()
	hombres = models.PositiveIntegerField()
	mujeres =  models.PositiveIntegerField()


	def __unicode__(self):
		return self.evento