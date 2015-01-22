from django.db import models

# Create your models here.
class Pago(models.Model):
	empleado = models.CharField(max_length=200)
	asistencias = models.PositiveIntegerField()
	inasistencias = models.PositiveIntegerField()
	extras = models.PositiveIntegerField()
	sanciones = models.PositiveIntegerField()
	total = models.PositiveIntegerField()
	fecha = models.DateTimeField()

	def __unicode__(self):
		return self.empleado